from dataclasses import dataclass
from typing import List, Dict, Set, Optional, Tuple, Any

producciones = [
    "E -> T E'",
    "E' -> + T E'",
    "E' -> - T E'",
    "E' -> ε",
    "T -> F T'",
    "T' -> * F T'",
    "T' -> / F T'",
    "T' -> ε",
    "F -> num",
    "F -> ( E )"
]

@dataclass
class Nodo:
    """Nodo del AST"""
    tipo: str
    valor: Any
    izq: Optional['Nodo'] = None
    der: Optional['Nodo'] = None
    atributos: Dict = None
    
    def __post_init__(self):
        if self.atributos is None:
            self.atributos = {}

@dataclass
class EntradaTabla:
    nombre: str
    tipo: str
    valor: Any
    direccion: Optional[int] = None

class TablaSimbolos:
    def __init__(self):
        self.tabla: Dict[str, EntradaTabla] = {}
        self.contador_temp = 0
        self.direccion_actual = 100
    
    def insertar(self, nombre: str, tipo: str, valor: Any) -> EntradaTabla:
        if nombre not in self.tabla:
            entrada = EntradaTabla(
                nombre=nombre,
                tipo=tipo,
                valor=valor,
                direccion=self.direccion_actual if tipo == 'temporal' else None
            )
            self.tabla[nombre] = entrada
            if tipo == 'temporal':
                self.direccion_actual += 4
            return entrada
        else:
            return self.tabla[nombre]
    
    def nueva_temporal(self) -> str:
        self.contador_temp += 1
        nombre = f"t{self.contador_temp}"
        return nombre
    
    def buscar(self, nombre: str) -> Optional[EntradaTabla]:
        return self.tabla.get(nombre)
    
    def imprimir(self):
        print(f"\n")
        print("TABLA DE SÍMBOLOS")
        print(f"{'Nombre':<12} {'Tipo':<12} {'Valor':<10} {'Dirección':<12}")
        print("-"*50)
        for entrada in self.tabla.values():
            dir_str = str(entrada.direccion) if entrada.direccion else '-'
            print(f"{entrada.nombre:<12} {entrada.tipo:<12} {entrada.valor:<10} {dir_str:<12}")

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
    if not simbolo or simbolo == 'ε':
        return False
    return (len(simbolo) == 1 and simbolo.isupper()) or simbolo.endswith("'")

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
    
    primeros_nt = {nt: set() for nt in no_terminales}
    
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
    
    siguientes = {nt: set() for nt in no_terminales}
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


class GeneradorCodigo:
    def __init__(self):
        self.codigo = []
    
    def generar(self, instruccion: str):
        self.codigo.append(instruccion)
    
    def imprimir(self):
        print("\n")
        print("CÓDIGO INTERMEDIO (Tres Direcciones)")
        for i, instr in enumerate(self.codigo, 1):
            print(f"{i:3}. {instr}")

