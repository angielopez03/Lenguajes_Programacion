# Generated from expr.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .exprParser import exprParser
else:
    from exprParser import exprParser

# This class defines a complete generic visitor for a parse tree produced by exprParser.

class exprVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by exprParser#prog.
    def visitProg(self, ctx:exprParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprParser#printExpr.
    def visitPrintExpr(self, ctx:exprParser.PrintExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprParser#assign.
    def visitAssign(self, ctx:exprParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprParser#blank.
    def visitBlank(self, ctx:exprParser.BlankContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprParser#AddSub.
    def visitAddSub(self, ctx:exprParser.AddSubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprParser#MulDiv.
    def visitMulDiv(self, ctx:exprParser.MulDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprParser#Parens.
    def visitParens(self, ctx:exprParser.ParensContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprParser#Id.
    def visitId(self, ctx:exprParser.IdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprParser#Int.
    def visitInt(self, ctx:exprParser.IntContext):
        return self.visitChildren(ctx)



del exprParser