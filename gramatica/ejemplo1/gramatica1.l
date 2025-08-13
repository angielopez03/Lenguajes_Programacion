%{
#include "gramatica1.tab.h"
%}

%%
0        { return ZERO; }
1        { return ONE; }
\n       { return NEWLINE; }
[ \t]+   { /* ignorar espacios */ }
.        { return ERROR_CHAR; }
%%
