#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    char tipo;       // '>' = inicial, '+' = aceptación, '-' = normal
    char nombre;     // nombre del estado (ej. 'A', 'B', 'C')
    char destino0;   // estado destino con símbolo '0'
    char destino1;   // estado destino con símbolo '1'
} Estado;

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

    archivoConfig = fopen("Conf.txt", "r");
    if(archivoConfig == NULL) {
        perror("Error al abrir Conf.txt");
        exit(1);
    }

    archivoCadenas = fopen("Cadenas.txt", "r");
    if(archivoCadenas == NULL) {
        perror("Error al abrir Cadenas.txt");
        exit(1);
    }

    // Procesar configuración del AFD
    numEstados = contarEstados(archivoConfig);
    mostrarAlfabeto(archivoConfig);
    estados = cargarEstados(archivoConfig, numEstados);

    mostrarTabla(estados, numEstados);

    verificarCadenas(estados, numEstados, archivoCadenas);

    free(estados);
    fclose(archivoConfig);
    fclose(archivoCadenas);

    return 0;
}

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

int buscarIndiceEstado(char nombreEstado, Estado* estados, int numEstados) {
    for(int i=0; i<numEstados; i++) {
        if(estados[i].nombre == nombreEstado) {
            return i;
        }
    }
    return -1;
}

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

        int idxFinal = buscarIndiceEstado(estadoActual, estados, numEstados);
        if(idxFinal != -1 && estados[idxFinal].tipo == '+') {
            printf("Cadena \"%s\" aceptada\n", cadena);
        } else {
            printf("Cadena \"%s\" no aceptada\n", cadena);
        }
    }
}

