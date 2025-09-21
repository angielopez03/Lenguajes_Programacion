# Analizador Sintáctico con Árbol de Sintaxis

Este proyecto implementa un analizador sintáctico en Python.

El programa:

* Lee una gramática libre de contexto desde un archivo (`gra.txt`).
* Recibe cadenas de prueba desde la consola.
* Genera un árbol de sintaxis con la librería `networkx` y lo dibuja con `matplotlib`.

---

## ¿Cómo funciona?

1. **Gramática (`gra.txt`)**
   Se define con producciones en forma:

   ```
    E -> E opsuma T
    E -> T
    T -> T opmul F
    T -> F
    F -> id
    F -> num
    F -> pari E pard
   ```

   * Los terminales como `+`, `*`, `(`, `)` se mapearon a tokens (`opsuma`, `opmul`, `pari`, `pard`) para facilitar la escritura.
   * Los no terminales son `E`, `T`, `F`.
   * Los terminales `num` e `id` se conectan a los valores concretos de la cadena (por ejemplo: `num -> 2`).

2. **Tokenización**

   * Convierte la cadena de entrada en tokens (`['num', 'opsuma', 'num', 'opmul', 'num']`)
   * También guarda los valores reales (`['2', '+', '3', '*', '4']`)
   * Si aparece un símbolo no soportado, el analizador lo rechaza inmediatamente.

3. **Algoritmo de Earley**

   * Construye una tabla (*chart*) con los posibles estados de análisis.
   * Permite procesar **gramáticas con recursión izquierda**, algo que los parsers recursivos simples no pueden hacer (aparecía el error `RecursionError`).
   * El análisis termina aceptando o rechazando la cadena.

4. **Construcción del árbol**

   * A partir de los estados aceptados, se reconstruye la derivación.
   * Cada símbolo se convierte en un nodo del grafo (`E`, `T`, `F`, `opsuma`, etc.).
   * Los terminales `num` e `id` se expanden con su valor concreto (`2`, `3`, `x`, etc.).
   * Se genera un **grafo dirigido** en `networkx` y se dibuja en forma jerárquica.

---

## ¿Por qué un analizador de Earley?

El algoritmo de Earley es general:

* Soporta **cualquier gramática libre de contexto**, incluso con **recursión izquierda directa o indirecta**.
* No necesita backtracking manual, ni eliminar recursión izquierda de la gramática.
* Es eficiente para expresiones matemáticas como `2+3*(4+5)` donde aparecen anidaciones y combinaciones de operadores.

Esto evita los problemas que surgían con un parser recursivo simple, que entraba en bucles infinitos con reglas como:

```
E -> E opsuma T
```

---

## Cadenas de ejemplo

Si la cadena es aceptada → se mostrará **ACEPTADA** y el **árbol de sintaxis** en una ventana gráfica. Si contiene símbolos no definidos o no cumple la gramática → mostrará **NO ACEPTADA**.

### 2+3*4

<img width="1183" height="156" alt="image" src="https://github.com/user-attachments/assets/b3d3070e-3ba8-4c3e-9c61-95463a580627" />

<img width="794" height="676" alt="image" src="https://github.com/user-attachments/assets/a4cea61d-6a5b-41d8-afcf-ae9793b9d513" />

### 2+3-4

<img width="1224" height="165" alt="image" src="https://github.com/user-attachments/assets/96219ee2-5691-47c2-b621-996711da6789" />

### 2+3*(4+5)

<img width="283" height="67" alt="image" src="https://github.com/user-attachments/assets/23a43493-81ec-410e-8393-78ff841c0b23" />


<img width="1917" height="1016" alt="image" src="https://github.com/user-attachments/assets/a76f8e68-54e8-4649-8a5f-8f95b06b5661" />

### 2+3*(4-5)

<img width="496" height="96" alt="image" src="https://github.com/user-attachments/assets/3c5e7870-8e3a-4509-8f29-d38f91c85a9c" />


---
