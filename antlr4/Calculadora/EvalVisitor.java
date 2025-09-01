import java.util.HashMap;
import java.util.Map;

public class EvalVisitor extends LabeledExprBaseVisitor<Double> {
    Map<String, Double> memory = new HashMap<>();
    /** true = trabajar en grados, false = radianes */
    boolean useDegrees = true;

    /** ID '=' expr NEWLINE */
    @Override
    public Double visitAssign(LabeledExprParser.AssignContext ctx) {
        String id = ctx.ID().getText();
        Double value = visit(ctx.expr());
        memory.put(id, value);
        return value;
    }

    /** expr NEWLINE */
    @Override
    public Double visitPrintExpr(LabeledExprParser.PrintExprContext ctx) {
        Double value = visit(ctx.expr());
        System.out.println(value);
        return 0.0;
    }

    /** INT */
    @Override
    public Double visitInt(LabeledExprParser.IntContext ctx) {
        return Double.valueOf(ctx.INT().getText());
    }

    /** ID */
    @Override
    public Double visitId(LabeledExprParser.IdContext ctx) {
        String id = ctx.ID().getText();
        if (memory.containsKey(id)) return memory.get(id);
        return 0.0;
    }

    /** expr op=('*'|'/') expr */
    @Override
    public Double visitMulDiv(LabeledExprParser.MulDivContext ctx) {
        double left = visit(ctx.expr(0));
        double right = visit(ctx.expr(1));
        if (ctx.op.getType() == LabeledExprParser.MUL) return left * right;
        return left / right;
    }

    /** expr op=('+'|'-') expr */
    @Override
    public Double visitAddSub(LabeledExprParser.AddSubContext ctx) {
        double left = visit(ctx.expr(0));
        double right = visit(ctx.expr(1));
        if (ctx.op.getType() == LabeledExprParser.ADD) return left + right;
        return left - right;
    }

    /** '(' expr ')' */
    @Override
    public Double visitParens(LabeledExprParser.ParensContext ctx) {
        return visit(ctx.expr());
    }

    /** Factorial */
    @Override
    public Double visitFactorial(LabeledExprParser.FactorialContext ctx) {
        int value = visit(ctx.expr()).intValue();
        return (double) factorial(value);
    }

    private int factorial(int n) {
        if (n < 0) throw new RuntimeException("Factorial no definido para negativos");
        int result = 1;
        for (int i = 2; i <= n; i++) result *= i;
        return result;
    }

    /** Funciones matemáticas*/
    @Override
    public Double visitFuncCall(LabeledExprParser.FuncCallContext ctx) {
        String func = ctx.func.getText();
        double value = visit(ctx.expr());

        if (useDegrees && (func.equals("sin") || func.equals("cos") || func.equals("tan"))) {
            value = Math.toRadians(value);
        }

        switch (func) {
            case "sin": return Math.sin(value);
            case "cos": return Math.cos(value);
            case "tan": return Math.tan(value);
            case "sqrt": return Math.sqrt(value);
            case "ln": return Math.log(value);
            case "log": return Math.log10(value);
            default: throw new RuntimeException("Función desconocida: " + func);
        }
    }
}

