import sys
from antlr4 import *
from LabeledExprLexer import LabeledExprLexer
from LabeledExprParser import LabeledExprParser
from EvalVisitor import EvalVisitor


def main(argv):
    input_stream = FileStream(argv[1]) if len(argv) > 1 else InputStream(sys.stdin.read())
    lexer = LabeledExprLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = LabeledExprParser(stream)
    tree = parser.prog()

    eval = EvalVisitor()
    eval.visit(tree)


if __name__ == '__main__':
    main(sys.argv)

