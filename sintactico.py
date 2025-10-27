from collections import defaultdict
from pprint import pprint

# =========================================
# GRAMÁTICA CORREGIDA
# =========================================
rules = [
    "programa -> decl_list",
    "decl_list -> decl decl_list | ε",
    "decl -> class_decl | func_decl | stmt",

    "class_decl -> class id class_herencia tk_dos_puntos TABS class_body ATRAS",
    "class_herencia -> tk_par_izq id tk_par_der | ε",
    "class_body -> decl_list",

    "func_decl -> def id tk_par_izq parametros tk_par_der func_tipo tk_dos_puntos TABS bloque ATRAS",
    "parametros -> parametro parametros' | ε",
    "parametros' -> tk_coma parametro parametros' | ε",
    "parametro -> id tk_dos_puntos tipo",
    "func_tipo -> tk_ejecuta tipo | ε",
    "tipo -> id | str | bool | object | tk_cua_izq tipo tk_cua_der | tk_cadena",

    "bloque -> tk_nueva_linea bloque | stmt bloque' | ε",
    "bloque' -> tk_nueva_linea bloque' | stmt bloque' | ε",

    # ✅ CORRECCIÓN: stmt_id' ahora maneja correctamente las expresiones
    "stmt -> id stmt_id' | if_stmt | while_stmt | for_stmt | print_stmt | return_stmt",
    "stmt_id' -> tk_dos_puntos tipo tk_asig expresion tk_nueva_linea | tk_asig expresion tk_nueva_linea | acceso_llamada",
    
    # ✅ NUEVO: acceso_llamada maneja accesos, llamadas Y asignaciones a atributos
    "acceso_llamada -> tk_punto id acceso_llamada_cont | tk_par_izq args tk_par_der acceso_post_llamada | tk_nueva_linea",
    "acceso_llamada_cont -> tk_asig expresion tk_nueva_linea | tk_punto id acceso_llamada_cont | tk_par_izq args tk_par_der acceso_post_llamada | tk_nueva_linea",
    "acceso_post_llamada -> tk_punto id acceso_llamada_cont | tk_nueva_linea",

    "tipo_opc -> tk_dos_puntos tipo | ε",

    "target -> id target'",
    "target' -> tk_punto id | ε",

    "expr_stmt -> expresion tk_nueva_linea",
    "return_stmt -> return expresion tk_nueva_linea",

    "if_stmt -> if condicion tk_dos_puntos TABS bloque ATRAS else_opc",
    "else_opc -> else tk_dos_puntos TABS bloque ATRAS | ε",
    "while_stmt -> while condicion tk_dos_puntos TABS bloque ATRAS",
    "for_stmt -> for id in expresion tk_dos_puntos TABS bloque ATRAS",
    "print_stmt -> print tk_par_izq expresion tk_par_der tk_nueva_linea",

    "condicion -> expresion condicion'",
    "condicion' -> op_rel expresion | ε",
    "op_rel -> tk_mayor | tk_menor | tk_igual | tk_distinto | tk_mayor_igual | tk_menor_igual",

    "expresion -> termino expresion'",
    "expresion' -> tk_suma termino expresion' | tk_resta termino expresion' | ε",
    "termino -> factor termino'",
    "termino' -> tk_mul factor termino' | tk_div factor termino' | ε",

    "factor -> tk_par_izq expresion tk_par_der | tk_entero | tk_cadena | True | False | None | id factor' | lista",
    "factor' -> tk_punto id factor'' | tk_par_izq args tk_par_der | ε",
    "factor'' -> tk_par_izq args tk_par_der | ε",

    "lista -> tk_cua_izq elementos tk_cua_der",
    "elementos -> expresion elementos' | ε",
    "elementos' -> tk_coma expresion elementos' | ε",

    "llamada -> id llamada'",
    "llamada' -> tk_par_izq args tk_par_der | tk_punto id tk_par_izq args tk_par_der | ε",

    "args -> expresion args' | ε",
    "args' -> tk_coma expresion args' | ε"
]

