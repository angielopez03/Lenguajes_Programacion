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

    # expr NEWLINE
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

    # expr : term (ADD term)*     # AddLeft    (uno o varios term())
    def visitAddLeft(self, ctx:exprParser.AddLeftContext):
        # ctx.term() devuelve una lista de term()
        terms = ctx.term()
        value = self.visit(terms[0])
        for i in range(1, len(terms)):
            value += self.visit(terms[i])
        return value

    # expr : term SUB expr       # SubRight   (term y expr)
    def visitSubRight(self, ctx:exprParser.SubRightContext):
        left = self.visit(ctx.term())
        right = self.visit(ctx.expr())
        return left - right

    # term : factor (MUL factor)*  # MulLeft   (uno o varios factor())
    def visitMulLeft(self, ctx:exprParser.MulLeftContext):
        factors = ctx.factor()
        value = self.visit(factors[0])
        for i in range(1, len(factors)):
            value *= self.visit(factors[i])
        return value

    # term : factor DIV term      # DivRight  (factor y term)
    def visitDivRight(self, ctx:exprParser.DivRightContext):
        left = self.visit(ctx.factor())
        right = self.visit(ctx.term())
        return left / right

    # expr : term                 # ToTerm
    def visitToTerm(self, ctx:exprParser.ToTermContext):
        return self.visit(ctx.term())

    # term : factor               # ToFactor
    def visitToFactor(self, ctx:exprParser.ToFactorContext):
        return self.visit(ctx.factor())

    # (expr)
    def visitParens(self, ctx:exprParser.ParensContext):
        return self.visit(ctx.expr())

