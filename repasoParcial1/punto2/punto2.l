%{
#include <stdio.h>
%}

ID      [a-zA-Z_][a-zA-Z0-9_]*
NUM     [0-9]+
ESP     [ \t]*

%%

{ESP}{ID}{ESP}={ESP}lambda{ESP}{ID}{ESP}:{ESP}{ID}{ESP}\*\*{ESP}{NUM}{ESP}\n {
    printf("ACEPTA\n");
}

{ESP}\n {
    /* Línea vacía - no imprime nada */
}

.*\n {
    printf("NO ACEPTA\n");
}

%%

int main(int argc, char *argv[]) {
    if (argc > 1) {
        FILE *archivo = fopen(argv[1], "r");
        if (!archivo) {
            perror("No se pudo abrir el archivo");
            return 1;
        }
        yyin = archivo;
        yylex();
        fclose(archivo);
    } else {
        yylex();
    }
    
    return 0;
}
