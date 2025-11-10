# EDTS - Calculadora Aritmética

Sistema completo de **Esquema de Traducción Dirigido por la Sintaxis** (EDTS) para una calculadora que soporta suma, resta, multiplicación y división.

## Componentes

1. **Gramática libre de contexto** sin recursión izquierda (LL(1))
2. **Atributos sintetizados y heredados** para evaluación semántica
3. **Conjuntos PRIMEROS, SIGUIENTES y PREDICCIÓN** para análisis sintáctico
4. **AST decorado** con valores calculados en cada nodo
5. **Tabla de símbolos** con constantes y variables temporales
6. **Gramática de atributos** con reglas semánticas
7. **EDTS completo** con acciones intercaladas
8. **Generador de código intermedio** (tres direcciones)

## Gramática

```
E  → T E'
E' → + T E' | - T E' | ε
T  → F T'
T' → * F T' | / F T' | ε
F  → num | ( E )
```

## Ejecución

El sistema genera:

1. **Gramática formal** con todas las producciones
2. **Conjuntos de análisis:**
   ```
   PRIMEROS(E) = { (, num }
   SIGUIENTES(E) = { $, ) }
   PREDICCIÓN(E → T E') = { (, num }
   ```

3. **AST decorado:**
   ```
   [OP: +]
     ├─ val = 13
     ├─ temp = t2
     ├─ hijo_izq:
     │   [NUM: 3.0]
     │     └─ val = 3.0
     └─ hijo_der:
         [OP: *]
           ├─ val = 10.0
           ├─ temp = t1
           ├─ hijo_izq:
              [NUM: 5.0]
                └─ val = 5.0
           └─ hijo_der:
              [NUM: 2.0]
                └─ val = 2.0
   ```

4. **Tabla de símbolos:**
   ```
   Nombre       Tipo         Valor      Dirección
   t1           temporal     10.0       100
   t2           temporal     13.0       104
   _const3      constante    3.0        -
   ```

5. **Código intermedio:**
   ```
   1. t1 := 5.0 * 2.0
   2. t2 := 3.0 + t1
   ```

## Conceptos clave

### Atributos
- **Sintetizados (↑)**: val - Se calculan de hijos a padres
- **Heredados (↓)**: inh - Se calculan de padres a hijos

### Código de Tres Direcciones
Formato: resultado := operando1 operador operando2

Ejemplo:

```
t1 := 5 * 2    # Primero: multiplicación
t2 := 3 + t1   # Luego: suma
```
