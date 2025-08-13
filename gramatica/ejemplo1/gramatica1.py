import re
import sys

class GramaticaBNF:
    def __init__(self):
        
        # Patrón base: solo dígitos binarios (0 y 1)
        self.patron_binario = re.compile(r'^[01]+$')
        
        # Casos base de la gramática: S → 0 | 1
        self.casos_base = re.compile(r'^[01]$')
        
        # Captura primer dígito, contenido medio, y último dígito
        self.patron_estructura = re.compile(r'^([01])(.*?)([01])$')
    
    def validar_cadena(self, cadena):

        cadena = cadena.strip()
        
        if not cadena:
            return False
        
        if not self.patron_binario.match(cadena):
            return False
        
        # Aplicar reglas BNF recursivamente
        return self._aplicar_reglas_bnf(cadena)
    
    def _aplicar_reglas_bnf(self, cadena):
        # Caso base: S → 0 | 1 (usar regex)
        if self.casos_base.match(cadena):
            return True
        
        # Caso recursivo: S → 0S0 | 1S1
        match = self.patron_estructura.match(cadena)
        if not match:
            return False
        
        primer_digito = match.group(1)
        contenido_medio = match.group(2)
        ultimo_digito = match.group(3)
        
        if primer_digito != ultimo_digito:
            return False
        
        if not contenido_medio:
            return False
        
        # Recursión: validar el contenido medio
        return self._aplicar_reglas_bnf(contenido_medio)
    
    def procesar_archivo(self, nombre_archivo):
        try:
            with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
                lineas = archivo.readlines()
            
            for i, linea in enumerate(lineas, 1):
                cadena = linea.strip()
                if cadena:  # Solo procesar líneas no vacías
                    if self.validar_cadena(cadena):
                        print("ACEPTA")
                    else:
                        print("NO ACEPTA")
                        
        except FileNotFoundError:
            print(f"Error: No se encontró el archivo '{nombre_archivo}'")
        except Exception as e:
            print(f"Error al procesar el archivo: {e}")

def main():
    
    nombre_archivo = sys.argv[1]
    validador = GramaticaBNF()
    validador.procesar_archivo(nombre_archivo)

if __name__ == "__main__":
    main()
