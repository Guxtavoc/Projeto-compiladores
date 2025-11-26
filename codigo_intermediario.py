from gramaticaCVisitor import gramaticaCVisitor
from gramaticaCParser import gramaticaCParser
from antlr4.tree.Tree import TerminalNodeImpl


class CodigoIntermediario(gramaticaCVisitor):

    def __init__(self):
        super().__init__()
        self.temp_count = 0
        self.label_count = 0
        self.code = []

    # Cria variaveis temporarios
    def new_temp(self):
        self.temp_count += 1
        return f"t{self.temp_count}"
    
    # cria labels
    def new_label(self):
        self.label_count += 1
        return f"L{self.label_count}"

    #escreve no arquivo final
    def emit(self, instr):
        self.code.append(instr)

    # visitar (percorrer a arvore)
    def visitPrograma(self, ctx):
        self.visitChildren(ctx)
        return self.code
    
    def visitBloco(self, ctx):
        return self.visitChildren(ctx)

    #salva no arquivo a declaração de variaveis
    def visitDeclaracao(self, ctx):
        for id_token in ctx.ID():
            nome = id_token.getText()
            self.emit(f"decl {nome}")
        return None

    #salva no arquivo a atribuição de variaveis
    def visitAtribuicao(self, ctx):
        nome = ctx.ID().getText()
        expr_ctx = ctx.expressao()
        place, _ = self._gen_expr(expr_ctx)
        self.emit(f"{nome} = {place}")
        return None

    # printf
    #ele percorre o nó de escrita e transforma o conteudo em TAC
    def visitEscrita(self, ctx):
        args = []
        inside = False

        for i in range(ctx.getChildCount()):
            ch = ctx.getChild(i)
            txt = ch.getText()

            if txt == "(":
                inside = True
                continue
            if txt == ")":
                break
            if not inside:
                continue

            if isinstance(ch, TerminalNodeImpl):
                if ch.getSymbol().type == gramaticaCParser.STRING:
                    args.append(ch.getText())
            else:
                place, _ = self._gen_expr(ch)
                args.append(place)

        if len(args) == 1:
            self.emit(f"print({args[0]})")
        elif len(args) > 1:
            self.emit(f"print({', '.join(args)})")
        else:
            self.emit("print()")

        return None

    #scanf
    def visitLeitura(self, ctx):
        for id_token in ctx.ID():
            nome = id_token.getText()
            self.emit(f"read {nome}")
        return None

    #while
    #condiciona o while em tac
    def visitEnquanto(self, ctx):
        start = self.new_label()
        end = self.new_label()

        self.emit(f"{start}:")
        cond_place, _ = self._gen_expr(ctx.expressao())
        self.emit(f"if {cond_place} == 0 goto {end}")

        self.visit(ctx.bloco())

        self.emit(f"goto {start}")
        self.emit(f"{end}:")
        return None

    # If / If-Else
    #condiciona o if else em tac
    def visitCondicional(self, ctx):
        cond_place, _ = self._gen_expr(ctx.expressao())

        else_label = self.new_label()
        end_label = self.new_label()

        self.emit(f"if {cond_place} == 0 goto {else_label}")
        self.visit(ctx.bloco(0))
        self.emit(f"goto {end_label}")

        if len(ctx.bloco()) > 1:
            self.emit(f"{else_label}:")
            self.visit(ctx.bloco(1))
            self.emit(f"{end_label}:")
        else:
            self.emit(f"{else_label}:")
        return None

    # Expressões
    def visitExpressao(self, ctx):
        place, _ = self._gen_expr(ctx)
        return place

    def visitAtomo(self, ctx):
        if ctx.NUMERO():
            return ctx.NUMERO().getText()
        if ctx.REAL():
            return ctx.REAL().getText()
        if ctx.STRING():
            return ctx.STRING().getText()
        if ctx.ID():
            return ctx.ID().getText()
        if ctx.expressao():
            return self._gen_expr(ctx.expressao())[0]
        return None

    # Gerador interno de expressões
    def _gen_expr(self, ctx):

        if ctx is None:
            return ("0", "int")

        #retorna int
        if hasattr(ctx, "NUMERO") and ctx.NUMERO():
            return (ctx.NUMERO().getText(), "int")
        
        #retorna float
        if hasattr(ctx, "REAL") and ctx.REAL():
            return (ctx.REAL().getText(), "float")
        
        #retorna string
        if hasattr(ctx, "STRING") and ctx.STRING():
            return (ctx.STRING().getText(), "string")
        
        #retorna id (variavel)
        if hasattr(ctx, "ID") and ctx.ID() and ctx.getChildCount() == 1:
            return (ctx.ID().getText(), "var")

        #aso o nó só tenha um galho ele avança
        if ctx.getChildCount() == 1:
            child = ctx.getChild(0)
            return self._gen_expr(child)

        # operações anárias (sinal de um valor)
        if ctx.getChildCount() == 2:
            op = ctx.getChild(0).getText()
            right = ctx.getChild(1)
            r_place, r_type = self._gen_expr(right)
            t = self.new_temp()
            if op == "-":
                self.emit(f"{t} = 0 - {r_place}")
            else:
                self.emit(f"{t} = {r_place}")
            return (t, r_type)

        # operaçãoes binarias (com dois valores)
        if ctx.getChildCount() == 3:
            left = ctx.getChild(0)
            op = ctx.getChild(1).getText()
            right = ctx.getChild(2)

            l_place, l_type = self._gen_expr(left)
            r_place, r_type = self._gen_expr(right)

            t = self.new_temp()
            self.emit(f"{t} = {l_place} {op} {r_place}")

            if l_type == "float" or r_type == "float":
                res_type = "float"
            else:
                res_type = "int"

            return (t, res_type)
        
        #se tudo falhar em tudo retorna erro
        return (ctx.getText(), "desconhecido")
