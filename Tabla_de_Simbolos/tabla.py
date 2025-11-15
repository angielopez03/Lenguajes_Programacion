from dataclasses import dataclass
from typing import List, Dict, Optional, Any
import sys

@dataclass
class Nodo:
    """Nodo del AST"""
    tipo: str
    valor: Any
    hijos: List['Nodo'] = None
    atributos: Dict = None
    
    def __post_init__(self):
        if self.hijos is None:
            self.hijos = []
        if self.atributos is None:
            self.atributos = {}

@dataclass
class EntradaTabla:
    nombre: str
    tipo: str
    valor: Any
    ambito: str
    direccion: Optional[int] = None

class TablaSimbolos:
    def __init__(self):
        self.tabla: Dict[str, EntradaTabla] = {}
        self.contador_temp = 0
        self.contador_label = 0
        self.direccion_actual = 100
        self.ambito_actual = "global"
        self.pila_ambitos = ["global"]
    
    def insertar(self, nombre: str, tipo: str, valor: Any = None) -> EntradaTabla:
        clave = f"{self.ambito_actual}.{nombre}"
        if clave not in self.tabla:
            entrada = EntradaTabla(
                nombre=nombre,
                tipo=tipo,
                valor=valor,
                ambito=self.ambito_actual,
                direccion=self.direccion_actual if tipo in ['temporal', 'variable'] else None
            )
            self.tabla[clave] = entrada
            if tipo in ['temporal', 'variable']:
                self.direccion_actual += 4
            return entrada
        return self.tabla[clave]
    
    def nueva_temporal(self) -> str:
        self.contador_temp += 1
        nombre = f"t{self.contador_temp}"
        return nombre
    
    def nueva_etiqueta(self) -> str:
        self.contador_label += 1
        return f"L{self.contador_label}"
    
    def buscar(self, nombre: str) -> Optional[EntradaTabla]:
        clave = f"{self.ambito_actual}.{nombre}"
        if clave in self.tabla:
            return self.tabla[clave]
        clave_global = f"global.{nombre}"
        return self.tabla.get(clave_global)
    
    def entrar_ambito(self, nombre: str):
        self.pila_ambitos.append(nombre)
        self.ambito_actual = nombre
    
    def salir_ambito(self):
        if len(self.pila_ambitos) > 1:
            self.pila_ambitos.pop()
            self.ambito_actual = self.pila_ambitos[-1]
    
    def imprimir(self):
        print("\n")
        print("TABLA DE SÍMBOLOS")
        print(f"{'Nombre':<15} {'Tipo':<15} {'Ámbito':<15} {'Valor':<10} {'Dirección':<10}")
        print("-"*70)
        for entrada in self.tabla.values():
            dir_str = str(entrada.direccion) if entrada.direccion else '-'
            val_str = str(entrada.valor)[:8] if entrada.valor else '-'
            print(f"{entrada.nombre:<15} {entrada.tipo:<15} {entrada.ambito:<15} {val_str:<10} {dir_str:<10}")

class GeneradorCodigo:
    def __init__(self):
        self.codigo = []
    
    def generar(self, instruccion: str):
        self.codigo.append(instruccion)
    
    def imprimir(self):
        print("\n")
        print("CÓDIGO INTERMEDIO (Tres Direcciones)")
        for i, instr in enumerate(self.codigo, 1):
            print(f"{i:4}. {instr}")

