# Ejecución de los ejercicios

### Ejercicio 1: Contador de palabras

<img width="584" height="115" alt="image" src="https://github.com/user-attachments/assets/47638622-df62-41ef-8b30-969d1fabcea7" />

### Ejercicio 2: Inglés a Americano

<img width="592" height="135" alt="image" src="https://github.com/user-attachments/assets/e915f631-5855-464a-97c6-554cb4e6c790" />

### Ejercicio 3: Escáner flex sencillo

<img width="591" height="316" alt="image" src="https://github.com/user-attachments/assets/6521b0bd-f001-47b3-91b9-e37bbab9a21c" />

### Ejercicio 4: Escáner de calculadora

<img width="592" height="204" alt="image" src="https://github.com/user-attachments/assets/47059465-84e5-4ee1-8b78-1f2416ce7e40" />

### Ejercicio 5: Calculadora simple

<img width="742" height="134" alt="image" src="https://github.com/user-attachments/assets/b24c8eaa-5669-4ab0-b3b7-e5756504ac7a" />

### Calculadora con hexadecimales

<img width="729" height="188" alt="image" src="https://github.com/user-attachments/assets/6c8add6d-be77-42d5-a888-3f7dceec960c" />

### Calculadora con hexadecimales y operadores

<img width="729" height="478" alt="image" src="https://github.com/user-attachments/assets/cdbf5824-ff19-484b-9af1-ebe52248cae2" />


---
# Preguntas de ejercicio

## 1. Manejo de comentarios

- Pregunta: ¿La calculadora aceptará una línea que contenga solo un comentario? ¿Por qué no? ¿Sería más fácil corregir esto en el escáner o analizador?

No, la calculadora no aceptará una línea que contenga solo un comentario.

```
%%
"+" { return ADD; }
"-" { return SUB; }
"*" { return MUL; }
"/" { return DIV; }
"|" { return ABS; }
[0-9]+ { yylval = atoi(yytext); return NUMBER; }
\n { return EOL; }
[ \t] { /* ignore whitespace */ }
. { printf("Mystery character %c\n", *yytext); }  // <- debido a esto
%%

```

Si se introduce un comentario como: /* esto es un comentario */
El scanner procesará:

/ → Regla . → Imprime "Mystery character /"

* → Regla . → Imprime "Mystery character *"

  → Regla [ \t] → Ignora espacio

e → Regla . → Imprime "Mystery character e"

s → Regla . → Imprime "Mystery character s"}

... y así con cada carácter

El resultado da error y mensajes de "Mystery character" para cada símbolo del comentario ya que no hay una regla que lo maneje.

**¿Dónde es más fácil corregirlo?**

En el escáner (Flex)

### 1. Nivel de Abstracción Apropiado

Los comentarios son elementos léxicos, no sintácticos:

Léxico: Patrones de caracteres (como palabras, números, símbolos)

Sintáctico: Estructura gramatical (como expresiones, declaraciones)

### 2. Eficiencia

```
"/*"([^*]|\*+[^*/])*\*+"/"  { /* ignorar comentarios */ }

```

El scanner puede descartar comentarios antes de enviar tokens al parser

El parser nunca ve los comentarios → más eficiente

Menos trabajo para el parser

### 3. Separación de Responsabilidades

Scanner: "¿Qué tipo de símbolos hay?" → Maneja comentarios

Parser: "¿Cómo se combinan estos símbolos?" → Maneja gramática

---

## 2. Conversión hexadecimal

- Pregunta: Convierta la calculadora en una calculadora hexadecimal que acepte números hexadecimales y decimales.

### Cambios principales:

Agregar #include <stdlib.h> para usar strtol

Nuevo patrón hexadecimal: 0[xX][0-9a-fA-F]+ que reconoce:

- 0x o 0X al inicio
- Seguido de dígitos hexadecimales (0-9, a-f, A-F)

Uso de strtol:

- Para hex: strtol(yytext, NULL, 16) convierte base 16
- Para decimal: strtol(yytext, NULL, 10) convierte base 10

Ambos devuelven NUMBER

**Implementación**

calcHexa.l

```
%{
#include "calcHexa.tab.h"
#include <stdlib.h>
%}

%%
"+" { return ADD; }
"-" { return SUB; }
"*" { return MUL; }
"/" { return DIV; }
"|" { return ABS; }

0[xX][0-9a-fA-F]+ { 
    yylval = (int)strtol(yytext, NULL, 16); 
    return NUMBER; 
}

[0-9]+ { 
    yylval = (int)strtol(yytext, NULL, 10); 
    return NUMBER; 
}

\n { return EOL; }
[ \t] { /* ignore whitespace */ }
. { printf("Mystery character %c\n", *yytext); }
%%

```

