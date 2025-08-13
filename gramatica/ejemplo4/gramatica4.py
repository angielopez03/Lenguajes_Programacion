import re
import sys

class GramaticaBNF_G4:
    def __init__(self):

        self.patron_valido = re.compile(r'^(ab|abb)$')
    
    def validar_cadena(self, cadena):
        cadena = cadena.strip()
        
        if not cadena:
            return False
        
        return self.patron_valido.match(cadena) is not None
    
    def procesar_archivo(self, nombre_archivo):
        """
        Procesa un archivo de texto validando cada línea
        """
        try:
            with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
                lineas = archivo.readlines()
            
            for linea in lineas:
                cadena = linea.strip()
                if cadena:  # Solo procesar líneas no vacías
                    if self.validar_cadena(cadena):
                        print("ACEPTO")
                    else:
                        print("NO ACEPTO")
                        
        except FileNotFoundError:
            print(f"Error: No se encontró el archivo '{nombre_archivo}'")
        except Exception as e:
            print(f"Error al procesar el archivo: {e}")

def main():
    if len(sys.argv) != 2:
        print("Uso: python script.py archivo.txt")
        return
    
    nombre_archivo = sys.argv[1]
    validador = GramaticaBNF_G4()
    validador.procesar_archivo(nombre_archivo)

if __name__ == "__main__":
    main()
