class automata:
    def __init__(self):
        self.estados = {'q0', 'q1', 'qr'}
        self.estado_inicial = 'q0'
        self.estados_aceptacion = {'q1'}
        
        self.transiciones = {
            'q0': {
                'letra': 'q1',
                'digito': 'qr',
                'otro': 'qr'
            },
            'q1': {
                'letra': 'q1',
                'digito': 'q1',
                'otro': 'qr'
            },
            'qr': {
                'letra': 'qr',
                'digito': 'qr',
                'otro': 'qr'
            }
        }
    
    def es_letra(self, char):
        return char.isalpha()
    
    def es_digito(self, char):
        return char.isdigit()
    
    def tipo_caracter(self, char):
        if self.es_letra(char):
            return 'letra'
        elif self.es_digito(char):
            return 'digito'
        else:
            return 'otro'
    
    def procesar_cadena(self, cadena):
        if not cadena:
            return False,
        
        estado_actual = self.estado_inicial        
        for i, char in enumerate(cadena):
            tipo_char = self.tipo_caracter(char)
            estado_anterior = estado_actual
            estado_actual = self.transiciones[estado_actual][tipo_char]
                    
        aceptada = estado_actual in self.estados_aceptacion
        resultado = "ACEPTADA" if aceptada else "NO ACEPTADA"
        
        return aceptada
    
    def validar_id(self, cadena):
        aceptada = self.procesar_cadena(cadena)
        
        return aceptada

afd = automata()

casos_prueba = [
    "id",
    "cc1011",
    "ID7856",
    "7856ID",
    "id-848439"
]

for cadena in casos_prueba:
    resultado = afd.validar_id(cadena)
    status = "ACEPTADA" if resultado else "NO ACEPTADA"
    print(f"'{cadena}', {status}")