# Autómata

Este programa es un simulador de un Autómata Finito Determinista (AFD) que:

- Lee la configuración del autómata desde config.txt.
- Incluye estados, transiciones, estado inicial y estados de aceptación.
- Construye una tabla de transiciones en memoria.
- Muestra la tabla de transiciones.
- Lee cadenas de prueba desde prueba.txt.
- Verifica si cada cadena es aceptada o rechazada por el AFD.

---

# Explicación del código

```
// Estructura para representar un estado del AFD
typedef struct {
    char tipo;       // '>' = inicial, '+' = aceptación, '-' = normal
    char nombre;     // nombre del estado (ej. 'A', 'B', 'C')
    char destino0;   // estado destino con símbolo '0'
    char destino1;   // estado destino con símbolo '1'
} Estado;


---


```

## int contarEstados(FILE* archivo)

```
int contarEstados(FILE* archivo) {
    char buffer[8];
    int contador = -1;
    do {
        fgets(buffer, 8, archivo);
        contador++;
    } while(buffer[0] != '-');
    fseek(archivo, 0, SEEK_SET); // rebobinar
    return contador;
}

```

- Qué hace:

Cuenta cuántos estados hay definidos en el archivo config.txt.

- Cómo funciona:

1. Lee línea por línea hasta encontrar una línea que empiece con '-' (ese guion marca el fin de la lista de estados).
2. Cada vez que lee una línea, aumenta el contador.
3. Al final regresa el número de estados y reinicia el puntero del archivo con fseek para que luego pueda volver a leerse desde el inicio.

---

## void mostrarAlfabeto(FILE* archivo)

```
void mostrarAlfabeto(FILE* archivo) {
    char linea[10], simbolo;
    do {
        fgets(linea, 8, archivo);
    } while(linea[0] != '-');

    printf("Alfabeto: ");
    do {
        simbolo = fgetc(archivo);
        printf("%c", simbolo);
    } while(simbolo != '\n');
    printf("\n");
    fseek(archivo, 0, SEEK_SET); // rebobinar
}

```

- Qué hace:

Muestra en pantalla el alfabeto/lenguaje del autómata.

- Cómo funciona:
1. Lee líneas hasta encontrar la que empieza con '-'.
2. Después imprime carácter por carácter lo que sigue (el lenguaje, ej: 01) hasta que encuentra un salto de línea \n.
3. Reinicia el puntero del archivo (fseek) para que no se pierda lo ya leído.

---

## Estado* cargarEstados(FILE* archivo, int numEstados)

```

Estado* cargarEstados(FILE* archivo, int numEstados) {
    Estado* estados = (Estado*) calloc(numEstados, sizeof(Estado));
    char buffer[8];
    for(int i=0; i<numEstados; i++) {
        fgets(buffer, 8, archivo);
        estados[i].tipo     = buffer[0];
        estados[i].nombre   = buffer[1];
        estados[i].destino0 = buffer[2];
        estados[i].destino1 = buffer[3];
    }
    return estados;
}

```

- Qué hace:

Crea y llena la tabla de transiciones del AFD en memoria dinámica.

- Cómo funciona:

1. Reserva memoria dinámica para una tabla numEstados x 4.
2. Cada fila representa un estado.
3. Cada columna guarda información:
4. Columna 0 → tipo de estado (>, +, o vacío).
5. Columna 1 → nombre del estado (ej: A, B).
6. Columna 2 → transición con símbolo 0.
7. Columna 3 → transición con símbolo 1.
8. Recorre el archivo y copia esos datos a la tabla.

---

## void mostrarTabla(Estado* estados, int numEstados)

```

void mostrarTabla(Estado* estados, int numEstados) {
    printf("\nTabla de transiciones:\n");
    printf("Tipo Estado  0   1\n");
    for(int i=0; i<numEstados; i++) {
        printf(" [%c]   %c    %c   %c\n", 
            estados[i].tipo, 
            estados[i].nombre, 
            estados[i].destino0, 
            estados[i].destino1);
    }
    printf("\n");
}

```

- Qué hace:

Muestra la tabla de transiciones para que el usuario vea cómo está estructurado el AFD.

- Cómo funciona:

Recorre cada estado (for) y cada columna (for) e imprime con formato [ ] los datos.

---

## int buscarIndiceEstado(char nombreEstado, Estado* estados, int numEstados)