term_userdef = [
    'id','class','def','return','print','if','else','while','for','in',
    'str','bool','object','True','False','None',
    'tk_asig','tk_dos_puntos','tk_coma','tk_par_izq','tk_par_der',
    'tk_mayor','tk_menor','tk_igual','tk_distinto','tk_mayor_igual','tk_menor_igual',
    'tk_suma','tk_resta','tk_mul','tk_div','tk_punto','tk_cadena','tk_entero',
    'tk_nueva_linea','tk_ejecuta','TABS','ATRAS','tk_cua_izq','tk_cua_der'
]

producciones = defaultdict(list)
for r in rules:
    if "->" not in r:
        continue
    izquierda, derecha = r.split("->", 1)
    A = izquierda.strip()
    A = A.replace("'", "'").replace("'", "'").strip()

    opciones = [op.strip() for op in derecha.strip().split("|")]
    for op in opciones:
        symbols = [s.replace("'", "'").replace("'", "'").strip() for s in op.split() if s.strip() != ""]
        producciones[A].append(symbols)

nonterm_userdef = set(producciones.keys())
print("\n🧩 No terminales detectados automáticamente:", nonterm_userdef)

FIRST = defaultdict(set)
FOLLOW = defaultdict(set)

def primeros(simbolo):
    if simbolo in term_userdef:
        return {simbolo}
    if simbolo == "ε":
        return {"ε"}
    res = set()
    for prod in producciones[simbolo]:
        for s in prod:
            res |= (primeros(s) - {"ε"})
            if "ε" not in primeros(s):
                break
        else:
            res.add("ε")
    return res

def calcular_first():
    cambio = True
    while cambio:
        cambio = False
        for nt in nonterm_userdef:
            prev = set(FIRST[nt])
            for prod in producciones[nt]:
                for s in prod:
                    FIRST[nt] |= (FIRST[s] if s in FIRST else primeros(s)) - {"ε"}
                    if "ε" not in (FIRST[s] if s in FIRST else primeros(s)):
                        break
                else:
                    FIRST[nt].add("ε")
            if prev != FIRST[nt]:
                cambio = True

def calcular_follow():
    for nt in nonterm_userdef:
        FOLLOW[nt] = set()
    FOLLOW["programa"].add("$")

    cambio = True
    while cambio:
        cambio = False
        for A, prods in list(producciones.items()):
            for prod in prods:
                simbolos = prod if isinstance(prod, list) else str(prod).split()

                for i, B in enumerate(simbolos):
                    if B not in nonterm_userdef:
                        continue

                    beta = simbolos[i+1:] if i+1 < len(simbolos) else []

                    first_beta = set()
                    if beta:
                        for s in beta:
                            first_s = FIRST[s] if s in FIRST else primeros(s)
                            first_beta |= (first_s - {"ε"})
                            if "ε" in first_s:
                                continue
                            else:
                                break
                        else:
                            first_beta.add("ε")
                    else:
                        first_beta.add("ε")

                    prev_len = len(FOLLOW[B])

                    FOLLOW[B] |= (first_beta - {"ε"})

                    if not beta or "ε" in first_beta:
                        FOLLOW[B] |= FOLLOW[A]

                    if len(FOLLOW[B]) != prev_len:
                        cambio = True

tabla = defaultdict(dict)

def construir_tabla():
    tabla.clear()
    for A, prods in producciones.items():
        for prod in prods:
            simbolos = prod if isinstance(prod, list) else str(prod).split()

            first_alpha = set()
            if not simbolos:
                first_alpha.add("ε")
            else:
                for s in simbolos:
                    first_s = FIRST[s] if s in FIRST else primeros(s)
                    first_alpha |= (first_s - {"ε"})
                    if "ε" in first_s:
                        continue
                    else:
                        break
                else:
                    first_alpha.add("ε")

            for t in (first_alpha - {"ε"}):
                if t in tabla[A] and tabla[A][t] != simbolos:
                    print(f"⚠️ CONFLICTO LL(1) en {A} con token {t}\n   Producción existente: {tabla[A][t]}\n   Nueva producción: {simbolos}\n")
                tabla[A][t] = simbolos

            if "ε" in first_alpha:
                for b in FOLLOW[A]:
                    if b in tabla[A] and tabla[A][b] != simbolos:
                        print(f"⚠️ CONFLICTO LL(1) (ε) en {A} con token {b}\n   Producción existente: {tabla[A][b]}\n   Nueva producción: {simbolos}\n")
                    tabla[A][b] = simbolos

