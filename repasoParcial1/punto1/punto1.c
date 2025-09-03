#include <stdio.h>
#include <ctype.h>

#define TAMANO_MAXIMO 256  // tamaño máximo de un lexema (token)

int main(int cantidadArgumentos, char *argumentos[]) {
    if (cantidadArgumentos != 2) {
        fprintf(stderr, "Uso: %s archivo.txt\n", argumentos[0]);
        return 1;
    }

    FILE *archivo = fopen(argumentos[1], "r");
    if (!archivo) {
        perror("No se pudo abrir el archivo");
        return 1;
    }

    int caracter;
    while ((caracter = fgetc(archivo)) != EOF) {
        if (isspace(caracter)) continue; // saltar espacios y saltos de línea

        // Caso: suma o incremento
        if (caracter == '+') {
            int siguienteCaracter = fgetc(archivo);
            if (siguienteCaracter == '+') {
                printf("INCR\t++\n");
            } else {
                if (siguienteCaracter != EOF) ungetc(siguienteCaracter, archivo);
                printf("SUMA\t+\n");
            }
            continue;
        }

        // Caso: número
        if (isdigit(caracter)) {
            char lexema[TAMANO_MAXIMO];
            int indice = 0;
            lexema[indice++] = (char)caracter;

            // seguir leyendo mientras sean dígitos
            while ((caracter = fgetc(archivo)) != EOF && isdigit(caracter) && indice < TAMANO_MAXIMO-1) {
                lexema[indice++] = (char)caracter;
            }

            // verificar si hay un punto
            if (caracter == '.') {
                int siguienteCaracter = fgetc(archivo);
                if (siguienteCaracter != EOF && isdigit(siguienteCaracter)) {
                    // es REAL
                    lexema[indice++] = '.';
                    lexema[indice++] = (char)siguienteCaracter;

                    while ((caracter = fgetc(archivo)) != EOF && isdigit(caracter) && indice < TAMANO_MAXIMO-1) {
                        lexema[indice++] = (char)caracter;
                    }
                    lexema[indice] = '\0';
                    if (caracter != EOF) ungetc(caracter, archivo);
                    printf("REAL\t%s\n", lexema);
                } else {
                    if (siguienteCaracter != EOF) ungetc(siguienteCaracter, archivo);
                    ungetc('.', archivo);
                    lexema[indice] = '\0';
                    printf("ENTERO\t%s\n", lexema);
                }
            } else {
                if (caracter != EOF) ungetc(caracter, archivo);
                lexema[indice] = '\0';
                printf("ENTERO\t%s\n", lexema);
            }
            continue;
        }

        // Caso: error (símbolo no reconocido)
        {
            char lexema[TAMANO_MAXIMO];
            int indice = 0;
            lexema[indice++] = (char)caracter;

            while ((caracter = fgetc(archivo)) != EOF && !isspace(caracter) && caracter != '+' && !isdigit(caracter) && indice < TAMANO_MAXIMO-1) {
                lexema[indice++] = (char)caracter;
            }
            if (caracter != EOF) ungetc(caracter, archivo);
            lexema[indice] = '\0';
            printf("ERROR\t%s\n", lexema);
        }
    }

    fclose(archivo);
    return 0;
}
