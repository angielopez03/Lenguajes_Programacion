%{
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

extern FILE *yyin;
int yylex(void);
int yyerror(char *s);
%}

%union {
    double dval;
}

%token <dval> NUMBER
%token ADD SUB MUL DIV ABS SQRT
%token EOL LPAREN RPAREN
%type <dval> exp factor term

%left ADD SUB
%left MUL DIV
%right UMINUS
%right SQRT ABS

%%

calclist: /* nothing */
        | calclist exp EOL { printf("= %.6f\n", $2); }
        | calclist EOL     { /* línea vacía */ }
        ;

exp: factor
   | exp ADD factor { $$ = $1 + $3; }
   | exp SUB factor { $$ = $1 - $3; }
   ;

factor: term
      | factor MUL term { $$ = $1 * $3; }
      | factor DIV term { 
          if ($3 == 0.0) {
              fprintf(stderr, "división por cero\n");
              $$ = 0.0;
          } else {
              $$ = $1 / $3;
          }
      }
      ;

term: NUMBER
    | ABS term { $$ = ($2 >= 0) ? $2 : -$2; }
    | SQRT term { 
        if ($2 < 0.0) {
            fprintf(stderr, "raíz de número negativo\n");
            $$ = 0.0;
        } else {
            $$ = sqrt($2);
        }
    }
    | SUB term %prec UMINUS { $$ = -$2; }
    | LPAREN exp RPAREN { $$ = $2; }
    ;

%%

int main(int argc, char **argv)
{
    if (argc > 1) {
        FILE *file = fopen(argv[1], "r");
        if (!file) {
            fprintf(stderr, "no se abre el archivo %s\n", argv[1]);
            return 1;
        }
        yyin = file;
    }
    
    yyparse();
    
    if (argc > 1) {
        fclose(yyin);
    }
    
    return 0;
}

int yyerror(char *s)
{
    fprintf(stderr, "Error: %s\n", s);
    return 0;
}
