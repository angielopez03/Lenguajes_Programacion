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


    # Enter a parse tree produced by matricesParser#ExpresionParentesis.
    def enterExpresionParentesis(self, ctx:matricesParser.ExpresionParentesisContext):
        pass

    # Exit a parse tree produced by matricesParser#ExpresionParentesis.
    def exitExpresionParentesis(self, ctx:matricesParser.ExpresionParentesisContext):
        pass


    # Enter a parse tree produced by matricesParser#ExpresionProductoFuncion.
    def enterExpresionProductoFuncion(self, ctx:matricesParser.ExpresionProductoFuncionContext):
        pass

    # Exit a parse tree produced by matricesParser#ExpresionProductoFuncion.
    def exitExpresionProductoFuncion(self, ctx:matricesParser.ExpresionProductoFuncionContext):
        pass


    # Enter a parse tree produced by matricesParser#ExpresionProducto.
    def enterExpresionProducto(self, ctx:matricesParser.ExpresionProductoContext):
        pass

    # Exit a parse tree produced by matricesParser#ExpresionProducto.
    def exitExpresionProducto(self, ctx:matricesParser.ExpresionProductoContext):
        pass


    # Enter a parse tree produced by matricesParser#ExpresionMatriz.
    def enterExpresionMatriz(self, ctx:matricesParser.ExpresionMatrizContext):
        pass

    # Exit a parse tree produced by matricesParser#ExpresionMatriz.
    def exitExpresionMatriz(self, ctx:matricesParser.ExpresionMatrizContext):
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