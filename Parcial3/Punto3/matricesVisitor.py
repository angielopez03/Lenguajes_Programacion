# Generated from matrices.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .matricesParser import matricesParser
else:
    from matricesParser import matricesParser

# This class defines a complete generic visitor for a parse tree produced by matricesParser.

class matricesVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by matricesParser#programa.
    def visitPrograma(self, ctx:matricesParser.ProgramaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by matricesParser#sentencia.
    def visitSentencia(self, ctx:matricesParser.SentenciaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by matricesParser#expresion.
    def visitExpresion(self, ctx:matricesParser.ExpresionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by matricesParser#matriz.
    def visitMatriz(self, ctx:matricesParser.MatrizContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by matricesParser#filas.
    def visitFilas(self, ctx:matricesParser.FilasContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by matricesParser#fila.
    def visitFila(self, ctx:matricesParser.FilaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by matricesParser#numero.
    def visitNumero(self, ctx:matricesParser.NumeroContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by matricesParser#identificador.
    def visitIdentificador(self, ctx:matricesParser.IdentificadorContext):
        return self.visitChildren(ctx)



del matricesParser