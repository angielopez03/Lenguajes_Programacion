%{
#include <stdio.h>
#include <stdlib.h>

int yylex();
void yyerror(const char *s);
int acepta = 0;
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
        if (acepta) {
            printf("ACEPTA\n");
        } else {
            printf("NO ACEPTA\n");
        }
        acepta = 0;
    }
    | NEWLINE {
        /* línea vacía, no hacer nada */
    }
    | error NEWLINE {
        printf("NO ACEPTA\n");
        acepta = 0;
        yyerrok;
    }
    ;

expresion:
    S {
        acepta = 1;
    }
    ;

S:
    A_nt LETRA_B
    ;

A_nt:
    LETRA_A LETRA_B {
        /* A_nt → ab (caso base) */
    }
    | LETRA_A A_nt LETRA_B {
        /* A_nt → aA_ntb (caso recursivo) */
    }
    ;

%%

void yyerror(const char *s) {
    acepta = 0;
}

int main(int argc, char *argv[]) {
    FILE *archivo;
    
    if (argc != 2) {
        printf("Uso: %s archivo.txt\n", argv[0]);
        return 1;
    }
    
    archivo = fopen(argv[1], "r");
    if (!archivo) {
        printf("Error: No se pudo abrir el archivo '%s'\n", argv[1]);
        return 1;
    }
    
    yyin = archivo;
    int resultado = yyparse();
    fclose(archivo);
    
    return resultado;
}
