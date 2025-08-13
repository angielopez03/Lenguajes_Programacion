%{
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

extern FILE *yyin;
int yylex(void);
int yyerror(char *s);

char number_str[1000];
int pos = 0;

int is_odd_palindrome(char *str) {
    int len = strlen(str);
    
    if (len % 2 == 0) {
        return 0;
    }
    
    for (int i = 0; i < len/2; i++) {
        if (str[i] != str[len-1-i]) {
            return 0;
        }
    }
    return 1;
}

int has_txt_extension(const char *filename) {
    const char *dot = strrchr(filename, '.');
    if (!dot || dot == filename) return 0;
    return strcmp(dot, ".txt") == 0;
}
%}

%token ZERO ONE NEWLINE ERROR_CHAR

%%
program: /* vacío */
       | program line
       ;

line: number NEWLINE { 
        number_str[pos] = '\0';  /* Terminar string */
        if (is_odd_palindrome(number_str)) {
            printf("ACEPTA\n");
        } else {
            printf("NO ACEPTA\n");
        }
        pos = 0;  /* Reiniciar para próximo número */
    }
    | NEWLINE { 
        /* línea vacía */ 
        pos = 0;
    }
    | error NEWLINE { 
        printf("NO ACEPTA\n"); 
        pos = 0;
        yyerrok; 
    }
    ;

number: digit
      | number digit
      ;

digit: ZERO { number_str[pos++] = '0'; }
     | ONE  { number_str[pos++] = '1'; }
     ;

%%

int main(int argc, char **argv) {
    FILE *input;
    
    if (argc != 2) {
        fprintf(stderr, "Error: Debe proporcionar exactamente un archivo como argumento.\n");
        fprintf(stderr, "Uso: %s <archivo.txt>\n", argv[0]);
        return 1;
    }
    
    if (!has_txt_extension(argv[1])) {
        fprintf(stderr, "Error: El archivo debe tener extensión .txt\n");
        fprintf(stderr, "Archivo proporcionado: %s\n", argv[1]);
        return 1;
    }
    
    input = fopen(argv[1], "r");
    if (!input) {
        fprintf(stderr, "Error: No se puede abrir el archivo %s\n", argv[1]);
        fprintf(stderr, "Verifique que el archivo exista y tenga permisos de lectura.\n");
        return 1;
    }
    
    yyin = input;
    
    // Procesar el archivo
    yyparse();
    
    fclose(input);
    
    return 0;
}

int yyerror(char *s) {
    return 0;
}
