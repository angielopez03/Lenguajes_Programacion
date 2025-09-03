%{
#include "punto3.tab.h"
#include <stdlib.h>
%}

%%
"+"         { return ADD; }
"-"         { return SUB; }
"*"         { return MUL; }
"/"         { return DIV; }
"|"         { return ABS; }
"sqrt"      { return SQRT; }
[0-9]+\.[0-9]+ { yylval.dval = atof(yytext); return NUMBER; }
[0-9]+      { yylval.dval = atof(yytext); return NUMBER; }
\n          { return EOL; }
[ \t]       { /* ignore whitespace */ }
"("         { return LPAREN; }
")"         { return RPAREN; }
.           { printf("Mystery character %c\n", *yytext); }
%%

int yywrap(void) {
    return 1;
}
