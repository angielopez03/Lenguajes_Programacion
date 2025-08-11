%{
#include "calcHexa.tab.h"
#include <stdlib.h>
%}

%%
"+" { return ADD; }
"-" { return SUB; }
"*" { return MUL; }
"/" { return DIV; }
"&" { return AND; }
"|" { return OR_ABS; }
"(" { return '('; }
")" { return ')'; }

0[xX][0-9a-fA-F]+ { 
    yylval = (int)strtol(yytext, NULL, 16); 
    return NUMBER; 
}

[0-9]+ { 
    yylval = (int)strtol(yytext, NULL, 10); 
    return NUMBER; 
}

\n { return EOL; }
[ \t] { }
. { printf("Mystery character %c\n", *yytext); }
%%
