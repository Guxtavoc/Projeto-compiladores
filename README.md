# Projeto Compiladores - IFMT 2025/2

Um compilador simples baseado na linguagem C, desenvolvido com ANTLR para a disciplina de Compiladores.

## 📋 Descrição

Este projeto visa implementar um compilador completo para uma linguagem de programação inspirada em C, incluindo as fases de análise léxica, sintática, semântica e geração de código.

## 🛠️ Tecnologias Utilizadas

- **ANTLR 4** - Framework para construção de compiladores
- **Python** - Linguagem de implementação do compilador
- **C** - Linguagem alvo / inspiração para a linguagem fonte

## 📁 Estrutura do Projeto

## Como Executar

### Pré-requisitos
- Python 3.8+
- [ANTLR 4.13.1](https://www.antlr.org/download/antlr-4.13.1-complete.jar)
- Java (para executar o ANTLR)

## Configuração do Ambiente
```bash
# Criar ambiente virtual
python -m venv virtual

# Ativar (Windows)
virtual\Scripts\activate

# Instalar dependências
pip install -r requirements.txt
```
## Instalação das Dependências
```bash
# Instalar runtime do ANTLR para Python
pip install antlr4-python3-runtime

# Ou via requirements.txt
pip install -r requirements.txt
```
## Execução do Compilador
```bash
# Gerar arquivos semanticos baseados em nossa pseudolinguagem
java -jar ./antlr-4.13.1-complete.jar -Dlanguage=Python3 gramaticaC.g4

# Executar o compilador
python.exe main.py .\arquivofonte.c

# Ou com mais opções
python src/main.py --input arquivo_fonte --output saida.asm
```
## 👥 Desenvolvimento

- **Disciplina**: Compiladores
- **Instituição**: IFMT - 2025/2
- **Desenvolvedores**:
  - [Gustavo Curado](https://github.com/Guxtavoc)
  - [Daniel Bonfim](https://github.com/DanielBarros19)

📅 Status do Projeto Em Desenvolvimento 

Análise Léxica

Análise Sintática

Análise Semântica

Geração de Código


