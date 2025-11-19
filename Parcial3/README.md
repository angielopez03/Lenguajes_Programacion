# Parcial 3

1. Modele una función que genere una gramática de atributos para una Lenguaje de programación que realice consultas de tipo SQL (CRUD)
2. Diseñe una gramática para un lenguaje de programación que sea capaz de resolver el producto punto entre dos matrices de diferentes dimensiones
3. Implemente en ANTLR la gramática del punto 2. Lenguaje objetivo python.

## Punto 1

### Operaciones Implementadas

- CREATE (new) - Insertar registros
- READ (get) - Consultar registros
- UPDATE (set) - Actualizar registros
- DELETE (drop) - Eliminar registros
- WHERE - Filtros condicionales en todas las operaciones
- Múltiples tablas
- Tipos de datos - Números, strings, booleanos, null
- Persistencia en sesión - Los datos se mantienen durante la ejecución

### Notación BNF

```
# ===== PROGRAMA =====

<programa> ::= { <sentencia> }

<sentencia> ::= <create_op>
              | <read_op>
              | <update_op>
              | <delete_op>

# ===== CREATE (INSERT) =====

<create_op> ::= "new" <identificador> "{" <pares> "}"

# ===== READ (SELECT) =====

<read_op> ::= "get" <identificador> [ <opt_where> ]

# ===== UPDATE =====

<update_op> ::= "set" <identificador> "{" <pares> "}" [ <opt_where> ]

# ===== DELETE =====

<delete_op> ::= "drop" <identificador> [ <opt_where> ]

# ===== CLÁUSULA WHERE =====

<opt_where> ::= ε                                          # Vacío (opcional)
              | "where" <identificador> <operador> <valor>

<operador> ::= "=" | "!=" | ">" | "<" | ">=" | "<="

# ===== VALORES =====

<pares> ::= <par> { "," <par> }

<par> ::= <identificador> ":" <valor>

<valor> ::= <numero>
          | <cadena>
          | <booleano>
          | <nulo>

<numero> ::= [0-9]+ [ "." [0-9]+ ]

<cadena> ::= '"' <caracter>* '"' | "'" <caracter>* "'"

<booleano> ::= "true" | "false"

<nulo> ::= "null"

<identificador> ::= [a-zA-Z_] [a-zA-Z0-9_]*

# ===== COMENTARIOS =====

<comentario> ::= "#" <resto_de_linea>
               | "//" <resto_de_linea>
```

#### CREATE - Insertar registros
Insertar usuarios

```
new users { name: "Ana", age: 25, active: true }
```

#### READ - Consultar registros
Leer todos los usuarios

```
get users
```

#### READ con WHERE - Consultas filtradas
Usuarios mayores de edad

```
get users where age >= 18
```

#### UPDATE - Actualizar registros

Actualizar edad de Ana

```
set users { age: 26 } where name = "Ana"
```

#### DELETE - Eliminar registros
Eliminar usuario menor de edad

```
drop users where age < 18
```
### Atributos generados

| Atributo | Tipo         | Descripción                                      |
| -------- | ------------ | ----------------------------------------------- |
| sql    | string       | Sintético (genera SQL final)                    |
| tabla  | string       | Heredado (nombre de la tabla objetivo)          |
| cols   | list<string> | Sintético (lista de columnas)                   |
| vals   | list<string> | Sintético (lista de valores SQL)                |
| cond   | string       | Sintético (condición SQL generada)              |
| lexema | string       | Sintético (captura literal del lexer en tokens) |


### Función generadora de una gramática de atributos

```
FUNCIÓN GenerarGramaticaDeAtributos(BNF)
    GA ← nueva_gramatica()              # Gramática con atributos
    PARA CADA produccion P EN BNF HACER
        regla ← P                       # Copiar estructura sintáctica
        
        SI encabezado(P) ES "new"       # CREATE → INSERT
            regla.agregarAtributo("sql", 
                "INSERT INTO " + <identificador>.lexema +
                "(" + <pares>.cols + ") VALUES (" + <pares>.vals + ");")

        SINO SI encabezado(P) ES "get"  # READ → SELECT
            regla.agregarAtributo("sql",
                "SELECT * FROM " + <identificador>.lexema +
                condicionOpcional(<opt_where>.cond))

        SINO SI encabezado(P) ES "set"  # UPDATE
            regla.agregarAtributo("sql",
                "UPDATE " + <identificador>.lexema +
                " SET " + <pares>.cols_vals +
                condicionOpcional(<opt_where>.cond) + ";")

        SINO SI encabezado(P) ES "drop" # DELETE
            regla.agregarAtributo("sql",
                "DELETE FROM " + <identificador>.lexema +
                condicionOpcional(<opt_where>.cond) + ";")

        SINO SI P CONTIENE <pares>
            regla.agregarAtributo("cols", concatenarCampos(P))
            regla.agregarAtributo("vals", concatenarValores(P))
            regla.agregarAtributo("cols_vals", concatenarAsignaciones(P))

        SINO SI P CONTIENE <opt_where>
            regla.agregarAtributo("cond", construirCondicion(P))

        SINO SI P TERMINA EN <valor>
            regla.agregarAtributo("lexema", convertirLiteral(P))

        FIN SI
        
        GA.agregarRegla(regla)
    FIN PARA
    
    RETORNAR GA
FIN FUNCIÓN
```
---

## Punto 2

### Notación BNF

```
<programa> ::= <sentencia>+

<sentencia> ::= <identificador> "=" <expresion> ";"

<expresion> ::= <matriz>
              | <expresion> "·" <expresion>

<matriz> ::= "[" <filas> "]"

<filas> ::= <fila> (";" <fila>)*

<fila> ::= "[" <numero> ("," <numero>)* "]"

<numero> ::= ["-"] <digito>+ ["." <digito>+]

<identificador> ::= <letra> (<letra> | <digito> | "_")*

<letra> ::= "a" | "b" | ... | "z" | "A" | "B" | ... | "Z"

<digito> ::= "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9"
```
---

### Punto 3

Ejecutar

```
antlr4 -Dlanguage=Python3 -visitor matrices.g4
python3 main.py prueba.txt
```