class TraductorPython:
    def __init__(self):
        self.tabla = TablaSimbolos()
        self.generador = GeneradorCodigo()
        self.tokens = []
        self.pos = 0
    
    def token_actual(self):
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        return None
    
    def avanzar(self):
        self.pos += 1
    
    def tokenizar_expresion(self, expresion: str):
        """Tokeniza una expresión directamente desde texto"""
        tokens = []
        i = 0
        
        while i < len(expresion):
            ch = expresion[i]
            
            if ch.isspace():
                i += 1
                continue
            
            if ch.isalpha() or ch == '_':
                inicio = i
                while i < len(expresion) and (expresion[i].isalnum() or expresion[i] == '_'):
                    i += 1
                lexema = expresion[inicio:i]
                
                if lexema in ['True', 'False', 'None', 'if', 'else', 'while', 'for', 'in', 'and', 'or', 'not']:
                    tokens.append({"tipo": lexema, "lexema": lexema})
                else:
                    tokens.append({"tipo": "id", "lexema": lexema})
                continue
            
            if ch.isdigit():
                inicio = i
                while i < len(expresion) and expresion[i].isdigit():
                    i += 1
                lexema = expresion[inicio:i]
                tokens.append({"tipo": "tk_entero", "lexema": lexema})
                continue
            
            if ch in ['"', "'"]:
                comilla = ch
                i += 1
                inicio = i
                while i < len(expresion) and expresion[i] != comilla:
                    i += 1
                lexema = expresion[inicio:i]
                tokens.append({"tipo": "tk_cadena", "lexema": lexema})
                i += 1  # consumir comilla de cierre
                continue
            
            if i + 1 < len(expresion):
                dos_char = expresion[i:i+2]
                if dos_char == '==':
                    tokens.append({"tipo": "tk_igual", "lexema": "=="})
                    i += 2
                    continue
                elif dos_char == '!=':
                    tokens.append({"tipo": "tk_distinto", "lexema": "!="})
                    i += 2
                    continue
                elif dos_char == '>=':
                    tokens.append({"tipo": "tk_mayor_igual", "lexema": ">="})
                    i += 2
                    continue
                elif dos_char == '<=':
                    tokens.append({"tipo": "tk_menor_igual", "lexema": "<="})
                    i += 2
                    continue
                elif dos_char == '->':
                    tokens.append({"tipo": "tk_ejecuta", "lexema": "->"})
                    i += 2
                    continue
            
            simbolos = {
                '(': 'tk_par_izq', ')': 'tk_par_der',
                '[': 'tk_cua_izq', ']': 'tk_cua_der',
                ':': 'tk_dos_puntos', ',': 'tk_coma',
                '.': 'tk_punto', '=': 'tk_asig',
                '+': 'tk_suma', '-': 'tk_resta',
                '*': 'tk_mul', '/': 'tk_div',
                '%': 'tk_mod', '>': 'tk_mayor',
                '<': 'tk_menor'
            }
            
            if ch in simbolos:
                tokens.append({"tipo": simbolos[ch], "lexema": ch})
                i += 1
                continue
            
            i += 1
        
        tokens.append({"tipo": "$", "lexema": "$"})
        return tokens
    
    def traducir_expresion(self):
        """E → T E'"""
        nodo_T = self.traducir_termino()
        return self.traducir_expresion_prima(nodo_T)
    
    def traducir_expresion_prima(self, heredado):
        """E' → + T E' | - T E' | ε"""
        token = self.token_actual()
        
        if token and token["tipo"] in ["tk_suma", "tk_resta"]:
            op = token["lexema"] if token["lexema"] in ["+", "-"] else ("+" if token["tipo"] == "tk_suma" else "-")
            self.avanzar()
            
            nodo_T = self.traducir_termino()
            
            temp = self.tabla.nueva_temporal()
            val_izq = heredado.atributos.get('lugar', heredado.valor)
            val_der = nodo_T.atributos.get('lugar', nodo_T.valor)
            
            self.tabla.insertar(temp, 'temporal')
            self.generador.generar(f"{temp} := {val_izq} {op} {val_der}")
            
            nodo_op = Nodo('BINOP', op, [heredado, nodo_T])
            nodo_op.atributos['lugar'] = temp
            
            return self.traducir_expresion_prima(nodo_op)
        
        return heredado
    
    def traducir_termino(self):
        """T → F T'"""
        nodo_F = self.traducir_factor()
        return self.traducir_termino_prima(nodo_F)
    
    def traducir_termino_prima(self, heredado):
        """T' → * F T' | / F T' | % F T' | ε"""
        token = self.token_actual()
        
        if token and token["tipo"] in ["tk_mul", "tk_div", "tk_mod"]:
            op_map = {"tk_mul": "*", "tk_div": "/", "tk_mod": "%"}
            op = op_map.get(token["tipo"], token["lexema"])
            self.avanzar()
            
            nodo_F = self.traducir_factor()
            
            temp = self.tabla.nueva_temporal()
            val_izq = heredado.atributos.get('lugar', heredado.valor)
            val_der = nodo_F.atributos.get('lugar', nodo_F.valor)
            
            self.tabla.insertar(temp, 'temporal')
            self.generador.generar(f"{temp} := {val_izq} {op} {val_der}")
            
            nodo_op = Nodo('BINOP', op, [heredado, nodo_F])
            nodo_op.atributos['lugar'] = temp
            
            return self.traducir_termino_prima(nodo_op)
        
        return heredado
    
    def traducir_factor(self):
        """F → (E) | num | cadena | True | False | None | id"""
        token = self.token_actual()
        
        if not token:
            raise Exception("Error: token inesperado")
        
        if token["tipo"] == "tk_par_izq":
            self.avanzar()
            nodo = self.traducir_expresion()
            if self.token_actual() and self.token_actual()["tipo"] == "tk_par_der":
                self.avanzar()
            return nodo
        
        elif token["tipo"] == "tk_entero":
            valor = token["lexema"]
            self.avanzar()
            self.tabla.insertar(f"_const_{valor}", 'constante', valor)
            nodo = Nodo('NUM', valor)
            nodo.atributos['lugar'] = valor
            return nodo
        
        elif token["tipo"] == "tk_cadena":
            valor = token["lexema"]
            self.avanzar()
            self.tabla.insertar(f"_str_{len(valor)}", 'constante', valor)
            nodo = Nodo('STRING', valor)
            nodo.atributos['lugar'] = f'"{valor}"'
            return nodo
        
        elif token["tipo"] in ["True", "False", "None"]:
            valor = token["tipo"]
            self.avanzar()
            nodo = Nodo('CONST', valor)
            nodo.atributos['lugar'] = valor
            return nodo
        
        elif token["tipo"] == "id":
            nombre = token["lexema"]
            self.avanzar()
            
            if self.token_actual() and self.token_actual()["tipo"] == "tk_par_izq":
                return self.traducir_llamada(nombre)
            
            if self.token_actual() and self.token_actual()["tipo"] == "tk_cua_izq":
                self.avanzar()  # consumir '['
                indice = self.traducir_expresion()
                if self.token_actual() and self.token_actual()["tipo"] == "tk_cua_der":
                    self.avanzar()
                
                temp = self.tabla.nueva_temporal()
                self.tabla.insertar(temp, 'temporal')
                lugar_indice = indice.atributos.get('lugar', indice.valor)
                self.generador.generar(f"{temp} := {nombre}[{lugar_indice}]")
                
                nodo = Nodo('INDEX', f"{nombre}[]", [Nodo('ID', nombre), indice])
                nodo.atributos['lugar'] = temp
                return nodo
            
            entrada = self.tabla.buscar(nombre)
            if not entrada:
                self.tabla.insertar(nombre, 'variable')
            
            nodo = Nodo('ID', nombre)
            nodo.atributos['lugar'] = nombre
            return nodo
        
        elif token["tipo"] == "tk_cua_izq":
            self.avanzar()
            elementos = []
            
            if self.token_actual() and self.token_actual()["tipo"] != "tk_cua_der":
                elem = self.traducir_expresion()
                elementos.append(elem)
                
                while self.token_actual() and self.token_actual()["tipo"] == "tk_coma":
                    self.avanzar()
                    elem = self.traducir_expresion()
                    elementos.append(elem)
            
            if self.token_actual() and self.token_actual()["tipo"] == "tk_cua_der":
                self.avanzar()
            
            temp = self.tabla.nueva_temporal()
            self.tabla.insertar(temp, 'temporal')
            
            self.generador.generar(f"{temp} := new_list({len(elementos)})")
            for i, elem in enumerate(elementos):
                lugar_elem = elem.atributos.get('lugar', elem.valor)
                self.generador.generar(f"{temp}[{i}] := {lugar_elem}")
            
            nodo = Nodo('LIST', '[]', elementos)
            nodo.atributos['lugar'] = temp
            return nodo
        
        raise Exception(f"Error: factor no reconocido - {token}")
    
    def traducir_llamada(self, nombre):
        """Traduce llamadas a funciones"""
        self.avanzar()  # consumir '('
        
        args = []
        if self.token_actual() and self.token_actual()["tipo"] != "tk_par_der":
            arg = self.traducir_expresion()
            args.append(arg.atributos.get('lugar', arg.valor))
            
            while self.token_actual() and self.token_actual()["tipo"] == "tk_coma":
                self.avanzar()
                arg = self.traducir_expresion()
                args.append(arg.atributos.get('lugar', arg.valor))
        
        if self.token_actual() and self.token_actual()["tipo"] == "tk_par_der":
            self.avanzar()
        
        for i, arg in enumerate(args):
            self.generador.generar(f"param {arg}")
        
        temp = self.tabla.nueva_temporal()
        self.tabla.insertar(temp, 'temporal')
        self.generador.generar(f"{temp} := call {nombre}, {len(args)}")
        
        nodo = Nodo('CALL', nombre, [Nodo('ARG', a) for a in args])
        nodo.atributos['lugar'] = temp
        return nodo
    
    def traducir_asignacion(self, nombre):
        """id := expresion"""
        self.avanzar()  # consumir '='
        
        nodo_expr = self.traducir_expresion()
        lugar_expr = nodo_expr.atributos.get('lugar', nodo_expr.valor)
        
        # insertar variable si no existe
        entrada = self.tabla.buscar(nombre)
        if not entrada:
            self.tabla.insertar(nombre, 'variable')
        
        self.generador.generar(f"{nombre} := {lugar_expr}")
        
        nodo = Nodo('ASSIGN', '=', [Nodo('ID', nombre), nodo_expr])
        nodo.atributos['lugar'] = nombre
        return nodo
    
    def traducir_condicion(self):
        """Traduce expresiones relacionales y lógicas"""
        nodo_izq = self.traducir_expresion()
        
        token = self.token_actual()
        
        if token and token["tipo"] in ["and", "or"]:
            op = token["tipo"]
            self.avanzar()
            nodo_der = self.traducir_condicion()
            
            temp = self.tabla.nueva_temporal()
            val_izq = nodo_izq.atributos.get('lugar', nodo_izq.valor)
            val_der = nodo_der.atributos.get('lugar', nodo_der.valor)
            
            self.tabla.insertar(temp, 'temporal')
            self.generador.generar(f"{temp} := {val_izq} {op} {val_der}")
            
            nodo = Nodo('LOGOP', op, [nodo_izq, nodo_der])
            nodo.atributos['lugar'] = temp
            return nodo
        
        if token and token["tipo"] in ["tk_mayor", "tk_menor", "tk_igual", "tk_distinto", "tk_mayor_igual", "tk_menor_igual"]:
            op_map = {
                "tk_mayor": ">", "tk_menor": "<", "tk_igual": "==",
                "tk_distinto": "!=", "tk_mayor_igual": ">=", "tk_menor_igual": "<="
            }
            op = op_map.get(token["tipo"], token["lexema"])
            self.avanzar()
            
            nodo_der = self.traducir_expresion()
            
            temp = self.tabla.nueva_temporal()
            val_izq = nodo_izq.atributos.get('lugar', nodo_izq.valor)
            val_der = nodo_der.atributos.get('lugar', nodo_der.valor)
            
            self.tabla.insertar(temp, 'temporal')
            self.generador.generar(f"{temp} := {val_izq} {op} {val_der}")
            
            nodo = Nodo('RELOP', op, [nodo_izq, nodo_der])
            nodo.atributos['lugar'] = temp
            return nodo
        
        return nodo_izq

