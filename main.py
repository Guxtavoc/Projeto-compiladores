from antlr4 import *
from gramaticaCLexer import gramaticaCLexer
from gramaticaCParser import gramaticaCParser
from graphviz import Digraph
import sys

class TreeVisualizer:
    def __init__(self):
        self.node_counter = 0
        self.graph = Digraph(comment='Arvore Sintatica', format='png')
        self.graph.attr(rankdir='TB')
    
    def visualize(self, tree, parser, output_filename="arvore_sintatica"):
        self.node_counter = 0
        self._add_node(tree, parser)
        return self.graph.render(output_filename, view=True, cleanup=True)
    
    def _add_node(self, node, parser, parent_id=None):
        current_id = str(self.node_counter)
        self.node_counter += 1
        
        label = self._get_node_label(node, parser)
        self.graph.node(current_id, label)
        
        if parent_id is not None:
            self.graph.edge(parent_id, current_id)
        
        if hasattr(node, 'getChildCount'):
            for i in range(node.getChildCount()):
                child = node.getChild(i)
                self._add_node(child, parser, current_id)
    
    def _get_node_label(self, node, parser):
        if isinstance(node, tree.Tree.TerminalNodeImpl):
            text = node.getText().replace('"', '\\"')
            return f'TOKEN: "{text}"'
        else:
            if hasattr(node, 'getRuleIndex'):
                rule_index = node.getRuleIndex()
                if rule_index >= 0:
                    rule_names = parser.ruleNames
                    return rule_names[rule_index]
            return "No"

def main():
    if len(sys.argv) != 2:
        print("Uso: python main.py <arquivo.c>")
        return
    
    arquivo = sys.argv[1]
    
    try:
        input_stream = FileStream(arquivo)
        lexer = gramaticaCLexer(input_stream)
        tokens = CommonTokenStream(lexer)
        parser = gramaticaCParser(tokens)
        tree = parser.programa()
        
        print("Analise sintatica concluida!")
        print("Arvore textual:", tree.toStringTree(recog=parser))
        
        visualizer = TreeVisualizer()
        output_path = visualizer.visualize(tree, parser)
        print("Arvore visual gerada:", output_path)
        
    except Exception as e:
        print("Erro:", e)

if __name__ == "__main__":
    main()