def construir_ast_simple(expresion: str, tabla: TablaSimbolos, generador: GeneradorCodigo) -> Nodo:
    tokens = expresion.replace('(', ' ( ').replace(')', ' ) ').split()
    pos = [0]
    
    def es_numero(s):
        try:
            float(s)
            return True
        except:
            return False
    
    def parsear_E():
        nodo_T = parsear_T()
        return parsear_E_prima(nodo_T)
    
    def parsear_E_prima(heredado):
        if pos[0] < len(tokens) and tokens[pos[0]] in ['+', '-']:
            op = tokens[pos[0]]
            pos[0] += 1
            
            nodo_T = parsear_T()
            
            temp = tabla.nueva_temporal()
            val_izq = heredado.atributos.get('val', heredado.valor)
            val_der = nodo_T.atributos.get('val', nodo_T.valor)
            
            if es_numero(str(val_izq)) and es_numero(str(val_der)):
                if op == '+':
                    resultado = float(val_izq) + float(val_der)
                else:
                    resultado = float(val_izq) - float(val_der)
            else:
                resultado = temp
            
            tabla.insertar(temp, 'temporal', resultado)
            generador.generar(f"{temp} := {val_izq} {op} {val_der}")
            
            nodo_op = Nodo('OP', op, heredado, nodo_T)
            nodo_op.atributos['val'] = resultado
            nodo_op.atributos['temp'] = temp
            
            return parsear_E_prima(nodo_op)
        
        return heredado
    
    def parsear_T():
        nodo_F = parsear_F()
        return parsear_T_prima(nodo_F)
    
    def parsear_T_prima(heredado):
        if pos[0] < len(tokens) and tokens[pos[0]] in ['*', '/']:
            op = tokens[pos[0]]
            pos[0] += 1
            
            nodo_F = parsear_F()
            
            temp = tabla.nueva_temporal()
            val_izq = heredado.atributos.get('val', heredado.valor)
            val_der = nodo_F.atributos.get('val', nodo_F.valor)
            
            if es_numero(str(val_izq)) and es_numero(str(val_der)):
                if op == '*':
                    resultado = float(val_izq) * float(val_der)
                else:
                    resultado = float(val_izq) / float(val_der) if float(val_der) != 0 else 'ERROR'
            else:
                resultado = temp
            
            tabla.insertar(temp, 'temporal', resultado)
            generador.generar(f"{temp} := {val_izq} {op} {val_der}")
            
            nodo_op = Nodo('OP', op, heredado, nodo_F)
            nodo_op.atributos['val'] = resultado
            nodo_op.atributos['temp'] = temp
            
            return parsear_T_prima(nodo_op)
        
        return heredado
    
    def parsear_F():
        if pos[0] < len(tokens):
            token = tokens[pos[0]]
            
            if token == '(':
                pos[0] += 1
                nodo = parsear_E()
                if pos[0] < len(tokens) and tokens[pos[0]] == ')':
                    pos[0] += 1
                return nodo
            
            elif es_numero(token):
                pos[0] += 1
                valor = float(token)
                tabla.insertar(f"_const{token}", 'constante', valor)
                nodo = Nodo('NUM', valor)
                nodo.atributos['val'] = valor
                return nodo
        
        raise Exception("Error de sintaxis")
    
    return parsear_E()

def imprimir_ast(nodo: Nodo, nivel: int = 0, prefijo: str = ""):
    if nodo is None:
        return
    
    indent = "  " * nivel
    
    if nodo.tipo == 'NUM':
        print(f"{indent}{prefijo}[NUM: {nodo.valor}]")
        print(f"{indent}  └─ val = {nodo.atributos.get('val', nodo.valor)}")
    elif nodo.tipo == 'OP':
        print(f"{indent}{prefijo}[OP: {nodo.valor}]")
        print(f"{indent}  ├─ val = {nodo.atributos.get('val', '?')}")
        if 'temp' in nodo.atributos:
            print(f"{indent}  ├─ temp = {nodo.atributos['temp']}")
        print(f"{indent}  ├─ hijo_izq:")
        imprimir_ast(nodo.izq, nivel + 2, "")
        print(f"{indent}  └─ hijo_der:")
        imprimir_ast(nodo.der, nivel + 2, "")