def imprimir_ast(nodo: Nodo, nivel: int = 0, prefijo: str = ""):
    """Imprime el AST de forma visual"""
    if nodo is None:
        return
    
    indent = "  " * nivel
    
    print(f"{indent}{prefijo}[{nodo.tipo}: {nodo.valor}]")
    
    if 'lugar' in nodo.atributos:
        print(f"{indent}  └─ lugar = {nodo.atributos['lugar']}")
    
    for i, hijo in enumerate(nodo.hijos):
        es_ultimo = (i == len(nodo.hijos) - 1)
        prefijo_hijo = "└─ " if es_ultimo else "├─ "
        imprimir_ast(hijo, nivel + 1, prefijo_hijo)

def imprimir_gramatica_atributos():
    """Imprime el ETDS completo"""
    print("ESQUEMA DE TRADUCCIÓN DIRIGIDO POR SINTAXIS (ETDS)")
    
    gramatica = """
E → T { E'.inh := T.lugar } 
    E' { E.lugar := E'.lugar }

E' → + T { temp := nueva_temporal() }
          { insertar_tabla(temp, 'temporal') }
          { generar(temp || ' := ' || E'.inh || ' + ' || T.lugar) }
          { E'₁.inh := temp }
       E'₁ { E'.lugar := E'₁.lugar }

E' → - T { temp := nueva_temporal() }
          { insertar_tabla(temp, 'temporal') }
          { generar(temp || ' := ' || E'.inh || ' - ' || T.lugar) }
          { E'₁.inh := temp }
       E'₁ { E'.lugar := E'₁.lugar }

E' → ε { E'.lugar := E'.inh }

T → F { T'.inh := F.lugar } 
    T' { T.lugar := T'.lugar }

T' → * F { temp := nueva_temporal() }
          { insertar_tabla(temp, 'temporal') }
          { generar(temp || ' := ' || T'.inh || ' * ' || F.lugar) }
          { T'₁.inh := temp }
       T'₁ { T'.lugar := T'₁.lugar }

T' → / F { temp := nueva_temporal() }
          { insertar_tabla(temp, 'temporal') }
          { generar(temp || ' := ' || T'.inh || ' / ' || F.lugar) }
          { T'₁.inh := temp }
       T'₁ { T'.lugar := T'₁.lugar }

T' → % F { temp := nueva_temporal() }
          { insertar_tabla(temp, 'temporal') }
          { generar(temp || ' := ' || T'.inh || ' % ' || F.lugar) }
          { T'₁.inh := temp }
       T'₁ { T'.lugar := T'₁.lugar }

T' → ε { T'.lugar := T'.inh }

F → num { F.lugar := num.lexema }
        { insertar_tabla('_const_' || num.lexema, 'constante', num.lexema) }

F → id { F.lugar := id.lexema }
       { si no existe(id.lexema): insertar_tabla(id.lexema, 'variable') }

F → ( E ) { F.lugar := E.lugar }

F → [ E₁, E₂, ..., Eₙ ] { temp := nueva_temporal() }
                        { generar(temp || ' := new_list(' || n || ')') }
                        { para i = 1 hasta n: generar(temp || '[' || i || '] := ' || Eᵢ.lugar) }
                        { F.lugar := temp }

# Sentencias de asignación
S → id := E { insertar_tabla(id.lexema, 'variable') si no existe }
            { generar(id.lexema || ' := ' || E.lugar) }

# Expresiones relacionales
C → E₁ relop E₂ { temp := nueva_temporal() }
                { insertar_tabla(temp, 'temporal') }
                { generar(temp || ' := ' || E₁.lugar || ' ' || relop || ' ' || E₂.lugar) }
                { C.lugar := temp }

# Llamadas a funciones
F → id ( Args ) { para cada arg en Args: generar('param ' || arg.lugar) }
                { temp := nueva_temporal() }
                { insertar_tabla(temp, 'temporal') }
                { generar(temp || ' := call ' || id.lexema || ', ' || Args.cantidad) }
                { F.lugar := temp }
"""
    
    print(gramatica)

