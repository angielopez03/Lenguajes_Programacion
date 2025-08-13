%{
#include <stdio.h>
#include <stdlib.h>

int yylex();
void yyerror(const char *s);
int acepta = 0;
extern FILE *yyin;  // Variable para archivo de entrada
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
    /* épsilon (cadena vacía) */ {
        /* A_nt → ε */
    }
    | LETRA_A A_nt LETRA_B {
        /* A_nt → aA_ntb */
    }
    ;

%%

void yyerror(const char *s) {
    /* No imprimir errores, solo marcar como no aceptado */
    acepta = 0;
}

int main(int argc, char *argv[]) {
    FILE *archivo;
    
    // Verificar que se proporcione exactamente un argumento (el archivo)
    if (argc != 2) {
        printf("Uso: %s archivo.txt\n", argv[0]);
        printf("Ejemplo: %s cadenas.txt\n", argv[0]);
        return 1;
    }
    
    // Intentar abrir el archivo
    archivo = fopen(argv[1], "r");
    if (!archivo) {
        printf("Error: No se pudo abrir el archivo '%s'\n", argv[1]);
        return 1;
    }
    
    // Redirigir la entrada estándar al archivo
    yyin = archivo;
    
    // Procesar el archivo
    int resultado = yyparse();
    
    // Cerrar el archivo
    fclose(archivo);
    
    return resultado;
}