calcHexa.l

```
%{
#include <stdio.h>
#include <stdlib.h>

int yylex(void);
int yyerror(char *s);
%}

%token NUMBER
%token ADD SUB MUL DIV ABS
%token EOL

%%
calclist: /* nothing */
        | calclist exp EOL { 
            printf("= %d (decimal) = 0x%x (hex)\n", $2, $2); 
        }
        ;

exp: factor
   | exp ADD factor { $$ = $1 + $3; }
   | exp SUB factor { $$ = $1 - $3; }
   ;

factor: term
      | factor MUL term { $$ = $1 * $3; }
      | factor DIV term { $$ = $1 / $3; }
      ;

term: NUMBER
    | ABS term { $$ = $2 >= 0? $2 : - $2; }
    ;
%%

int main(int argc, char **argv)
{
    printf("Calculadora Hexadecimal\n");
    printf("Ingrese expresiones:\n\n");
    
    yyparse();
    return 0;
}

int yyerror(char *s)
{
    fprintf(stderr, "Error: %s\n", s);
    return 0;
}

```

**Ejecución**

<img width="729" height="188" alt="image" src="https://github.com/user-attachments/assets/3bc820ba-6498-4a81-a171-876e723a091b" />

---

## 3. Operadores de nivel de bits

- Pregunta: Agregue operadores de nivel de bits como AND y OR a la calculadora.

El símbolo | se usa para:

Valor absoluto unario: |5|, |-3|

OR bitwise binario: 5 | 3

Solución: Usar contexto para diferenciarlos

Si | aparece después de un número/expresión → OR binario

Si | aparece al inicio o después de un operador → Valor absoluto unario

### 1. Diferenciación del símbolo |

En el Scanner (calcHexa.l):

```
"|" { return OR_ABS; }  /* Un solo token para ambos usos */

```

En el Parser (calcHexa.y):

```
/* Como operador binario (OR) */
exp OR_ABS factor { $$ = $1 | $3; }

/* Como operador unario (valor absoluto) */  
OR_ABS exp OR_ABS        { $$ = $2 >= 0? $2 : -$2; }

```

### 2. Precedencia de Operadores

```
%left OR_ABS         /* OR: menor precedencia */
%left AND            /* AND: mayor que OR */
%left ADD SUB        /* Suma/resta: mayor que bitwise */
%left MUL DIV        /* Mult/div: mayor que suma */
%right UMINUS        /* Unarios: mayor precedencia */

```

Esto significa: 5 + 3 & 2 | 1 se evalúa como ((5 + 3) & 2) | 1

**Ejecución**

<img width="729" height="478" alt="image" src="https://github.com/user-attachments/assets/f8a08c1f-c95e-4f8d-a605-0e934b4992c0" />

---

## 4. Reconocimiento de tokens

- Pregunta: ¿La versión manuscrita del escáner en el Ejemplo 1-4 reconoce exactamente los mismos tokens que la versión generada por flex?

Hay ciertos aspectos a comparar:

### 1. Reconocimiento de Patrones

Versión flex

```
"+" { return ADD; }        /* Operador suma exacto */
[0-9]+ { ... }            /* Uno o más dígitos */
[ \t] { }                 /* Espacios y tabs */
. { ... }                 /* Cualquier otro carácter */

```

Una versión manuscrita típicamente usaría:

```
char c = getchar();
if (c == '+') return ADD;
else if (isdigit(c)) { /* leer secuencia de dígitos */ }
else if (c == ' ' || c == '\t') { /* ignorar */ }

```

### 2. Diferencias comunes

**Manejo de números**

- Flex: [0-9]+ reconoce secuencias automáticamente
- Manual: Debe hacer bucles para leer todos los dígitos

**Whitespace**

- Flex: [ \t] maneja múltiples espacios
- Manual: Puede procesar un carácter a la vez

**Caracteres desconocidos**

- Flex: . captura todo lo demás
- Manual: Debe manejar cada caso explícitamente

**Eficiencia**

- Flex: . Autómata optimizado
- Manual: Código manual con if/else

### 3. Posibles Discrepancias

**Números multi-dígito**

- Flex: 123 se reconoce como un solo token NUMBER
- Manual: Podría procesar 1, 2, 3 como tokens separados si no está bien implementado

**Secuencias de whitespace**

- Flex:     (múltiples espacios) se ignoran automáticamente
- Manual: Podría requerir bucles para consumir todos los espacios

**Manejo de EOF**

- Flex: Maneja automáticamente el final del archivo
- Manual: Debe verificar explícitamente EOF