def main():
    imprimir_gramatica_atributos()
    
    try:
        with open("entrada.txt", "r", encoding="utf-8") as f:
            expresion = f.read().strip()
        print(f"\nExpresión leída desde entrada.txt")
    except:
        expresion = "resultado = (5 + 3) * 2 - 8 / 4 + 10 % 3"
        print(f"\nNo se encontró entrada.txt, usando expresión de ejemplo")
    
    print(f"EXPRESIÓN A TRADUCIR: {expresion}\n")
    
    traductor = TraductorPython()
    
    traductor.tokens = traductor.tokenizar_expresion(expresion)
    
    print("Tokens generados:")
    for i, tok in enumerate(traductor.tokens[:-1]):  # excluir el token $
        print(f"   {i+1}. {tok['tipo']:15} → {tok['lexema']}")
    print()
    
    try:
        if len(traductor.tokens) >= 2 and traductor.tokens[0]["tipo"] == "id" and traductor.tokens[1]["tipo"] == "tk_asig":
            nombre_var = traductor.tokens[0]["lexema"]
            traductor.avanzar()  # consumir variable
            ast = traductor.traducir_asignacion(nombre_var)
        else:
            ast = traductor.traducir_expresion()
        
        print("AST DECORADO:")
        print("-"*70)
        imprimir_ast(ast)
        
        traductor.tabla.imprimir()
        traductor.generador.imprimir()
        
    except Exception as e:
        print(f"\nError durante la traducción: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
