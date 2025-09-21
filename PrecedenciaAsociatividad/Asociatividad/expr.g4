grammar expr;

prog:   stat+ ;

stat:   expr NEWLINE                # printExpr
    |   ID '=' expr NEWLINE         # assign
    |   NEWLINE                     # blank
    ;
    
expr
    : term (ADD term)*              # AddLeft
    | term SUB expr                 # SubRight
    | term                          # ToTerm
    ;

term
    : factor (MUL factor)*          # MulLeft
    | factor DIV term               # DivRight
    | factor                        # ToFactor
    ;

factor
    : INT                           # Int
    | ID                            # Id
    | '(' expr ')'                  # Parens
    ;

MUL : '*' ;
DIV : '/' ;
ADD : '+' ;
SUB : '-' ;
ID  : [a-zA-Z]+ ;
INT : [0-9]+ ;
NEWLINE : [\r\n]+ ;
WS : [ \t]+ -> skip ;