```

int buscarIndiceEstado(char nombreEstado, Estado* estados, int numEstados) {
    for(int i=0; i<numEstados; i++) {
        if(estados[i].nombre == nombreEstado) {
            return i;
        }
    }
    return -1; // no encontrado
}

```

- Qué hace:

Localiza el índice de un estado dentro de la tabla.

- Cómo funciona:

1. Recorre todos los estados y compara si el estado coincide con la columna 1 de alguna fila de la tabla. Si coincide, regresa el índice.
2. Si no lo encuentra, imprime un error.

---

## void verificarCadenas(Estado* estados, int numEstados, FILE* archivoCadenas)

```

void verificarCadenas(Estado* estados, int numEstados, FILE* archivoCadenas) {
    char cadena[100];

    while(fgets(cadena, 100, archivoCadenas) != NULL) {
        cadena[strcspn(cadena, "\n")] = 0; // quitar salto de línea

        char estadoActual = '\0';
        // Buscar estado inicial
        for(int i=0; i<numEstados; i++) {
            if(estados[i].tipo == '>' || estados[i].tipo == '+') {
                estadoActual = estados[i].nombre;
                break;
            }
        }

        // Caso de cadena vacía (E)
        if(cadena[0] == 'E') {
            int idx = buscarIndiceEstado(estadoActual, estados, numEstados);
            if(idx != -1 && estados[idx].tipo == '+') {
                printf("Cadena \"%s\" aceptada (E)\n", cadena);
            } else {
                printf("Cadena \"%s\" no aceptada\n", cadena);
            }
            continue;
        }

        // Recorrer cada símbolo de la cadena
        for(int i=0; cadena[i] != '\0'; i++) {
            int idx = buscarIndiceEstado(estadoActual, estados, numEstados);
            if(idx == -1) break;

            if(cadena[i] == '0') {
                estadoActual = estados[idx].destino0;
            } else if(cadena[i] == '1') {
                estadoActual = estados[idx].destino1;
            }
        }

        // Verificar aceptación
        int idxFinal = buscarIndiceEstado(estadoActual, estados, numEstados);
        if(idxFinal != -1 && estados[idxFinal].tipo == '+') {
            printf("Cadena \"%s\" aceptada\n", cadena);
        } else {
            printf("Cadena \"%s\" no aceptada\n", cadena);
        }
    }
}



```

- Qué hace:

Verifica una a una las cadenas del archivo Cadenas.txt y decide si son aceptadas o rechazadas.

- Cómo funciona:

1. Lee una cadena de prueba (ej: 1010).
2. Quita el salto de línea \n.
3. Busca el estado inicial (marcado con > o +).
4. Si la cadena es "E" (cadena vacía), revisa directamente si el estado inicial es de aceptación (+).
5. Si no es vacía, recorre cada símbolo:
6. Si es 0, busca en la tabla la transición correspondiente.
7. Si es 1, lo mismo pero en otra columna.
8. Al final revisa si el estado en el que terminó es de aceptación (+).

---

## int main()

```
int main() {
    FILE *archivoConfig, *archivoCadenas;
    int numEstados;
    Estado* estados;

    // Abrir archivo de configuración
    archivoConfig = fopen("Conf.txt", "r");
    if(archivoConfig == NULL) {
        perror("Error al abrir Conf.txt");
        exit(1);
    }

    // Abrir archivo con cadenas de prueba
    archivoCadenas = fopen("Cadenas.txt", "r");
    if(archivoCadenas == NULL) {
        perror("Error al abrir Cadenas.txt");
        exit(1);
    }

    // Procesar configuración del AFD
    numEstados = contarEstados(archivoConfig);
    mostrarAlfabeto(archivoConfig);
    estados = cargarEstados(archivoConfig, numEstados);

    // Mostrar tabla de transiciones
    mostrarTabla(estados, numEstados);

    // Verificar las cadenas
    verificarCadenas(estados, numEstados, archivoCadenas);

    // Liberar memoria y cerrar archivos
    free(estados);
    fclose(archivoConfig);
    fclose(archivoCadenas);

    return 0;
}

```

- Qué hace:

Es el flujo principal del programa:

1. Abre los archivos config.txt y prueba.txt.
2. Llama a contarEstados para saber cuántos estados tiene el AFD.
3. Llama a mostrarAlfabeto para mostrar el alfabeto.
4. Crea la tabla con cargarEstados.
5. La imprime con mostrarTabla.
6. Verifica las cadenas de prueba con verificarCadenas.
7. Cierra los archivos y termina.
