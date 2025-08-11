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

### 1. Nivel de abstracción apropiado

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

### 3. Separación de responsabilidades

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

No. La versión manuscrita reconoce más tokens que la versión Flex

Hay ciertos aspectos a comparar:

### Diferencias principales

- Tokens adicionales en la versión manuscrita

```
case '(': return OP;    /* Paréntesis izquierdo */
case ')': return CP;    /* Paréntesis derecho */

```

En Flex: Los paréntesis se tratarían como "Mystery character"

- Manejo de comentarios

Versión manuscrita
  
```
case '/': c = getc(yyin);
if(c == '/') {
    /* it's a comment */
    while((c = getc(yyin)) != '\n')
        if(c == EOF) return 0;
    break;  /* Ignora toda la línea */
}

```

En Flex: No hay manejo de comentarios - / solo es DIV

- Manejo de números multidígito

Ambas versiones son funcionalmente iguales:

- Flex: [0-9]+ automáticamente
- Manuscrita: Bucle manual pero mismo resultado

### Comportamiento con entrada de prueba

**Entrada:** 3 + (4 / 2) // comentario

- Flex: NUMBER(3) ADD Mystery( Mystery) DIV NUMBER(2) Mystery) Mystery/ Mystery/ ...
- Manuscrito: NUMBER(3) ADD OP NUMBER(4) DIV NUMBER(2) CP EOL

### Manejo de EOF

Manuscrita: Manejo sofisticado del EOF

```
static int seeneof = 0;
if(seeneof) return 0;
if(c == EOF) seeneof = 1;

```
Flex: Manejo automático más simple

### Robustez

La versión manuscrita es más robusta:

- Soporta paréntesis para expresiones complejas
- Ignora comentarios de línea (//)
- Mejor manejo de EOF en casos edge

La versión flex es más simple:

- Código más conciso
- Menos propenso a bugs
- Pero menos funcional

**Respuesta:** No, la versión manuscrita reconoce más tokens que la versión Flex:

- Adicionales: OP (paréntesis izquierdo), CP (paréntesis derecho)
- Funcionalidad extra: Ignora comentarios //
- Menos tokens "Mystery": Maneja casos que Flex reportaría como desconocidos

La versión manuscrita es más completa pero más compleja de mantener.

---

## 5. Limitaciones de flex

- Pregunta: ¿Puedes pensar en idiomas para los que Flex no sería una buena herramienta para escribir un escáner?

Flex es poderoso para muchos lenguajes, pero tiene limitaciones importantes para ciertos tipos de lenguajes.

### 1. Lenguajes sensibles al contexto

**Python (indentación significativa)**

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

### 2. Lenguajes con sintaxis dependiente del contexto

**C/C++ con ambigüedad typedef**

```
typedef int T;
T * x;        // ¿T multiplicación x, o declaración de puntero?

```

Problema: Flex solo ve lexemas, no puede distinguir si T es:

- Un tipo (typedef)
- Una variable

**HTML/XML anidado**

```
<script>
  var x = "</script>"; // ¿Fin del script o string?
</script>

```

Problema: Flex no puede manejar fácilmente contextos anidados donde las reglas cambian según el estado.

### 3. Lenguajes que requieren lookahead extenso

**SQL con palabras clave contextuales**

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

Flex no es ideal para:

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
yes "esto es una prueba" | head -1000000 > test.txt

# 2. Compilar ambas versiones
flex wc_flex.l
cc -o wc_flex lex.yy.c -lfl
cc -o wc_manual wc_manual.c

# 3. Probar y medir tiempo
echo "=== Versión Flex ==="
time ./wc_flex < test.txt

echo "=== Versión C Manual ==="
time ./wc_manual < test.txt

```

### Ejecución:

<img width="739" height="383" alt="image" src="https://github.com/user-attachments/assets/25a4907b-fe59-4ff6-9834-06feeaa923dd" />

**Análisis de resultados**

Rendimiento:

- C Manual: 0.128s
- Flex: 0.261s
  
C Manual es 104% más rápida (más del doble de velocidad)

**¿Por qué C manual es más rápido?**

1. Overhead de Flex

```
// Flex internamente hace algo como:
while (state != FINAL) {
    c = input();
    state = transition_table[state][c];  // Búsqueda en tabla
    // Más lógica de autómata...
}

```

2. Simplicidad de C manual

```
// C manual es directo:
c = getchar();           // Una sola llamada
if (isalpha(c)) { ... }  // Verificación simple

```

3. Factores técnicos

Flex tiene más overhead porque:

- Tablas de transición: Consulta tablas en memoria para cada carácter
- Función strlen(): Calcula longitud de cada palabra reconocida
- Buffer management: Maneja buffers internos
- Lógica de backtracking: Para patrones complejos

C Manual es más eficiente porque:

- Una sola pasada: Un getchar() por carácter
- Sin strlen(): Cuenta caracteres sobre la marcha
- Lógica mínima: Solo verifica isalpha() y maneja estado

**¿Cuándo flex podría ser más rápida?**

Patrones Muy Complejos:

```
/* Si tuviera patrones como estos: */
[a-zA-Z][a-zA-Z0-9_]*\.[a-zA-Z]{2,4}    /* emails */
https?://[^\s]+                          /* URLs */
[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}  /* IPs */

```
La versión manual sería muchísimo más compleja y probablemente más lenta.

- Múltiples estados: Si necesitara manejar comentarios, strings, etc., la versión manual se volvería muy complicada.

**Conclusión**

Para conteo simple de palabras C manual siempre será más rápida, la tarea es tan simple que el overhead de Flex no se justifica
