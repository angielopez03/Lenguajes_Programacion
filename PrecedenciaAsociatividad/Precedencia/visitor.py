import math
from exprVisitor import exprVisitor
from exprParser import exprParser


class visitor(exprVisitor):
    def __init__(self):
        self.memory = {}

    # ID '=' expr
    def visitAssign(self, ctx:exprParser.AssignContext):
        id_ = ctx.ID().getText()
        value = self.visit(ctx.expr())
        self.memory[id_] = value
        return value

    # expr NEWLIpython3 Calc.py t.exprNE
    def visitPrintExpr(self, ctx:exprParser.PrintExprContext):
        value = self.visit(ctx.expr())
        print(value)
        return 0.0

    # INT
    def visitInt(self, ctx:exprParser.IntContext):
        return float(ctx.INT().getText())

    # ID
    def visitId(self, ctx:exprParser.IdContext):
        id_ = ctx.ID().getText()
        return self.memory.get(id_, 0.0)

    # expr op=('*'|'/') expr
    def visitMulDiv(self, ctx:exprParser.MulDivContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if ctx.op.type == exprParser.MUL:
            return left * right
        return left / right

    # expr op=('+'|'-') expr
    def visitAddSub(self, ctx:exprParser.AddSubContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if ctx.op.type == exprParser.ADD:
            return left + right
        return left - right

    # (expr)
    def visitParens(self, ctx:exprParser.ParensContext):
        return self.visit(ctx.expr())
