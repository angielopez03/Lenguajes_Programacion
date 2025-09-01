grammar LabeledExpr;

prog:   stat+ ;

stat:   expr NEWLINE                # printExpr
    |   ID '=' expr NEWLINE         # assign
    |   NEWLINE                     # blank
    ;

expr:   expr op=('*'|'/') expr      # MulDiv
    |   expr op=('+'|'-') expr      # AddSub
    |   expr '!'                    # Factorial
    |   func=FUNC '(' expr ')'      # FuncCall
    |   INT                         # Int
    |   ID                          # Id
    |   '(' expr ')'                # Parens
    ;

FUNC:   'sin' | 'cos' | 'tan' | 'sqrt' | 'ln' | 'log' ;

MUL :   '*' ;
DIV :   '/' ;
ADD :   '+' ;
SUB :   '-' ;
ID  :   [a-zA-Z]+ ;
INT :   [0-9]+ ;
NEWLINE:'\r'? '\n' ;
WS  :   [ \t]+ -> skip ;

