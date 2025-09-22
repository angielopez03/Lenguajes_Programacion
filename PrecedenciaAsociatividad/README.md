# Prueba de Precedencia y Asociatividad con ANTLR

Se implementó una calculadora en ANTLR (lenguaje objetivo python, usando visitor)
El objetivo fue:

1. Definir una gramática original con reglas de precedencia y asociatividad clásicas:

   * Multiplicación y división (`*`, `/`) tienen mayor precedencia que suma y resta (`+`, `-`).
   * Los operadores son asociativos por la izquierda.

2. Rediseñar la gramática para modificar la asociatividad (operadores `-` y `/` con recursión derecha).

3. Ejecutar pruebas con distintas cadenas de entrada y comparar los resultados obtenidos entre las dos versiones de la gramática.

---

## Gramáticas utilizadas

### Gramática original (izquierda, precedencia normal)

* Precedencia: `*`, `/` > `+`, `-`
* Asociatividad: izquierda para todos los operadores

```
grammar expr;

prog:   stat+ ;

stat:   expr NEWLINE                # printExpr
    |   ID '=' expr NEWLINE         # assign
    |   NEWLINE                     # blank
    ;

expr:   expr op=('*'|'/') expr      # MulDiv
    |   expr op=('+'|'-') expr      # AddSub
    |   INT                         # Int
    |   ID                          # Id
    |   '(' expr ')'                # Parens
    ;

MUL :   '*' ;
DIV :   '/' ;
ADD :   '+' ;
SUB :   '-' ;
ID  :   [a-zA-Z]+ ;
INT :   [0-9]+ ;
NEWLINE:'\r'? '\n' ;
WS  :   [ \t]+ -> skip ;
```

---

### Gramática con preceddencia modificada

* Precedencia: `+`, `-` > `*`, `/`
* Asociatividad: izquierda para todos los operadores

```
grammar expr;

prog:   stat+ ;

stat:   expr NEWLINE                # printExpr
    |   ID '=' expr NEWLINE         # assign
    |   NEWLINE                     # blank
    ;

expr:   expr op=('+'|'-') expr      # AddSub
    |   expr op=('*'|'/') expr      # MulDiv
    |   INT                         # Int
    |   ID                          # Id
    |   '(' expr ')'                # Parens
    ;

MUL :   '*' ;
DIV :   '/' ;
ADD :   '+' ;
SUB :   '-' ;
ID  :   [a-zA-Z]+ ;
INT :   [0-9]+ ;
NEWLINE:'\r'? '\n' ;
WS  :   [ \t]+ -> skip ;
```

### 🔹 Pruebas de **precedencia**

Cadenas probadas con la gramática original (izquierda):

| Expresión  | Evaluación clásica             | Modificada   |
| ---------- | ------------------------------ | -------------|
| `2+3*4`    | `2 + (3*4) = 14                |  20          |
| `10+5*2`   | `10 + (5*2) = 20               |  30          |
| `1+2*3`    | `1 + (2*3) = 7                 |  9           |
| `6+3*4/2`  | `6 + ((3*4)/2) =`12            |  18          |
| `10+20*30` | `10 + (20*30)`= 610            |  900         |

<img width="866" height="149" alt="image" src="https://github.com/user-attachments/assets/98a40261-8526-429f-a665-c7cfb7d94481" />

<img width="866" height="149" alt="image" src="https://github.com/user-attachments/assets/8950458c-711c-44ac-b08b-9bbcc7300d4a" />

En la gramática original las alternativas para la suma y la multiplicación están en el mismo nivel de recursión. Dado que en ANTLR las alternativas de una regla se evalúan en el orden en que se definen, la primera alternativa que ANTLR prueba es la de suma y resta (+, -), y luego intenta la multiplicación y división (*, /). Esto hace que ANTLR priorice las sumas antes que las multiplicaciones, y esto afectará la precedencia de los operadores.

- Alternativas definidas primero en una regla de ANTLR tienen mayor precedencia porque ANTLR las evalúa primero.

- Para establecer precedencia adecuada entre operadores, es necesario definir las reglas de mayor precedencia en un nivel más interno y las de menor precedencia en un nivel más externo. Esto se logra estructurando la gramática, dividiendo las operaciones de mayor precedencia en reglas más internas (como multiplicación) y las de menor precedencia en reglas más externas (como suma).

---

### Gramática con preceddencia modificada (derecha para `-` y `/`)

* Precedencia: `*`, `/` > `+`, `-`
* Asociatividad:

  * `+` y `*` → izquierda
  * `-` y `/` → derecha

```
grammar expr;

prog:   stat+ ;

stat:   expr NEWLINE                # printExpr
    |   ID '=' expr NEWLINE         # assign
    |   NEWLINE                     # blank
    ;
    
expr
    : term (ADD term)*              # AddLeft
    | term SUB expr                 # SubRight
    | term                          # ToTerm
    ;

term
    : factor (MUL factor)*          # MulLeft
    | factor DIV term               # DivRight
    | factor                        # ToFactor
    ;

factor
    : INT                           # Int
    | ID                            # Id
    | '(' expr ')'                  # Parens
    ;

MUL : '*' ;
DIV : '/' ;
ADD : '+' ;
SUB : '-' ;
ID  : [a-zA-Z]+ ;
INT : [0-9]+ ;
NEWLINE : [\r\n]+ ;
WS : [ \t]+ -> skip ;
```

### 🔹 Pruebas de **asociatividad**

Comparación entre la gramática clásica (izquierda) y la modificada (derecha):

| Expresión   | Izquierda (clásica)  | Derecha (modificada)  |
| ----------- | -------------------- | --------------------- |
| `10-5-2`    | `(10 - 5) - 2 = 3`   | `10 - (5 - 2) = 7`    |
| `100/10/2`  | `(100 / 10) / 2 = 5` | `100 / (10 / 2) = 20` |
| `40-20-3-5` | `((40-20)-3)-5 = 12` | `40-(20-(3-5)) = 18`  |
| `50/5/2`    | `(50 / 5) / 2 = 5`   | `50 / (5 / 2) = 20`   |
| `30-10-5`   | `(30 - 10) - 5 = 15` | `30 - (10 - 5) = 25`  |

<img width="866" height="156" alt="image" src="https://github.com/user-attachments/assets/1a480232-d067-4e6f-a928-76bd7fb8a326" />

<img width="866" height="153" alt="image" src="https://github.com/user-attachments/assets/01404f7d-8e0c-43f6-b967-da83fd71885c" />


Aquí se observa claramente la diferencia:

* Con asociatividad izquierda, la operación se agrupa desde el principio hacia la izquierda.
* Con asociatividad derecha, la operación se agrupa hacia el final.

---

## Conclusiones

* La **precedencia** define qué operadores se evalúan primero (ejemplo: multiplicación antes que suma).
* La **asociatividad** define el orden de agrupamiento de operadores del mismo nivel.
* Para operadores asociativos (`+`, `*`), el resultado no cambia.
* Para operadores no asociativos (`-`, `/`), el resultado sí cambia dependiendo de si la gramática es izquierda o derecha.

