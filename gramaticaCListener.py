# Generated from gramaticaC.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .gramaticaCParser import gramaticaCParser
else:
    from gramaticaCParser import gramaticaCParser

# This class defines a complete listener for a parse tree produced by gramaticaCParser.
class gramaticaCListener(ParseTreeListener):

    # Enter a parse tree produced by gramaticaCParser#programa.
    def enterPrograma(self, ctx:gramaticaCParser.ProgramaContext):
        pass

    # Exit a parse tree produced by gramaticaCParser#programa.
    def exitPrograma(self, ctx:gramaticaCParser.ProgramaContext):
        pass


    # Enter a parse tree produced by gramaticaCParser#biblioteca.
    def enterBiblioteca(self, ctx:gramaticaCParser.BibliotecaContext):
        pass

    # Exit a parse tree produced by gramaticaCParser#biblioteca.
    def exitBiblioteca(self, ctx:gramaticaCParser.BibliotecaContext):
        pass


    # Enter a parse tree produced by gramaticaCParser#bloco.
    def enterBloco(self, ctx:gramaticaCParser.BlocoContext):
        pass

    # Exit a parse tree produced by gramaticaCParser#bloco.
    def exitBloco(self, ctx:gramaticaCParser.BlocoContext):
        pass


    # Enter a parse tree produced by gramaticaCParser#declaracao.
    def enterDeclaracao(self, ctx:gramaticaCParser.DeclaracaoContext):
        pass

    # Exit a parse tree produced by gramaticaCParser#declaracao.
    def exitDeclaracao(self, ctx:gramaticaCParser.DeclaracaoContext):
        pass


    # Enter a parse tree produced by gramaticaCParser#tipo.
    def enterTipo(self, ctx:gramaticaCParser.TipoContext):
        pass

    # Exit a parse tree produced by gramaticaCParser#tipo.
    def exitTipo(self, ctx:gramaticaCParser.TipoContext):
        pass


    # Enter a parse tree produced by gramaticaCParser#lista_variaveis.
    def enterLista_variaveis(self, ctx:gramaticaCParser.Lista_variaveisContext):
        pass

    # Exit a parse tree produced by gramaticaCParser#lista_variaveis.
    def exitLista_variaveis(self, ctx:gramaticaCParser.Lista_variaveisContext):
        pass


    # Enter a parse tree produced by gramaticaCParser#var_decl_item.
    def enterVar_decl_item(self, ctx:gramaticaCParser.Var_decl_itemContext):
        pass

    # Exit a parse tree produced by gramaticaCParser#var_decl_item.
    def exitVar_decl_item(self, ctx:gramaticaCParser.Var_decl_itemContext):
        pass


    # Enter a parse tree produced by gramaticaCParser#comando.
    def enterComando(self, ctx:gramaticaCParser.ComandoContext):
        pass

    # Exit a parse tree produced by gramaticaCParser#comando.
    def exitComando(self, ctx:gramaticaCParser.ComandoContext):
        pass


    # Enter a parse tree produced by gramaticaCParser#escrita.
    def enterEscrita(self, ctx:gramaticaCParser.EscritaContext):
        pass

    # Exit a parse tree produced by gramaticaCParser#escrita.
    def exitEscrita(self, ctx:gramaticaCParser.EscritaContext):
        pass


    # Enter a parse tree produced by gramaticaCParser#leitura.
    def enterLeitura(self, ctx:gramaticaCParser.LeituraContext):
        pass

    # Exit a parse tree produced by gramaticaCParser#leitura.
    def exitLeitura(self, ctx:gramaticaCParser.LeituraContext):
        pass


    # Enter a parse tree produced by gramaticaCParser#lista_identificador.
    def enterLista_identificador(self, ctx:gramaticaCParser.Lista_identificadorContext):
        pass

    # Exit a parse tree produced by gramaticaCParser#lista_identificador.
    def exitLista_identificador(self, ctx:gramaticaCParser.Lista_identificadorContext):
        pass


    # Enter a parse tree produced by gramaticaCParser#identificador.
    def enterIdentificador(self, ctx:gramaticaCParser.IdentificadorContext):
        pass

    # Exit a parse tree produced by gramaticaCParser#identificador.
    def exitIdentificador(self, ctx:gramaticaCParser.IdentificadorContext):
        pass


    # Enter a parse tree produced by gramaticaCParser#atribuicao.
    def enterAtribuicao(self, ctx:gramaticaCParser.AtribuicaoContext):
        pass

    # Exit a parse tree produced by gramaticaCParser#atribuicao.
    def exitAtribuicao(self, ctx:gramaticaCParser.AtribuicaoContext):
        pass


    # Enter a parse tree produced by gramaticaCParser#enquanto.
    def enterEnquanto(self, ctx:gramaticaCParser.EnquantoContext):
        pass

    # Exit a parse tree produced by gramaticaCParser#enquanto.
    def exitEnquanto(self, ctx:gramaticaCParser.EnquantoContext):
        pass


    # Enter a parse tree produced by gramaticaCParser#repita.
    def enterRepita(self, ctx:gramaticaCParser.RepitaContext):
        pass

    # Exit a parse tree produced by gramaticaCParser#repita.
    def exitRepita(self, ctx:gramaticaCParser.RepitaContext):
        pass


    # Enter a parse tree produced by gramaticaCParser#laco_para.
    def enterLaco_para(self, ctx:gramaticaCParser.Laco_paraContext):
        pass

    # Exit a parse tree produced by gramaticaCParser#laco_para.
    def exitLaco_para(self, ctx:gramaticaCParser.Laco_paraContext):
        pass


    # Enter a parse tree produced by gramaticaCParser#incremento.
    def enterIncremento(self, ctx:gramaticaCParser.IncrementoContext):
        pass

    # Exit a parse tree produced by gramaticaCParser#incremento.
    def exitIncremento(self, ctx:gramaticaCParser.IncrementoContext):
        pass


    # Enter a parse tree produced by gramaticaCParser#loop_infinito.
    def enterLoop_infinito(self, ctx:gramaticaCParser.Loop_infinitoContext):
        pass

    # Exit a parse tree produced by gramaticaCParser#loop_infinito.
    def exitLoop_infinito(self, ctx:gramaticaCParser.Loop_infinitoContext):
        pass


    # Enter a parse tree produced by gramaticaCParser#expressao.
    def enterExpressao(self, ctx:gramaticaCParser.ExpressaoContext):
        pass

    # Exit a parse tree produced by gramaticaCParser#expressao.
    def exitExpressao(self, ctx:gramaticaCParser.ExpressaoContext):
        pass


    # Enter a parse tree produced by gramaticaCParser#expr_bool.
    def enterExpr_bool(self, ctx:gramaticaCParser.Expr_boolContext):
        pass

    # Exit a parse tree produced by gramaticaCParser#expr_bool.
    def exitExpr_bool(self, ctx:gramaticaCParser.Expr_boolContext):
        pass


    # Enter a parse tree produced by gramaticaCParser#expr_relacao.
    def enterExpr_relacao(self, ctx:gramaticaCParser.Expr_relacaoContext):
        pass

    # Exit a parse tree produced by gramaticaCParser#expr_relacao.
    def exitExpr_relacao(self, ctx:gramaticaCParser.Expr_relacaoContext):
        pass


    # Enter a parse tree produced by gramaticaCParser#expr_comparacao.
    def enterExpr_comparacao(self, ctx:gramaticaCParser.Expr_comparacaoContext):
        pass

    # Exit a parse tree produced by gramaticaCParser#expr_comparacao.
    def exitExpr_comparacao(self, ctx:gramaticaCParser.Expr_comparacaoContext):
        pass


    # Enter a parse tree produced by gramaticaCParser#termo.
    def enterTermo(self, ctx:gramaticaCParser.TermoContext):
        pass

    # Exit a parse tree produced by gramaticaCParser#termo.
    def exitTermo(self, ctx:gramaticaCParser.TermoContext):
        pass


    # Enter a parse tree produced by gramaticaCParser#fator.
    def enterFator(self, ctx:gramaticaCParser.FatorContext):
        pass

    # Exit a parse tree produced by gramaticaCParser#fator.
    def exitFator(self, ctx:gramaticaCParser.FatorContext):
        pass


    # Enter a parse tree produced by gramaticaCParser#primary.
    def enterPrimary(self, ctx:gramaticaCParser.PrimaryContext):
        pass

    # Exit a parse tree produced by gramaticaCParser#primary.
    def exitPrimary(self, ctx:gramaticaCParser.PrimaryContext):
        pass



del gramaticaCParser