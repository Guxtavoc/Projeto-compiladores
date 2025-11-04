from antlr4 import *
from gramaticaCLexer import gramaticaCLexer
from gramaticaCParser import gramaticaCParser
from graphviz import Digraph
import os

class TreeVisualizer:
    def __init__(self):
        self.node_counter = 0
        self.graph = Digraph(comment='Árvore Sintática', format='png')
        self._setup_graph()
    
    def _setup_graph(self):
        """Configura o estilo do gráfico"""
        self.graph.attr(rankdir='TB', size='14,10')
        self.graph.attr('node', 
                       shape='box', 
                       style='rounded', 
                       fontname='Arial',
                       fontsize='10',
                       margin='0.2')
        self.graph.attr('edge', fontname='Arial', fontsize='9')
    
    def visualize(self, tree, parser, output_filename="arvore_sintatica"):
        """Gera a visualização da árvore"""
        self.node_counter = 0
        self._add_node(tree, parser)
        
        # Renderiza o gráfico
        try:
            output_path = self.graph.render(
                output_filename, 
                view=True, 
                cleanup=True
            )
            return output_path
        except Exception as e:
            print(f"❌ Erro ao gerar imagem: {e}")
            # Salva o código DOT para debug
            with open(f"{output_filename}.dot", "w", encoding="utf-8") as f:
                f.write(self.graph.source)
            print(f"📄 Código DOT salvo em: {output_filename}.dot")
            return None
    
    def _add_node(self, node, parser, parent_id=None):
        """Adiciona um nó e seus filhos recursivamente"""
        current_id = str(self.node_counter)
        self.node_counter += 1
        
        # Define o label do nó
        label = self._get_node_label(node, parser)
        
        # Adiciona o nó ao gráfico
        self.graph.node(current_id, label)
        
        # Conecta ao pai se existir
        if parent_id is not None:
            self.graph.edge(parent_id, current_id)
        
        # Processa os filhos
        if hasattr(node, 'getChildCount'):
            for i in range(node.getChildCount()):
                child = node.getChild(i)
                self._add_node(child, parser, current_id)
    
    def _get_node_label(self, node, parser):
        """Retorna o label apropriado para o nó"""
        if isinstance(node, tree.Tree.TerminalNodeImpl):
            # Nó terminal (token)
            text = node.getText()
            # Escapa caracteres especiais
            text = text.replace('"', '\\"').replace('\n', '\\n')
            return f'TOKEN: "{text}"'
        else:
            # Nó não-terminal (regra)
            if hasattr(node, 'getRuleIndex'):
                rule_index = node.getRuleIndex()
                if rule_index >= 0 and hasattr(parser, 'ruleNames'):
                    rule_names = parser.ruleNames
                    if rule_index < len(rule_names):
                        return rule_names[rule_index]
            return "Nó"

def main():
    # Lista arquivos .c disponíveis
    c_files = []
    for root, dirs, files in os.walk("."):
        for file in files:
            if file.endswith(".c"):
                c_files.append(os.path.join(root, file))
    
    if not c_files:
        print("❌ Nenhum arquivo .c encontrado!")
        return
    
    print("📁 Arquivos .c disponíveis:")
    for i, file in enumerate(c_files, 1):
        print(f"{i}. {file}")
    
    # Seleciona arquivo
    try:
        choice = int(input(f"\nEscolha um arquivo (1-{len(c_files)}): ")) - 1
        if choice < 0 or choice >= len(c_files):
            print("❌ Escolha inválida!")
            return
        selected_file = c_files[choice]
    except (ValueError, IndexError):
        print("❌ Escolha inválida!")
        return
    
    try:
        print(f"\n🔍 Analisando: {selected_file}")
        input_stream = FileStream(selected_file, encoding="utf-8")
        lexer = gramaticaCLexer(input_stream)
        tokens = CommonTokenStream(lexer)
        parser = gramaticaCParser(tokens)
        tree = parser.programa()
        
        print("✅ Análise sintática bem-sucedida!")
        print(f"\n🌳 Árvore textual:\n{tree.toStringTree(recog=parser)}")
        
        # Gera visualização
        visualizer = TreeVisualizer()
        output_path = visualizer.visualize(tree, parser, "arvore_sintatica")
        
        if output_path:
            print(f"\n📊 Árvore visual gerada: {output_path}")
        
    except FileNotFoundError:
        print("❌ Arquivo não encontrado!")
    except Exception as e:
        print(f"❌ Erro durante a análise: {e}")

if __name__ == "__main__":
    main()