def leer_tokens(nombre_archivo="salida.txt"):
    tokens = []
    with open(nombre_archivo, "r", encoding="utf-8") as f:
        for linea in f:
            linea = linea.strip()
            if not linea or not linea.startswith("<"):
                continue
            partes = linea[1:-1].split(",")
            if len(partes) == 4:
                tipo = partes[0]
                lexema = partes[1]
                linea_num = int(partes[2])
                col = int(partes[3])
            elif len(partes) == 3:
                tipo = partes[0]
                lexema = partes[0]
                linea_num = int(partes[1])
                col = int(partes[2])
            else:
                continue
            tokens.append({"tipo": tipo, "lexema": lexema, "linea": linea_num, "col": col})
    tokens.append({"tipo": "$", "lexema": "$", "linea": 9999, "col": 9999})
    return tokens

mapa_simbolos = {
    "tk_par_izq": "(", "tk_par_der": ")", "tk_dos_puntos": ":",
    "tk_coma": ",", "tk_punto": ".", "tk_asig": "=",
    "tk_mayor": ">", "tk_menor": "<", "tk_igual": "==", "tk_distinto": "!=",
    "tk_mayor_igual": ">=", "tk_menor_igual": "<=", "tk_suma": "+", "tk_resta": "-",
    "tk_mul": "*", "tk_div": "/", "tk_cadena": "cadena", "tk_entero": "entero",
    "tk_nueva_linea": "\\n", "tk_ejecuta": "->", "TABS": "indentación", "ATRAS": "dedentación",
    "True": "True", "False": "False", "None": "None", "tk_cua_izq": "[", "tk_cua_der": "]"
}

def analizador_sintactico(tokens, tabla, simbolo_inicial="programa"):
    pila = ["$", simbolo_inicial]
    index = 0

    while pila:
        tope = pila[-1]
        actual = tokens[index]["tipo"]

        if tope == "$" and actual == "$":
            print("✔️ Análisis sintáctico completado sin errores.")
            return

        if tope in term_userdef or tope == "$":
            if tope == actual:
                pila.pop()
                index += 1
            else:
                token = tokens[index]
                esperado = mapa_simbolos.get(tope, tope)
                encontrado = mapa_simbolos.get(token["tipo"], token["lexema"])
                print(f"<{token['linea']},{token['col']}> Error sintactico: se encontro: \"{encontrado}\"; se esperaba: \"{esperado}\".")
                return
        else:
            if actual in tabla[tope]:
                prod = tabla[tope][actual]
                pila.pop()
                if prod != ["ε"]:
                    for s in reversed(prod):
                        pila.append(s)
            else:
                token = tokens[index]
                esperados = [mapa_simbolos.get(x, x) for x in tabla[tope].keys()]
                encontrados = mapa_simbolos.get(token["tipo"], token["lexema"])
                lista_esp = ",".join(f"\"{e}\"" for e in esperados)
                print(f"<{token['linea']},{token['col']}> Error sintactico: se encontro: \"{encontrados}\"; se esperaba: {lista_esp}.")
                return

if __name__ == "__main__":
    print("Calculando FIRST...")
    calcular_first()
    print("Calculando FOLLOW...")
    calcular_follow()
    print("Construyendo tabla LL(1)...")
    construir_tabla()
    print("Iniciando análisis sintáctico...\n")
    tokens = leer_tokens("salida.txt")
    analizador_sintactico(tokens, tabla, "programa")