import math
from LabeledExprVisitor import LabeledExprVisitor
from LabeledExprParser import LabeledExprParser


class EvalVisitor(LabeledExprVisitor):
    def __init__(self):
        self.memory = {}
        self.useDegrees = True  # True = trabajar en grados, False = radianes

    # ID '=' expr
    def visitAssign(self, ctx:LabeledExprParser.AssignContext):
        id_ = ctx.ID().getText()
        value = self.visit(ctx.expr())
        self.memory[id_] = value
        return value

    # expr NEWLINE
    def visitPrintExpr(self, ctx:LabeledExprParser.PrintExprContext):
        value = self.visit(ctx.expr())
        print(value)
        return 0.0

    # INT
    def visitInt(self, ctx:LabeledExprParser.IntContext):
        return float(ctx.INT().getText())

    # ID
    def visitId(self, ctx:LabeledExprParser.IdContext):
        id_ = ctx.ID().getText()
        return self.memory.get(id_, 0.0)

    # expr op=('*'|'/') expr
    def visitMulDiv(self, ctx:LabeledExprParser.MulDivContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if ctx.op.type == LabeledExprParser.MUL:
            return left * right
        return left / right

    # expr op=('+'|'-') expr
    def visitAddSub(self, ctx:LabeledExprParser.AddSubContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if ctx.op.type == LabeledExprParser.ADD:
            return left + right
        return left - right

    # (expr)
    def visitParens(self, ctx:LabeledExprParser.ParensContext):
        return self.visit(ctx.expr())

    # factorial
    def visitFactorial(self, ctx:LabeledExprParser.FactorialContext):
        value = int(self.visit(ctx.expr()))
        return float(self.factorial(value))

    def factorial(self, n):
        if n < 0:
            raise RuntimeError("Factorial no definido para negativos")
        result = 1
        for i in range(2, n+1):
            result *= i
        return result

    # funciones matemáticas
    def visitFuncCall(self, ctx:LabeledExprParser.FuncCallContext):
        func = ctx.func.text
        value = self.visit(ctx.expr())

        if self.useDegrees and func in ("sin", "cos", "tan"):
            value = math.radians(value)

        if func == "sin": return math.sin(value)
        if func == "cos": return math.cos(value)
        if func == "tan": return math.tan(value)
        if func == "sqrt": return math.sqrt(value)
        if func == "ln": return math.log(value)
        if func == "log": return math.log10(value)
        raise RuntimeError(f"Función desconocida: {func}")

