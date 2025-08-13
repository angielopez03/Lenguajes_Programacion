import re
import sys

class GramaticaBNF_G5_Detallado:
    def __init__(self):
        
        self.regla_S = re.compile(r'^(.+)b$')
        
        self.regla_A_base = re.compile(r'^a$')

        self.regla_A_recursiva = re.compile(r'^a(ab)+$')
        
        self.regla_A_completa = re.compile(r'^a(ab)*$')
        
        self.alfabeto_valido = re.compile(r'^[ab]+$')
        
        self.patron_completo = re.compile(r'^a(ab)*b$')
    
    def mostrar_analisis(self, cadena):      
        if not cadena:
            print("NO ACEPTA")
            return False
        
        if not self.alfabeto_valido.match(cadena):
            return False
        
        match_S = self.regla_S.match(cadena)
        if not match_S:
            print(f"NO ACEPTA")
            return False
        
        parte_A = match_S.group(1)
        
        if self.regla_A_base.match(parte_A):
            print(f"ACEPTA")
            return True
        elif self.regla_A_recursiva.match(parte_A):
            match_recursiva = re.match(r'^a(ab)+$', parte_A)
            if match_recursiva:
                repeticiones = len(match_recursiva.group(1)) // 2
                print(f"  - ACEPTA")
                return True
        
        print(f"NO ACEPTA")
        return False
    
    def validar_cadena(self, cadena):
        cadena = cadena.strip()
        return bool(self.patron_completo.match(cadena))
    
    def procesar_archivo(self, nombre_archivo, modo_detallado=False):
        try:
            with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
                for linea in archivo:
                    cadena = linea.strip()
                    if cadena:  # Solo procesar líneas no vacías
                        if modo_detallado:
                            resultado = self.mostrar_analisis(cadena)
                            print()
                        else:
                            if self.validar_cadena(cadena):
                                print("ACEPTA")
                            else:
                                print("NO ACEPTA")
                        
        except FileNotFoundError:
            print(f"Error: No se encontró el archivo '{nombre_archivo}'", file=sys.stderr)
            sys.exit(1)
        except Exception as e:
            print(f"Error al procesar el archivo: {e}", file=sys.stderr)
            sys.exit(1)

def main():
    nombre_archivo = sys.argv[1]
    modo_detallado = len(sys.argv) > 2 and sys.argv[2] == '-v'
    
    validador = GramaticaBNF_G5_Detallado()
    validador.procesar_archivo(nombre_archivo, modo_detallado)

if __name__ == "__main__":
    main()
