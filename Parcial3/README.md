# Parcial 3

1. Modele una función que genere una gramática de atributos para una Lenguaje de programación que realice consultas de tipo SQL (CRUD)
2. Diseñe una gramática para un lenguaje de programación que sea capaz de resolver el producto punto entre dos matrices de diferentes dimensiones
3. Implemente en ANTLR la gramática del punto 2. Lenguaje objetivo python.

## Punto 1

### Operaciones Implementadas

- CREATE (`new`) - Insertar registros
- READ (`get`) - Consultar registros
- UPDATE (`set`) - Actualizar registros
- DELETE (`drop`) - Eliminar registros
- WHERE - Filtros condicionales en todas las operaciones
- Múltiples tablas - Hasta 10 tablas simultáneas
- Tipos de datos - Números, strings, booleanos, null
- Persistencia en sesión - Los datos se mantienen durante la ejecución

### Operadores Soportados

| Operador | Descripción | Ejemplo |
|----------|-------------|---------|
| `=` | Igual | `age = 25` |
| `!=` | Diferente | `status != "inactive"` |
| `>` | Mayor que | `price > 100` |
| `<` | Menor que | `stock < 10` |
| `>=` | Mayor o igual | `age >= 18` |
| `<=` | Menor o igual | `quantity <= 50` |

---

### Notación BNF

```bnf
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
