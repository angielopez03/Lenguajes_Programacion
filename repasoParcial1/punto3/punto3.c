#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[]) {
    if (argc != 3) {
        printf("Uso: %s archivo palabra_clave\n", argv[0]);
        return 1;
    }

    char *nombreArchivo = argv[1];
    char *palabraClave = argv[2];
    FILE *archivo = fopen(nombreArchivo, "r");

    if (!archivo) {
        perror("Error al abrir el archivo");
        return 1;
    }

    char linea[1024];  // buffer para leer líneas del archivo
    int contador = 0;

    // leer el archivo línea por línea
    while (fgets(linea, sizeof(linea), archivo)) {
        char *ptr = linea;

        // buscar ocurrencias de la palabra clave en la línea
        while ((ptr = strstr(ptr, palabraClave)) != NULL) {
            contador++;
            ptr += strlen(palabraClave); // avanzar para evitar bucles infinitos
        }
    }

    fclose(archivo);

    printf("%s se repite %d veces en el texto.\n", palabraClave, contador);
    return 0;
}

