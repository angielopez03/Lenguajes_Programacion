grammar matrices;

programa: sentencia+ EOF;

sentencia: identificador '=' expresion ';';

expresion
    : matriz                                   #ExpresionMatriz
    | expresion '·' expresion                  #ExpresionProducto
    | expresion '.punto' '(' expresion ')'     #ExpresionProductoFuncion
    | '(' expresion ')'                        #ExpresionParentesis
    ;

matriz: '[' filas ']';

filas: fila (';' fila)*;

fila: '[' numero (',' numero)* ']';

numero: NUMERO;

identificador: IDENTIFICADOR;

IDENTIFICADOR: LETRA (LETRA | DIGITO | '_')*;

NUMERO: '-'? DIGITO+ ('.' DIGITO+)?;

fragment LETRA: [a-zA-Z];
fragment DIGITO: [0-9];

WS: [ \t\r\n]+ -> skip;

COMENTARIO_LINEA: '//' ~[\r\n]* -> skip;
COMENTARIO_BLOQUE: '/*' .*? '*/' -> skip;
