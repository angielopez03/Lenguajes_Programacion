# Generated from matrices.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .matricesParser import matricesParser
else:
    from matricesParser import matricesParser

# This class defines a complete listener for a parse tree produced by matricesParser.
class matricesListener(ParseTreeListener):

    # Enter a parse tree produced by matricesParser#programa.
    def enterPrograma(self, ctx:matricesParser.ProgramaContext):
        pass

    # Exit a parse tree produced by matricesParser#programa.
    def exitPrograma(self, ctx:matricesParser.ProgramaContext):
        pass


    # Enter a parse tree produced by matricesParser#sentencia.
    def enterSentencia(self, ctx:matricesParser.SentenciaContext):
        pass

    # Exit a parse tree produced by matricesParser#sentencia.
    def exitSentencia(self, ctx:matricesParser.SentenciaContext):
        pass


    # Enter a parse tree produced by matricesParser#expresion.
    def enterExpresion(self, ctx:matricesParser.ExpresionContext):
        pass

    # Exit a parse tree produced by matricesParser#expresion.
    def exitExpresion(self, ctx:matricesParser.ExpresionContext):
        pass


    # Enter a parse tree produced by matricesParser#matriz.
    def enterMatriz(self, ctx:matricesParser.MatrizContext):
        pass

    # Exit a parse tree produced by matricesParser#matriz.
    def exitMatriz(self, ctx:matricesParser.MatrizContext):
        pass


    # Enter a parse tree produced by matricesParser#filas.
    def enterFilas(self, ctx:matricesParser.FilasContext):
        pass

    # Exit a parse tree produced by matricesParser#filas.
    def exitFilas(self, ctx:matricesParser.FilasContext):
        pass


    # Enter a parse tree produced by matricesParser#fila.
    def enterFila(self, ctx:matricesParser.FilaContext):
        pass

    # Exit a parse tree produced by matricesParser#fila.
    def exitFila(self, ctx:matricesParser.FilaContext):
        pass


    # Enter a parse tree produced by matricesParser#numero.
    def enterNumero(self, ctx:matricesParser.NumeroContext):
        pass

    # Exit a parse tree produced by matricesParser#numero.
    def exitNumero(self, ctx:matricesParser.NumeroContext):
        pass


    # Enter a parse tree produced by matricesParser#identificador.
    def enterIdentificador(self, ctx:matricesParser.IdentificadorContext):
        pass

    # Exit a parse tree produced by matricesParser#identificador.
    def exitIdentificador(self, ctx:matricesParser.IdentificadorContext):
        pass



del matricesParser