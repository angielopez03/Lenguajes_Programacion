# ETDS y código de tres direcciones

Este proyecto implementa un Esquema de Traducción Dirigido por Sintaxis (ETDS) para un subconjunto del lenguaje Python. El traductor genera:

- AST Decorado (Árbol de Sintaxis Abstracta con atributos)
- Tabla de Símbolos con variables, temporales y constantes
- Código Intermedio en representación de tres direcciones

---

## Uso

1. **Crear archivo de entrada** `entrada.txt`:
```python
z = x * 2 + y / 4 - 5
```

2. **Ejecutar el traductor**:
```bash
python tabla.py
```

3. **Ver resultados**:
   - AST decorado en consola
   - Tabla de símbolos
   - Código de tres direcciones


## Ejemplos de uso

### Ejemplo 1: Expresión Aritmética Simple
**Entrada (`entrada.txt`):**
```python
x = 5 + 3
```

**Salida esperada:**
```
AST DECORADO:
[ASSIGN: =]
  └─ lugar = x
  ├─ [ID: x]
  └─ [BINOP: +]
    └─ lugar = t1
    ├─ [NUM: 5]
      └─ lugar = 5
    └─ [NUM: 3]
      └─ lugar = 3

CÓDIGO INTERMEDIO:
   1. t1 := 5 + 3
   2. x := t1
```

### Ejemplo 2: Expresión compleja con paréntesis
**Entrada:**
```python
resultado = (10 + 5) * 2 - 8 / 4
```

**Código de tres direcciones:**
```
1. t1 := 10 + 5
2. t2 := t1 * 2
3. t3 := 8 / 4
4. t4 := t2 - t3
5. resultado := t4
```

---

## Características soportadas

### Expresiones Aritméticas
- Operadores: `+`, `-`, `*`, `/`, `%`
- Precedencia y asociatividad correctas
- Paréntesis para agrupar

### Literales
- Enteros: `42`, `0`, `1234`
- Cadenas: `"hola"`, `'mundo'`
- Booleanos: `True`, `False`
- None: `None`

### Variables
- Declaración implícita
- Asignación: `x = 10`
- Uso en expresiones

### Listas
- Literales: `[1, 2, 3]`
- Acceso: `lista[0]`
- Listas anidadas: `[[1, 2], [3, 4]]`

### Operadores relacionales
- Comparaciones: `>`, `<`, `>=`, `<=`, `==`, `!=`
- En expresiones condicionales

---

## Gramática soportada

### Gramática sdimplificada del ETDS

```
E  → T E'
E' → + T E' | - T E' | ε
T  → F T'
T' → * F T' | / F T' | % F T' | ε
F  → num | id | ( E ) | [ Lista ] | llamada

S  → id = E
C  → E relop E
```

---

## Esquema de traducción

### Atributos utilizados

- **`lugar`**: Nombre de la variable/temporal donde se guarda el resultado
- **`inh`** (heredado): Valor que viene del padre
- **`val`**: Valor sintetizado hacia arriba

### Acciones semánticas principales

```python
E → T { E'.inh := T.lugar } 
    E' { E.lugar := E'.lugar }

E' → + T { temp := nueva_temporal() }
          { insertar_tabla(temp, 'temporal') }
          { generar(temp || ' := ' || E'.inh || ' + ' || T.lugar) }
          { E'₁.inh := temp }
       E'₁ { E'.lugar := E'₁.lugar }

F → num { F.lugar := num.lexema }
        { insertar_tabla('_const_' || num.lexema, 'constante') }
```
