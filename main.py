import sys
import os
from antlr4 import FileStream, CommonTokenStream
from gramaticaCLexer import gramaticaCLexer
from gramaticaCParser import gramaticaCParser
from antlr4.tree.Tree import TerminalNodeImpl
from graphviz import Digraph
from codigo_intermediario import CodigoIntermediario
from codigo_final import CodigoFinal
from semantico import Semantico

class TreeVisualizer:
    def __init__(self):
        self.node_counter = 0
        self.graph = Digraph(comment='Arvore Sintatica', format='png')
        self.graph.attr(rankdir='TB')

    def visualize(self, tree, parser, output_filename="arvore"):
        self.node_counter = 0
        self.graph = Digraph(comment='Arvore Sintatica', format='png')
        self.graph.attr(rankdir='TB')
        self._add_node(tree, parser)
        base, ext = os.path.splitext(output_filename)
        if base == "":
            base = output_filename
        rendered = self.graph.render(base, view=False, cleanup=True)
        return rendered

    def _add_node(self, node, parser, parent_id=None):
        current_id = str(self.node_counter)
        self.node_counter += 1

        label = self._get_node_label(node, parser)
        label = label.replace("\n", "\\n").replace('"', '\\"')
        self.graph.node(current_id, label)

        if parent_id is not None:
            self.graph.edge(parent_id, current_id)

        if hasattr(node, "getChildCount"):
            for i in range(node.getChildCount()):
                child = node.getChild(i)
                self._add_node(child, parser, current_id)

    def _get_node_label(self, node, parser):
        from antlr4.tree.Tree import TerminalNodeImpl
        if isinstance(node, TerminalNodeImpl):
            return f'TOKEN: {node.getText()}'
        else:
            try:
                rule_index = node.getRuleIndex()
                if rule_index >= 0:
                    return parser.ruleNames[rule_index]
            except Exception:
                pass
        return type(node).__name__

#gera o nome dos arquivos de output com base no nome original
def criar_nome_saida(caminho, sufixo, extensao):
    base, _ = os.path.splitext(caminho)
    return f"{base}_{sufixo}.{extensao}"


def main():
    if len(sys.argv) < 2:
        print("Uso: python main.py <arquivo.c>")
        sys.exit(1)

    arquivo = sys.argv[1]
    if not os.path.isfile(arquivo):
        print(f"Arquivo não encontrado: {arquivo}")
        sys.exit(1)

    try:
        #analise lexica e sintatica
        input_stream = FileStream(arquivo, encoding="utf-8")
        lexer = gramaticaCLexer(input_stream)
        tokens = CommonTokenStream(lexer)
        parser = gramaticaCParser(tokens)
        tree = parser.programa()

        print("Análise sintática concluída!")
        print("Árvore textual:", tree.toStringTree(recog=parser))

        #gera a arvore sintatica com o grafiz
        visualizer = TreeVisualizer()
        nome_arvore = criar_nome_saida(arquivo, "arvore", "png")
        try:
            caminho_arvore = visualizer.visualize(tree, parser, nome_arvore)
            print(f"Árvore sintática visual gerada em: {caminho_arvore}")
        except Exception as e:
            print("Falha ao gerar PNG da árvore:", e)

        #faz a analise semantica com o visitor
        sem = Semantico()
        sem.visit(tree)

        if hasattr(sem, "erros") and sem.erros:
            print("\nErros semânticos encontrados:")
            for erro in sem.erros:
                print(" -", erro)
            print("Interrompendo geração devido a erros semânticos.")
            sys.exit(2)
        else:
            print("Análise semântica concluída sem erros!")

        #cria o TAC com o visitor
        tac_gen = CodigoIntermediario()
        tac_gen.visit(tree)
        tac = tac_gen.code  

        nome_tac = criar_nome_saida(arquivo, "tac", "txt")
        with open(nome_tac, "w", encoding="utf-8") as f:
            for line in tac:
                f.write(line + "\n")
        print(f"Código intermediário (TAC) salvo em: {nome_tac}")

        #gera o codigo final utilizando o TAC
        final_gen = CodigoFinal(tac)
        codigo_py = final_gen.gerar()

        nome_final = criar_nome_saida(arquivo, "final", "py")
        with open(nome_final, "w", encoding="utf-8") as f:
            f.write(codigo_py)
        print(f"Código final gerado em: {nome_final}")

    except Exception as e:
        print("Erro não esperado:", e)
        sys.exit(99)


if __name__ == "__main__":
    main()
