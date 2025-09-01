# Calculadora en ANTLR4

---

Este proyecto implementa una calculadora científica básica utilizando ANTLR 4

La calculadora interpreta expresiones matemáticas definidas en una gramática personalizada y las evalúa mediante un Visitor en Java.

## Funciones

La calculadora soporta:

- Operaciones aritméticas básicas:
    - Suma (+), Resta (-), Multiplicación (*), División (/)
- Agrupación con paréntesis: ( )
- Variables y asignación:
- Funciones matemáticas:
    - Sin(x), cos(x), tan(x), sqrt(x), ln(x), log(x)
- Factorial con el operador !
- Modo grados (por defecto) y radianes para las funciones trigonométricas.

---

## Archivos

- LabeledExpr.g4

Define la gramática de la calculadora: operaciones, funciones, factorial, etc.

- EvalVisitor.java

  - Implementa la lógica de evaluación de expresiones usando el patrón Visitor.
  - Maneja enteros y números reales (Double).
  - Implementa las funciones matemáticas y el factorial.
  - Permite trabajar en grados o radianes (variable useDegrees).

- Calc.java

Es el programa principal que:

  - Lee la entrada desde teclado o archivo.
  - Genera el árbol sintáctico con ANTLR.
  - Evalúa la expresión usando EvalVisitor.

---

## Ejecución

### 1. Generar el parser con ANTLR

En la carpeta del proyecto:

```
antlr4 -no-listener -visitor LabeledExpr.g4
```

Esto generará los archivos necesarios (LabeledExprLexer.java, LabeledExprParser.java, etc.).

### 2. Compilar

```
javac Calc.java LabeledExpr*.java
```

### 3. Ejecutar

Ejecutar con el archivo de prueba t.expr

```
java Calc t.expr
```

---

## Ejemplo

Prueba en grados

<img width="738" height="498" alt="image" src="https://github.com/user-attachments/assets/13edb775-ee90-44f7-8f1f-de2cbf5466e2" />

Prueba en radianes

<img width="738" height="498" alt="image" src="https://github.com/user-attachments/assets/1eb8bb08-5ae6-4faf-a1bb-bcfe9e37bc21" />

---

## Nota

Por defecto, las funciones trigonométricas (sin, cos, tan) trabajan en grados. Si se desea cambiar a radianes, es necesario modificar la variable:

```
boolean useDegrees = false;
```

en EvalVisitor.java.
