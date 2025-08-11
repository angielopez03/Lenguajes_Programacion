/* Calculator with bitwise operators */
%{
#include <stdio.h>
#include <stdlib.h>

/* Declaraciones de funciones */
int yylex(void);
int yyerror(char *s);
%}

/* Declaraciones de tokens */
%token NUMBER
%token ADD SUB MUL DIV 
%token AND OR_ABS
%token EOL

/* Precedencia de operadores */
%left OR_ABS         /* OR tiene menor precedencia */
%left AND            /* AND tiene mayor precedencia que OR */
%left ADD SUB        /* Suma y resta */
%left MUL DIV        /* Multiplicación y división */
%right UMINUS        /* Menos unario y valor absoluto */

%%
calclist: /* nothing */
        | calclist exp EOL { 
            printf("= %d (decimal) = 0x%x (hex) = 0b", $2, $2);
            /* Mostrar en binario */
            int num = $2;
            for(int i = 31; i >= 0; i--) {
                if((num >> i) & 1) printf("1");
                else printf("0");
                if(i % 4 == 0 && i != 0) printf("_");
            }
            printf("\n\n");
        }
        ;

exp: factor
   | exp ADD factor    { $$ = $1 + $3; }
   | exp SUB factor    { $$ = $1 - $3; }
   | exp OR_ABS factor { $$ = $1 | $3; }
   | exp AND factor    { $$ = $1 & $3; }
   ;

factor: term
      | factor MUL term { $$ = $1 * $3; }
      | factor DIV term { 
          if($3 == 0) {
              yyerror("División por cero");
              $$ = 0;
          } else {
              $$ = $1 / $3; 
          }
      }
      ;

term: NUMBER
    | OR_ABS exp OR_ABS        { $$ = $2 >= 0? $2 : -$2; }
    | SUB term %prec UMINUS    { $$ = -$2; }
    | '(' exp ')'              { $$ = $2; }
    ;
%%

int main(int argc, char **argv)
{
    printf("=== Calculadora con Operadores Bitwise ===\n");
    printf("Operadores soportados:\n");
    printf("  +, -, *, /     : Aritméticos\n");
    printf("  &              : AND bitwise\n");
    printf("  |              : OR bitwise (entre números)\n");
    printf("  |n|            : Valor absoluto (unario)\n");
    printf("\nIngrese expresiones:\n\n");
    
    yyparse();
    return 0;
}

int yyerror(char *s)
{
    fprintf(stderr, "Error: %s\n", s);
    return 0;
}
