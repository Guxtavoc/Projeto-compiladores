from antlr4 import *
from gramaticaCLexer import gramaticaCLexer
from gramaticaCParser import gramaticaCParser
import sys
import os
import glob

def analisar_arquivo(arquivo):
    """Analisa um único arquivo e retorna a árvore e o parser"""
    try:
        input_stream = FileStream(arquivo, encoding="utf-8")
        lexer = gramaticaCLexer(input_stream)
        tokens = CommonTokenStream(lexer)
        parser = gramaticaCParser(tokens)
        tree = parser.programa()
        return tree, parser, None
    except Exception as e:
        return None, None, str(e)

def main():
    if len(sys.argv) > 1:
        # Analisa arquivos passados como argumentos
        arquivos = sys.argv[1:]
    else:
        # Analisa todos os arquivos .c do diretório
        arquivos = glob.glob("*.c")
        if not arquivos:
            print("Nenhum arquivo .c encontrado!")
            print("Uso: python analisador.py [arquivo1.c arquivo2.c ...]")
            return
    
    for arquivo in arquivos:
        if not os.path.exists(arquivo):
            print(f"❌ Arquivo não encontrado: {arquivo}")
            continue
        
        print(f"\n{'='*60}")
        print(f"📁 Analisando: {arquivo}")
        print(f"{'='*60}")
        
        tree, parser, erro = analisar_arquivo(arquivo)
        
        if erro:
            print(f"❌ Erro: {erro}")
        else:
            print("✅ Análise sintática bem-sucedida!")
            print(f"🌳 Árvore: {tree.toStringTree(recog=parser)}")

if __name__ == "__main__":
    main()