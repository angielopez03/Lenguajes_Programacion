import re
import sys

class GramaticaBNF_G2:
    def __init__(self):
        self.patron_ab = re.compile(r'^[ab]+$')
        
        self.patron_estructura = re.compile(r'^(a*)(b+)$')
    
    def validar_cadena(self, cadena):
        cadena = cadena.strip()
        
        if not cadena:
            return False
        
        if not self.patron_ab.match(cadena):
            return False
        
        # Extraer grupos de 'a's y 'b's
        match = self.patron_estructura.match(cadena)
        if not match:
            return False
        
        grupo_as = match.group(1)  # grupo de 'a's
        grupo_bs = match.group(2)  # grupo de 'b's
        
        num_as = len(grupo_as)
        num_bs = len(grupo_bs)
        
        # Verificar la relación: num_bs = num_as + 1
        return num_bs == num_as + 1
    
    def procesar_archivo(self, nombre_archivo):
        try:
            with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
                lineas = archivo.readlines()
            
            for linea in lineas:
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
    validador = GramaticaBNF_G2()
    validador.procesar_archivo(nombre_archivo)

if __name__ == "__main__":
    main()
