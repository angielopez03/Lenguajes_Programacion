%{
#include "gramatica5.tab.h"
#include <stdio.h>
%}

%%

[a]     { return LETRA_A; }
[b]     { return LETRA_B; }
\n      { return NEWLINE; }
[ \t]   { /* ignorar espacios y tabulaciones */ }
.       { return ERROR; }

%%

int yywrap() {
    return 1;
}
