#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Estructura para representar un estado del AFD
typedef struct {
    char tipo;       // '>' = inicial, '+' = aceptación, '-' = normal
    char nombre;     // nombre del estado (ej. 'A', 'B', 'C')
    char destino0;   // estado destino con símbolo '0'
    char destino1;   // estado destino con símbolo '1'
} Estado;

// Prototipos de funciones
int contarEstados(FILE* archivo);
void mostrarAlfabeto(FILE* archivo);
Estado* cargarEstados(FILE* archivo, int numEstados);
void mostrarTabla(Estado* estados, int numEstados);
void verificarCadenas(Estado* estados, int numEstados, FILE* archivoCadenas);
int buscarIndiceEstado(char nombreEstado, Estado* estados, int numEstados);

int main() {
    FILE *archivoConfig, *archivoCadenas;
    int numEstados;
    Estado* estados;

    // Abrir archivo de configuración
    archivoConfig = fopen("config.txt", "r");
    if(archivoConfig == NULL) {
        perror("Error al abrir config.txt");
        exit(1);
    }

    // Abrir archivo con cadenas de prueba
    archivoCadenas = fopen("prueba.txt", "r");
    if(archivoCadenas == NULL) {
        perror("Error al abrir prueba.txt");
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

// Cuenta cuántos estados hay antes del separador "-"
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

// Muestra el alfabeto definido en el archivo después de "-"
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

// Carga los estados y transiciones en memoria
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

// Muestra la tabla de transiciones
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

// Busca el índice de un estado por nombre
int buscarIndiceEstado(char nombreEstado, Estado* estados, int numEstados) {
    for(int i=0; i<numEstados; i++) {
        if(estados[i].nombre == nombreEstado) {
            return i;
        }
    }
    return -1; // no encontrado
}

// Verifica cada cadena en el archivo
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
