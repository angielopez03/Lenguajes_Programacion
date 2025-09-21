import networkx as nx
import matplotlib.pyplot as plt

class analizadorEarley:
    def __init__(self, archivo_gramatica):
        self.gramatica = {}
        self.inicio = None
        self.cargar_gramatica(archivo_gramatica)

    def cargar_gramatica(self, archivo):
        with open(archivo, "r", encoding="utf-8") as f:
            for linea in f:
                linea = linea.strip()
                if not linea or linea.startswith("#"):
                    continue
                izquierda, derecha = linea.split("->")
                izquierda = izquierda.strip()
                alternativas = [alt.strip().split() for alt in derecha.split("|")]
                if self.inicio is None:
                    self.inicio = izquierda
                self.gramatica.setdefault(izquierda, []).extend(alternativas)

    def analizar(self, tokens, valores=None):
        self.valores = valores or tokens
        n = len(tokens)
        tabla = [set() for _ in range(n+1)]
        estado_inicial = (self.inicio, tuple(self.gramatica[self.inicio][0]), 0, 0, ())
        tabla[0].add(estado_inicial)

        for i in range(n+1):
            agregado = True
            while agregado:
                agregado = False
                for estado in list(tabla[i]):
                    izquierda, derecha, punto, origen, hijos = estado
                    # Avance
                    if punto < len(derecha):
                        simbolo = derecha[punto]
                        if simbolo in self.gramatica:  # no terminal
                            for prod in self.gramatica[simbolo]:
                                nuevo = (simbolo, tuple(prod), 0, i, ())
                                if nuevo not in tabla[i]:
                                    tabla[i].add(nuevo); agregado = True
                        elif i < n and tokens[i] == simbolo:  # terminal
                            lexema = self.valores[i] if simbolo in ["num", "id", "opsuma", "opmul", "pari", "pard"] else tokens[i]
                            nuevo = (izquierda, derecha, punto+1, origen,
                                     hijos + ((simbolo, (lexema,)),))
                            tabla[i+1].add(nuevo)
                    else:  # Reducción
                        for st in list(tabla[origen]):
                            izq2, der2, pto2, ori2, hij2 = st
                            if pto2 < len(der2) and der2[pto2] == izquierda:
                                nuevo = (izq2, der2, pto2+1, ori2,
                                         hij2 + ((izquierda, hijos),))
                                if nuevo not in tabla[i]:
                                    tabla[i].add(nuevo); agregado = True
        for estado in tabla[n]:
            if estado[0] == self.inicio and estado[3] == 0 and \
                estado[2] == len(estado[1]):
                    return (self.inicio, estado[4])
        return None

    def construir_grafo(self, arbol):
        G = nx.DiGraph()
        contador = {"c": 0}
        def nuevo_id():
            i = contador["c"]
            contador["c"] += 1
            return f"n{i}"

        def agregar(nodo):
            if isinstance(nodo, tuple) and len(nodo) == 2 and isinstance(nodo[1], tuple):
                simbolo, hijos = nodo
                nid = nuevo_id()
                G.add_node(nid, label=simbolo)
                for h in hijos:
                    cid = agregar(h)
                    G.add_edge(nid, cid)
                return nid
            else:
                nid = nuevo_id()
                G.add_node(nid, label=str(nodo))
                return nid

        raiz = agregar(arbol)
        return G, raiz

    def jerarquia(self, G, raiz, x=0, y=0, dx=1.0, dy=-1.0, pos=None, nivel=0):
        if pos is None:
            pos = {raiz: (x, y)}
        hijos = list(G.successors(raiz))
        if hijos:
            ancho = dx * (len(hijos) - 1)
            siguiente_x = x - ancho / 2
            for i, hijo in enumerate(hijos):
                pos[hijo] = (siguiente_x + i * dx, y + dy)
                self.jerarquia(G, hijo, siguiente_x + i * dx, y + dy, dx/2, dy, pos, nivel+1)
        return pos

    def dibujar(self, G, raiz, cadena):
        pos = self.jerarquia(G, raiz, dx=4.0, dy=-1.5)
        etiquetas = nx.get_node_attributes(G, 'label')
        nx.draw(G, pos, labels=etiquetas, with_labels=True,
                node_color="lightblue", node_size=1200,
                font_size=9, arrows=False)
        plt.title(f"Árbol de sintaxis: {cadena}")
        plt.show()

def tokenizar(cadena):
    tokens, valores = [], []
    i = 0
    mapeo = {'+': 'opsuma', '*': 'opmul', '(': 'pari', ')': 'pard'}

    while i < len(cadena):
        c = cadena[i]
        if c.isspace():
            i += 1
        elif c in mapeo:
            tokens.append(mapeo[c])
            valores.append(c)
            i += 1
        elif c.isdigit():
            num = ""
            while i < len(cadena) and cadena[i].isdigit():
                num += cadena[i]; i += 1
            tokens.append("num"); valores.append(num)
        elif c.isalpha():
            var = ""
            while i < len(cadena) and cadena[i].isalnum():
                var += cadena[i]; i += 1
            tokens.append("id"); valores.append(var)
        else:
            print(f"Error: símbolo no soportado '{c}'")
            return None, None
    return tokens, valores

def main():
    analizador = analizadorEarley("gra.txt")
    print("Ingrese 'salir' para terminar")

    while True:
        cadena = input("\nCadena: ").strip()
        if cadena.lower() == "salir":
            break
        tokens, valores = tokenizar(cadena)
        if tokens is None:
            print("NO ACEPTADA (símbolo inválido)")
            continue
        arbol = analizador.analizar(tokens, valores)
        if arbol:
            print("ACEPTADA")
            G, raiz = analizador.construir_grafo(arbol)
            analizador.dibujar(G, raiz, cadena)
        else:
            print("NO ACEPTADA (no cumple la gramática)")

if __name__ == "__main__":
    main()
