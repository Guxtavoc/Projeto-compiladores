from antlr4 import *
from gramaticaCLexer import gramaticaCLexer
from gramaticaCParser import gramaticaCParser

def main():
    input_stream = FileStream("teste.c", encoding="utf-8")
    lexer = gramaticaCLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = gramaticaCParser(tokens)
    tree = parser.programa()
    print(tree.toStringTree(recog=parser))

if __name__ == "__main__":
    main()