grammar matrices;

// =====================
//     PARSER
// =====================

programa: sentencia+ EOF;

sentencia: identificador '=' expresion ';';

expresion
    : matriz
    | '(' expresion ')'
    | expresion PUNTO_OP expresion
    | expresion PUNTO_FUNC '(' expresion ')'
    | identificador
    ;

matriz: '[' filas ']';
filas: fila (SEP fila)*;
fila: '[' numero (SEP numero)* ']';
numero: NUMERO;
identificador: IDENTIFICADOR;

// =====================
//       LEXER
// =====================

// Números
NUMERO: '-'? DIGITO+ ('.' DIGITO+)?;
IDENTIFICADOR: [a-zA-Z_] [a-zA-Z0-9_]*;

// Operadores
PUNTO_OP: '·';
PUNTO_FUNC: '.punto';

// Comentarios y espacios
COMENTARIO: '//' ~[\r\n]* -> skip;
ESPACIO: [ \t\r\n]+ -> skip;

// Permitir saltos de línea o espacios entre elementos
SEP: (','? ESPACIO*);

// Fragmentos
fragment DIGITO: [0-9];

