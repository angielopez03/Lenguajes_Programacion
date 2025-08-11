## Ejecución de los ejercicios}

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

1. Manejo de comentarios:

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
s → Regla . → Imprime "Mystery character s"
... y así con cada carácter

El resultado da error y mensajes de "Mystery character" para cada símbolo del comentario ya que no hay una regla que lo maneje.

**¿Dónde es más fácil corregirlo?**
En el ESCÁNER (Flex)
1. Nivel de Abstracción Apropiado
Los comentarios son elementos léxicos, no sintácticos:

Léxico: Patrones de caracteres (como palabras, números, símbolos)
Sintáctico: Estructura gramatical (como expresiones, declaraciones)

2. Eficiencia

```
"/*"([^*]|\*+[^*/])*\*+"/"  { /* ignorar comentarios */ }

```

El scanner puede descartar comentarios antes de enviar tokens al parser
El parser nunca ve los comentarios → más eficiente
Menos trabajo para el parser

3. Separación de Responsabilidades

Scanner: "¿Qué tipo de símbolos hay?" → Maneja comentarios
Parser: "¿Cómo se combinan estos símbolos?" → Maneja gramática
