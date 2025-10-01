producciones = [
    "S->A uno B C",
    "S->S dos",
    "A->B C D",
    "A->A tres",
    "A->ε",
    "B->D cuatro C tres",
    "B->ε",
    "C->cinco D B",
    "C->ε",
    "D->seis",
    "D->ε"
]

def parsear_produccion(produccion):
    if '->' in produccion:
        partes = produccion.split('->')
    else:
        partes = produccion.split('=')
    
    lado_izq = partes[0].strip()
    lado_der = partes[1].strip()
    
    if lado_der in ['ε', 'epsilon', '#', '']:
        return (lado_izq, ['ε'])
    
    simbolos = lado_der.split()
    return (lado_izq, simbolos)

def es_no_terminal(simbolo):
    return len(simbolo) == 1 and simbolo.isupper()

def es_terminal(simbolo):
    return simbolo != 'ε' and not es_no_terminal(simbolo)

def obtener_producciones(no_terminal, producciones_parseadas):
    return [(i, prod) for i, prod in enumerate(producciones_parseadas) if prod[0] == no_terminal]

def calcular_primeros_cadena(cadena, primeros_nt):
    if not cadena or cadena == ['ε']:
        return {'ε'}
    
    primeros = set()
    
    for i, simbolo in enumerate(cadena):
        if es_terminal(simbolo):
            primeros.add(simbolo)
            return primeros
        
        if simbolo in primeros_nt:
            primeros_simbolo = primeros_nt[simbolo]
        else:
            return set()
        primeros.update(primeros_simbolo - {'ε'})
        
        if 'ε' in primeros_simbolo:
            if i == len(cadena) - 1:
                primeros.add('ε')
        else:
            break
    
    return primeros

def calcular_primeros_no_terminales(producciones_parseadas):
    no_terminales = []
    for izq, _ in producciones_parseadas:
        if izq not in no_terminales:
            no_terminales.append(izq)
    
    primeros_nt = {}
    
    for nt in no_terminales:
        primeros_nt[nt] = set()
    
    cambios = True
    iteraciones = 0
    max_iter = 100
    
    while cambios and iteraciones < max_iter:
        cambios = False
        iteraciones += 1
        
        for nt in no_terminales:
            anterior = primeros_nt[nt].copy()
            
            for _, (lado_izq, lado_der) in obtener_producciones(nt, producciones_parseadas):
                
                if lado_der and es_no_terminal(lado_der[0]) and lado_der[0] == nt:
                    if 'ε' in primeros_nt[nt] and len(lado_der) > 1:
                        resto = lado_der[1:]
                        primeros_resto = calcular_primeros_cadena(resto, primeros_nt)
                        primeros_nt[nt].update(primeros_resto)
                else:
                    primeros_prod = calcular_primeros_cadena(lado_der, primeros_nt)
                    primeros_nt[nt].update(primeros_prod)
            
            if primeros_nt[nt] != anterior:
                cambios = True
    
    return primeros_nt


def calcular_siguientes(producciones_parseadas, primeros_nt, simbolo_inicial):
    no_terminales = []
    for izq, _ in producciones_parseadas:
        if izq not in no_terminales:
            no_terminales.append(izq)
    
    siguientes = {}
    for nt in no_terminales:
        siguientes[nt] = set()
    
    siguientes[simbolo_inicial].add('$')
    
    cambios = True
    iteraciones = 0
    max_iter = 100
    
    while cambios and iteraciones < max_iter:
        cambios = False
        iteraciones += 1
        
        for lado_izq, lado_der in producciones_parseadas:
            for i, simbolo in enumerate(lado_der):
                if not es_no_terminal(simbolo):
                    continue
                anterior = siguientes[simbolo].copy()
                
                if i + 1 < len(lado_der):
                    resto = lado_der[i + 1:]
                    primeros_resto = calcular_primeros_cadena(resto, primeros_nt)
                    
                    siguientes[simbolo].update(primeros_resto - {'ε'})
                    
                    if 'ε' in primeros_resto:
                        siguientes[simbolo].update(siguientes[lado_izq])
                else:
                    siguientes[simbolo].update(siguientes[lado_izq])
                
                if siguientes[simbolo] != anterior:
                    cambios = True
    
    return siguientes

def calcular_prediccion(lado_der, lado_izq, primeros_nt, siguientes):
    primeros_alfa = calcular_primeros_cadena(lado_der, primeros_nt)
    
    if 'ε' in primeros_alfa:
        return (primeros_alfa - {'ε'}) | siguientes.get(lado_izq, set())
    else:
        return primeros_alfa


def main():  
    producciones_parseadas = [parsear_produccion(p) for p in producciones]
    
    print("\nGRAMÁTICA:")
    for i, (izq, der) in enumerate(producciones_parseadas, 1):
        der_str = ' '.join(der)
        print(f"  {i}. {izq} → {der_str}")
    
    no_terminales = []
    for izq, _ in producciones_parseadas:
        if izq not in no_terminales:
            no_terminales.append(izq)
    
    simbolo_inicial = no_terminales[0]
    
    print("\n")
    print("    CONJUNTOS PRIMEROS:")
    
    primeros_nt = calcular_primeros_no_terminales(producciones_parseadas)
    
    for nt in no_terminales:
        primeros_list = sorted(list(primeros_nt[nt]))
        print(f"PRIMEROS({nt}) = {{ {', '.join(primeros_list)} }}")
    
    print("\n")
    print("    CONJUNTOS SIGUIENTES:")
    
    siguientes = calcular_siguientes(producciones_parseadas, primeros_nt, simbolo_inicial)
    
    for nt in no_terminales:
        siguientes_list = sorted(list(siguientes[nt]))
        print(f"SIGUIENTES({nt}) = {{ {', '.join(siguientes_list)} }}")
    
    print("\n")
    print("    CONJUNTOS DE PREDICCIÓN:")
    
    for i, (lado_izq, lado_der) in enumerate(producciones_parseadas, 1):
        pred = calcular_prediccion(lado_der, lado_izq, primeros_nt, siguientes)
        pred_list = sorted(list(pred))
        der_str = ' '.join(lado_der)
        print(f"PRED({i}. {lado_izq} → {der_str}) = {{ {', '.join(pred_list)} }}")
    
if __name__ == "__main__":
    main()