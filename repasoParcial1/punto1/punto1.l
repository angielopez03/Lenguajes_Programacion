%{
#include <stdio.h>
%}

/* Definición de patrones */
DIGITO   [0-9]
ENTERO   {DIGITO}+
REAL     {DIGITO}+"."{DIGITO}+

%%

"++"        { printf("INCR\t%s\n", yytext); }
"+"         { printf("SUMA\t%s\n", yytext); }
{REAL}      { printf("REAL\t%s\n", yytext); }
{ENTERO}    { printf("ENTERO\t%s\n", yytext); }
[ \t\n]+    { /* ignorar espacios, tabs y saltos de línea */ }
.+           { printf("ERROR\t%s\n", yytext); }

%%

int main(int argc, char *argv[]) {
    if (argc > 1) {
        FILE *archivo = fopen(argv[1], "r");
        if (!archivo) {
            perror("No se pudo abrir el archivo");
            return 1;
        }
        yyin = archivo;
    }
    yylex(); // ejecuta el analizador léxico
    return 0;
}

