%{
#include <stdio.h>
#include <stdlib.h>

int yylex();
void yyerror(const char *s);
extern FILE *yyin;
%}

%token LETRA_A LETRA_B NEWLINE ERROR
%start programa

%%

programa:
    /* vacío */
    | programa linea
    ;

linea:
    expresion NEWLINE {
        printf("ACEPTA\n");
    }
    | NEWLINE {
        /* línea vacía*/
    }
    | error NEWLINE {
        printf("NO ACEPTA\n");
        yyerrok;
    }
    ;

expresion:
    S
    ;

S:
    A_produccion LETRA_B
    ;

A_produccion:
    LETRA_A {
    }
    | A_produccion LETRA_A LETRA_B {
    }
    ;

%%

void yyerror(const char *s) {
    /* No imprimir errores automáticamente */
}

int main(int argc, char *argv[]) {
    FILE *archivo;
    
    if (argc != 2) {
        fprintf(stderr, "Uso: %s archivo.txt\n", argv[0]);
        return 1;
    }
    
    archivo = fopen(argv[1], "r");
    if (!archivo) {
        fprintf(stderr, "Error: No se pudo abrir el archivo '%s'\n", argv[1]);
        return 1;
    }
    
    yyin = archivo;
    int resultado = yyparse();
    fclose(archivo);
    
    return resultado;
}