def imprimir_gramatica_atributos():
    print("\n")
    print("GRAMÁTICA DE ATRIBUTOS")

    reglas = [
        ("E → T E'", [
            "E'.inh := T.val",
            "E.val := E'.val"
        ]),
        ("E' → + T E'₁", [
            "temp := nueva_temporal()",
            "temp.val := E'.inh + T.val",
            "insertar_tabla(temp)",
            "E'₁.inh := temp.val",
            "generar(temp || ' := ' || E'.inh || ' + ' || T.val)",
            "E'.val := E'₁.val"
        ]),
        ("E' → - T E'₁", [
            "temp := nueva_temporal()",
            "temp.val := E'.inh - T.val",
            "insertar_tabla(temp)",
            "E'₁.inh := temp.val",
            "generar(temp || ' := ' || E'.inh || ' - ' || T.val)",
            "E'.val := E'₁.val"
        ]),
        ("E' → ε", [
            "E'.val := E'.inh"
        ]),
        ("T → F T'", [
            "T'.inh := F.val",
            "T.val := T'.val"
        ]),
        ("T' → * F T'₁", [
            "temp := nueva_temporal()",
            "temp.val := T'.inh * F.val",
            "insertar_tabla(temp)",
            "T'₁.inh := temp.val",
            "generar(temp || ' := ' || T'.inh || ' * ' || F.val)",
            "T'.val := T'₁.val"
        ]),
        ("T' → / F T'₁", [
            "temp := nueva_temporal()",
            "temp.val := T'.inh / F.val",
            "insertar_tabla(temp)",
            "T'₁.inh := temp.val",
            "generar(temp || ' := ' || T'.inh || ' / ' || F.val)",
            "T'.val := T'₁.val"
        ]),
        ("T' → ε", [
            "T'.val := T'.inh"
        ]),
        ("F → num", [
            "F.val := num.valor",
            "insertar_tabla(num)"
        ]),
        ("F → ( E )", [
            "F.val := E.val"
        ])
    ]
    
    for prod, acciones in reglas:
        print(f"\n{prod}")
        for accion in acciones:
            print(f"    {{ {accion} }}")
    

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
    print("PRIMEROS:")
    primeros_nt = calcular_primeros_no_terminales(producciones_parseadas)
    
    for nt in no_terminales:
        primeros_list = sorted(list(primeros_nt[nt]))
        print(f"({nt:3}) = {{ {', '.join(primeros_list)} }}")
    
    print("\n")
    print("SIGUIENTES:")
    siguientes = calcular_siguientes(producciones_parseadas, primeros_nt, simbolo_inicial)
    
    for nt in no_terminales:
        siguientes_list = sorted(list(siguientes[nt]))
        print(f"({nt:3}) = {{ {', '.join(siguientes_list)} }}")
    
    print("\n")
    print("PREDICCIÓN:")
    for i, (lado_izq, lado_der) in enumerate(producciones_parseadas, 1):
        pred = calcular_prediccion(lado_der, lado_izq, primeros_nt, siguientes)
        pred_list = sorted(list(pred))
        der_str = ' '.join(lado_der)
        print(f"{i:2}. {lado_izq} → {der_str:15}) = {{ {', '.join(pred_list)} }}")
    
    imprimir_gramatica_atributos()
    
    ruta_archivo = "entrada.txt"

    try:
        with open(ruta_archivo, "r") as f:
            expresion = f.read().strip()
        print(f"\nEJEMPLO DE TRADUCCIÓN: {expresion}")
    except Exception as e:
        print(f"Error al leer el archivo de entrada: {e}")
        return

    tabla = TablaSimbolos()
    generador = GeneradorCodigo()
    
    try:
        ast = construir_ast_simple(expresion, tabla, generador)
        
        print("\nAST DECORADO:")
        imprimir_ast(ast)
        
        tabla.imprimir()
        generador.imprimir()
        
        resultado_final = ast.atributos.get('val', '?')
        print(f"\n")
        print(f"RESULTADO FINAL: {expresion} = {resultado_final}")
        
    except Exception as e:
        print(f"Error al procesar la expresión: {e}")
    
    print("\n")
    print("ESQUEMA DE TRADUCCIÓN DIRIGIDO POR SINTAXIS (EDTS)")
    print("""
E → T { E'.inh := T.val } 
    E' { E.val := E'.val }

E' → + { temp := nueva_temporal() } 
     T { temp.val := E'.inh + T.val }
       { insertar_tabla(temp) }
       { E'₁.inh := temp.val }
       { generar(temp || " := " || E'.inh || " + " || T.val) }
     E'₁ { E'.val := E'₁.val }

E' → - { temp := nueva_temporal() } 
     T { temp.val := E'.inh - T.val }
       { insertar_tabla(temp) }
       { E'₁.inh := temp.val }
       { generar(temp || " := " || E'.inh || " - " || T.val) }
     E'₁ { E'.val := E'₁.val }

E' → ε { E'.val := E'.inh }

T → F { T'.inh := F.val } 
    T' { T.val := T'.val }

T' → * { temp := nueva_temporal() } 
     F { temp.val := T'.inh * F.val }
       { insertar_tabla(temp) }
       { T'₁.inh := temp.val }
       { generar(temp || " := " || T'.inh || " * " || F.val) }
     T'₁ { T'.val := T'₁.val }

T' → / { temp := nueva_temporal() } 
     F { temp.val := T'.inh / F.val }
       { insertar_tabla(temp) }
       { T'₁.inh := temp.val }
       { generar(temp || " := " || T'.inh || " / " || F.val) }
     T'₁ { T'.val := T'₁.val }

T' → ε { T'.val := T'.inh }

F → num { F.val := num.valor }
        { insertar_tabla(num) }

F → ( E ) { F.val := E.val }
    """)
    

if __name__ == "__main__":
    main()

