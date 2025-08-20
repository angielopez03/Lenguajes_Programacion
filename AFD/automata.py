class Estado:
    def __init__(self, tipo='', nombre='', destino0='', destino1=''):
        self.tipo = tipo
        self.nombre = nombre
        self.destino0 = destino0
        self.destino1 = destino1

def contar_estados(archivo_config):
    with open(archivo_config, 'r', encoding='utf-8') as archivo:
        contador = -1
        for linea in archivo:
            contador += 1
            if linea.strip().startswith('-'):
                break
    return contador

def mostrar_alfabeto(archivo_config):
    with open(archivo_config, 'r', encoding='utf-8') as archivo:
        # Buscar la línea que empieza con '-'
        for linea in archivo:
            if linea.strip().startswith('-'):
                break
        
        # La siguiente línea contiene el alfabeto
        alfabeto = archivo.readline().strip()
        print(f"Alfabeto: {alfabeto}")

def cargar_estados(archivo_config, num_estados):
    estados = []
    with open(archivo_config, 'r', encoding='utf-8') as archivo:
        for i in range(num_estados):
            linea = archivo.readline().rstrip('\n')  # Solo quitar salto de línea
            if len(linea) >= 4:
                tipo = linea[0] if linea[0] != ' ' else '-'  # Si es espacio, es estado normal
                nombre = linea[1]
                destino0 = linea[2]
                destino1 = linea[3]
                estados.append(Estado(tipo, nombre, destino0, destino1))
    return estados

def mostrar_tabla(estados):
    print("\nTabla de transiciones:")
    print("Tipo Estado  0   1")
    for estado in estados:
        print(f" [{estado.tipo}]   {estado.nombre}    {estado.destino0}   {estado.destino1}")
    print()

def buscar_indice_estado(nombre_estado, estados):
    for i, estado in enumerate(estados):
        if estado.nombre == nombre_estado:
            return i
    return -1

def buscar_estado_inicial(estados):
    for estado in estados:
        if estado.tipo == '>':
            return estado.nombre
    # Si no hay estado marcado como inicial, buscar uno que sea inicial Y de aceptación
    for estado in estados:
        if estado.tipo == '+':
            return estado.nombre
    return None

def verificar_cadenas(estados, archivo_cadenas):
    try:
        with open(archivo_cadenas, 'r', encoding='utf-8') as archivo:
            for linea in archivo:
                cadena = linea.strip()
                if not cadena:  # Saltar líneas vacías
                    continue
                
                # Buscar estado inicial
                estado_actual = buscar_estado_inicial(estados)
                
                if estado_actual is None:
                    print(f"Error: No se encontró estado inicial")
                    continue
                
                # Caso de cadena vacía (E)
                if cadena == 'E' or cadena == '':
                    idx = buscar_indice_estado(estado_actual, estados)
                    if idx != -1 and estados[idx].tipo == '+':
                        print(f'Cadena "{cadena}" aceptada (E)')
                    else:
                        print(f'Cadena "{cadena}" no aceptada')
                    continue
                
                # Procesar cada símbolo de la cadena
                for simbolo in cadena:
                    idx = buscar_indice_estado(estado_actual, estados)
                    if idx == -1:
                        break
                    
                    if simbolo == '0':
                        estado_actual = estados[idx].destino0
                    elif simbolo == '1':
                        estado_actual = estados[idx].destino1
                    else:
                        print(f'Error: Símbolo "{simbolo}" no reconocido en la cadena "{cadena}"')
                        break
                
                # Verificar si el estado final es de aceptación
                idx_final = buscar_indice_estado(estado_actual, estados)
                if idx_final != -1 and estados[idx_final].tipo == '+':
                    print(f'Cadena "{cadena}" aceptada')
                else:
                    print(f'Cadena "{cadena}" no aceptada')
    
    except FileNotFoundError:
        print(f"Error: No se pudo abrir el archivo {archivo_cadenas}")

def main():
    archivo_config = "Conf.txt"
    archivo_cadenas = "Cadenas.txt"
    
    try:
        # Procesar configuración del AFD
        num_estados = contar_estados(archivo_config)
        mostrar_alfabeto(archivo_config)
        estados = cargar_estados(archivo_config, num_estados)
        
        mostrar_tabla(estados)
        
        verificar_cadenas(estados, archivo_cadenas)
        
    except FileNotFoundError as e:
        print(f"Error al abrir archivo: {e}")
    except Exception as e:
        print(f"Error inesperado: {e}")

if __name__ == "__main__":
    main()
