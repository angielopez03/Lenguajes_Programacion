import sys
from antlr4 import *
from exprLexer import exprLexer
from exprParser import exprParser
from visitor import visitor

def main(argv):
    input_stream = FileStream(argv[1]) if len(argv) > 1 else InputStream(sys.stdin.read())
    lexer = exprLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = exprParser(stream)
    tree = parser.prog()
    eval = visitor()
    eval.visit(tree)


if __name__ == '__main__':
    main(sys.argv)

