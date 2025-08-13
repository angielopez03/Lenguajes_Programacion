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
        /* línea vacía */
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
    LETRA_A LETRA_B LETRA_B {
        /* Equivale a: S → Ab donde A → ab */
    }
    | LETRA_A LETRA_B {
        /* Equivale a: S → Ab donde A → a */
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
