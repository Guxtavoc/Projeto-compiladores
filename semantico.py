from gramaticaCVisitor import gramaticaCVisitor
from gramaticaCParser import gramaticaCParser

class Semantico(gramaticaCVisitor):
    def __init__(self):
        # tabela: nome → tipo
        self.tabela = {}
        self.erros = []

    # -----------------------------------------------------
    # Declaração: tipo ID ('=' expr)? (',' ID ('=' expr)?)* ';'
    # -----------------------------------------------------
    def visitDeclaracao(self, ctx: gramaticaCParser.DeclaracaoContext):
        tipo = ctx.tipo().getText()

        for id_token in ctx.ID():
            nome = id_token.getText()

            if nome in self.tabela:
                self.erros.append(f"Variável '{nome}' redeclarada.")
            else:
                self.tabela[nome] = tipo

        return self.visitChildren(ctx)

    # -----------------------------------------------------
    # Atribuição: ID '=' expressao
    # -----------------------------------------------------
    def visitAtribuicao(self, ctx: gramaticaCParser.AtribuicaoContext):
        nome = ctx.ID().getText()

        if nome not in self.tabela:
            self.erros.append(f"Variável '{nome}' usada sem declaração.")
        else:
            tipo_var = self.tabela[nome]
            tipo_expr = self._get_tipo_expr(ctx.expressao())

            if tipo_var == "int" and tipo_expr == "float":
                self.erros.append(
                    f"Atribuição inválida: variável '{nome}' (int) não pode receber float."
                )

        return self.visitChildren(ctx)

    # -----------------------------------------------------
    # Uso de variáveis no átomo
    # -----------------------------------------------------
    def visitAtomo(self, ctx: gramaticaCParser.AtomoContext):
        if ctx.ID():
            nome = ctx.ID().getText()
            if nome not in self.tabela:
                self.erros.append(f"Variável '{nome}' usada sem declaração.")
        return self.visitChildren(ctx)

    # -----------------------------------------------------
    # Inferência de tipo da expressão
    # -----------------------------------------------------
    def _get_tipo_expr(self, ctx):
        # Se é um átomo diretamente
        if isinstance(ctx, gramaticaCParser.AtomoContext):
            # número inteiro
            if ctx.NUMERO():
                return "int"
            # número real
            if ctx.REAL():
                return "float"
            # identificador
            if ctx.ID():
                nome = ctx.ID().getText()
                return self.tabela.get(nome, "desconhecido")
            # ( expressao )
            if ctx.expressao():
                return self._get_tipo_expr(ctx.expressao())

        # Se a expressão tem filhos (operação binária)
        if ctx.getChildCount() == 3:
            filho0 = ctx.getChild(0)
            filho2 = ctx.getChild(2)

            tipo_esq = self._get_tipo_expr(filho0)
            tipo_dir = self._get_tipo_expr(filho2)

            if tipo_esq == "float" or tipo_dir == "float":
                return "float"
            return "int"

        # unário: +x ou -x
        if ctx.getChildCount() == 2:
            return self._get_tipo_expr(ctx.getChild(1))

        return "desconhecido"
