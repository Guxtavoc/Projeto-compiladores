from antlr4 import *
from gramaticaCLexer import gramaticaCLexer
from gramaticaCParser import gramaticaCParser
from graphviz import Digraph
import sys

from semantico import Semantico
from antlr4.tree.Tree import TerminalNodeImpl


class TreeVisualizer:
    def __init__(self):
        self.node_counter = 0
        self.graph = Digraph(comment='Arvore Sintatica', format='png')
        self.graph.attr(rankdir='TB')

    def visualize(self, tree, parser, output_filename="arvore_sintatica"):
        self.node_counter = 0
        self._add_node(tree, parser)
        return self.graph.render(output_filename, view=False, cleanup=True)

    def _add_node(self, node, parser, parent_id=None):
        current_id = str(self.node_counter)
        self.node_counter += 1

        label = self._get_node_label(node, parser)
        self.graph.node(current_id, label)

        if parent_id is not None:
            self.graph.edge(parent_id, current_id)

        if hasattr(node, 'getChildCount'):
            for i in range(node.getChildCount()):
                self._add_node(node.getChild(i), parser, current_id)

    def _get_node_label(self, node, parser):
        if isinstance(node, TerminalNodeImpl):
            return f"TOKEN: {node.getText()}"
        else:
            return parser.ruleNames[node.getRuleIndex()]


def main():
    arquivo = sys.argv[1]

    try:
        input_stream = FileStream(arquivo)
        lexer = gramaticaCLexer(input_stream)
        tokens = CommonTokenStream(lexer)
        parser = gramaticaCParser(tokens)
        tree = parser.programa()

        print("\n✔ Análise Sintática OK!")
        print("Árvore textual:", tree.toStringTree(recog=parser))

        # Visualização
        visualizer = TreeVisualizer()
        output = visualizer.visualize(tree, parser)
        print("Árvore sintática visual gerada em:", output)

        # Análise semântica
        sem = Semantico()
        sem.visit(tree)

        if sem.erros:
            print("\n❌ Erros Semânticos:")
            for e in sem.erros:
                print(" -", e)
        else:
            print("\n✔ Análise semântica concluída sem erros!")

    except Exception as e:
        print("Erro:", e)


if __name__ == "__main__":
    main()