---

## 5. Limitaciones de Flex

- Pregunta: ¿Puedes pensar en idiomas para los que Flex no sería una buena herramienta para escribir un escáner?

Flex es poderoso para muchos lenguajes, pero tiene limitaciones importantes para ciertos tipos de lenguajes.

### 1. Lenguajes Sensibles al Contexto

**Python (Indentación Significativa)**

```
if x > 0:
    print("positivo")
    if y > 0:
        print("y también positivo")
print("fin")

```

Problema con Flex:

- Flex procesa carácter por carácter sin memoria del estado anterior
- No puede rastrear niveles de indentación automáticamente
- Necesita lógica externa para manejar el stack de indentación

Por qué es difícil: Flex no puede determinar si los espacios representan entrada o salida de un bloque.

```
^[ \t]+ { /* ¿Cómo saber si es INDENT o DEDENT? */ }

```

### 2. Lenguajes con Sintaxis Dependiente del Contexto

**C/C++ con Ambigüedad Typedef**

```
typedef int T;
T * x;        // ¿T multiplicación x, o declaración de puntero?

```

Problema: Flex solo ve lexemas, no puede distinguir si T es:

- Un tipo (typedef)
- Una variable

**HTML/XML Anidado**

```
<script>
  var x = "</script>"; // ¿Fin del script o string?
</script>

```

Problema: Flex no puede manejar fácilmente contextos anidados donde las reglas cambian según el estado.

### 3. Lenguajes que Requieren Lookahead Extenso

**SQL con Palabras Clave Contextuales**

```
SELECT order FROM order ORDER BY order;

```

Problema: order puede ser:

- Palabra clave (ORDER BY)
- Nombre de tabla
- Nombre de columna

Flex no puede hacer lookahead suficiente para decidir el contexto.

### Conclusión

Flex es excelente para:

- Lenguajes con gramática regular
- Tokens bien definidos y fijos
- Sintaxis consistente

Flex NO es ideal para:

- Lenguajes sensibles al contexto
- Sintaxis que depende del estado global
- Tokens que cambian de significado según contexto semántico
- Recursión en la definición de tokens

## 6. Programa de conteo de palabras

- Pregunta: Reescriba el programa de conteo de palabras en C. Ejecute algunos archivos grandes en ambas versiones. ¿Es la versión C notablemente más rápida? ¿Fue mucho más difícil de depurar?

**Implementación**

Versión en flex

```
%{
int chars = 0;
int words = 0;
int lines = 0;
%}
%%
[a-zA-Z]+ { words++; chars += strlen(yytext); }
\n { chars++; lines++; }
. { chars++; }
%%
int main(int argc, char **argv)
{
 yylex();
 printf("%8d%8d%8d\n", lines, words, chars);
}

```

Versión en C

```
#include <stdio.h>
#include <ctype.h>
#include <stdbool.h>

int main(int argc, char **argv) {
    int chars = 0;
    int words = 0;
    int lines = 0;
    int c;
    bool in_word = false;
    
    while ((c = getchar()) != EOF) {
        chars++;
        
        if (c == '\n') {
            lines++;
            if (in_word) {
                words++;
                in_word = false;
            }
        }
        else if (isalpha(c)) {
            if (!in_word) {
                in_word = true;
            }
        }
        else {
            if (in_word) {
                words++;
                in_word = false;
            }
        }
    }
    
    /* Si el archivo termina en medio de una palabra */
    if (in_word) {
        words++;
    }
    
    printf("%8d%8d%8d\n", lines, words, chars);
    return 0;
}

```

**Método de prueba**

```
# 1. Crear archivo de prueba grande
yes "esto es una prueba" | head -1000 > test.txt

# 2. Compilar ambas versiones
flex wc_flex.l
cc -o wc_flex lex.yy.c -lfl
cc -o wc_manual wc.c

# 3. Probar y medir tiempo
echo "=== Versión Flex ==="
time ./wc_flex < test.txt

echo "=== Versión C Manual ==="
time ./wc_manual < test.txt

# 4. Comparar con wc de Unix (referencia)
echo "=== wc de Unix ==="
time wc test.txt

```

### Velocidad:

- Flex: Más rápida para archivos grandes
- C Manual: Más lenta debido a más llamadas a isalpha() y lógica de estado

### Facilidad de Depuración:

Flex - Más Fácil:

- Lógica clara y declarativa
- Patrones visuales obvios
- Menos código para debuggear

C Manual - Más Difícil:

- Lógica de estados puede ser confusa
- Más lugares donde pueden ocurrir bugs
- Casos edge más difíciles de manejar


