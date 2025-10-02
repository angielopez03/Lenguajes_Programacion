# Implementación de la gramática

*Por: Laura Sophia Hernández, Angie Lorena López y María Belén Peña*

<br>

Esta implementación a lenguaje python imprime los primeros, siguientes y predicción de la gramática introducida; para ello se evaluaron los dos ejercicios ya resueltos a mano para comprobar su resultado.

### Gramáticas

Ejercicio 1:
```
"S->A uno B C", 
"S->S dos", 
"A->B C D", 
"A->A tres", 
"A->ε", 
"B->D cuatro C tres", 
"B->ε", 
"C->cinco D B", 
"C->ε", 
"D->seis", 
"D->ε"
```

Ejercicio 2:
```
"S ->A B uno",
"A -> dos B",
"A ->ε",
"B -> C D",     
"B -> tres",
"B ->ε",
"C -> cuatro A B",
"C -> cinco",
"D -> seis",
"D ->ε"
```

## Código

**Parsear_produccion:**
<img width="938" height="677" alt="image" src="https://github.com/user-attachments/assets/ae18c347-85aa-42ee-bc3b-ca8bfdbecad6" />
<img width="610" height="435" alt="image" src="https://github.com/user-attachments/assets/766d9113-8a68-4b36-b3c9-100b7b508169" />

Va entrando cadena por cadena, separa lado derecho o izquierdo en lo que dicte la flecha y guarda en no terminal si es mayúscula y un solo caracter, y el resto en terminal exceptuando vacios.

Organiza los simbolos ahora llamados índices y calcula los primeros.

<br>

**Primeros_no_terminales:**
<img width="905" height="874" alt="image" src="https://github.com/user-attachments/assets/778f08c9-f0e4-44d9-b8b2-4636a85a5a01" />

Construye primeros_nt (un diccionario que para cada no terminal contiene su conjunto de primeros), de esa manera es más fácil actualizar y extraer los primeros(i) de los primeros(i), etc.

<br>

**Cálculo_siguientes:**
<img width="782" height="800" alt="image" src="https://github.com/user-attachments/assets/9895869e-b267-427c-928d-313631364811" />

Calcula los siguientesconsiderando los vacios y repeticiones, iniciando la primera línea siempre con $.

<br>

**Cálculo_predicción:**
<img width="900" height="450" alt="image" src="https://github.com/user-attachments/assets/abd0a373-6d31-4970-b866-b70c33c390ce" />

Se calcula la predicción de cada regla, teniendo en cuenta el vacío y la unión de los siguientes.


## Resultados

Gramática 1:

<img width="511" height="792" alt="image" src="https://github.com/user-attachments/assets/3481b06a-6846-4ed0-a894-5ffe7bd23163" />

<br>
<br>

Gramática 2:

<img width="501" height="750" alt="image" src="https://github.com/user-attachments/assets/29234f3e-f70b-44fd-9d9c-14cbc354ac1b" />

<br>
<br>

:D
