class automata:
    
    def __init__(self):
        self.estado_inicial = 'q0'
        self.estados_finales = {'q0', 'q1', 'q2'}
        self.reset()
    
    def reset(self):
        self.estado_actual = self.estado_inicial
    
    def transicion(self, simbolo):
        if self.estado_actual == 'q0':
            if simbolo == 'a':
                return 'q0'
            elif simbolo == 'b':
                return 'q1'
            elif simbolo == 'c':
                return 'q2'
            else:
                return 'q3'
                
        elif self.estado_actual == 'q1':
            if simbolo == 'a':
                return 'q3'
            elif simbolo == 'b':
                return 'q1'
            elif simbolo == 'c':
                return 'q2'
            else:
                return 'q3'
                
        elif self.estado_actual == 'q2':
            if simbolo == 'a' or simbolo == 'b':
                return 'q3'
            elif simbolo == 'c':
                return 'q2'
            else:
                return 'q3'
                
        else:
            return 'q3'
    
    def procesar_cadena(self, cadena):
        self.reset()
        
        for simbolo in cadena:
            self.estado_actual = self.transicion(simbolo)
            if self.estado_actual == 'q3':
                return False
        
        return self.estado_actual in self.estados_finales


automata = automata()

casos_prueba = ["", "a", "b", "ba", "bb", "aba", "ab", "aaabbb", "c","abc"]

for cadena in casos_prueba:
    resultado = automata.procesar_cadena(cadena)
    cadena_mostrar = f'"{cadena}"' if cadena else '""'
    estado = "ACEPTA" if resultado else "NO ACEPTA"
    print(f"{cadena_mostrar}, {estado}")