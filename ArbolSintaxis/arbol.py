import networkx as nx
import matplotlib.pyplot as plt
from collections import defaultdict

class EarleyParser:
    def __init__(self, grammar_file):
        self.grammar = defaultdict(list)
        self.start = None
        self.cargar_gramatica(grammar_file)

    def cargar_gramatica(self, file):
        with open(file, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                left, right = line.split("->")
                left = left.strip()
                rights = [alt.strip().split() for alt in right.split("|")]
                if self.start is None:
                    self.start = left
                self.grammar[left].extend(rights)

    def parse(self, tokens, valores=None):
        self.valores = valores or tokens
        n = len(tokens)
        chart = [set() for _ in range(n+1)]
        start_item = (self.start, tuple(self.grammar[self.start][0]), 0, 0, ())
        chart[0].add(start_item)

        for i in range(n+1):
            added = True
            while added:
                added = False
                for state in list(chart[i]):
                    lhs, rhs, dot, origin, children = state
                    # Avance
                    if dot < len(rhs):
                        sym = rhs[dot]
                        if sym in self.grammar:  # no terminal
                            for prod in self.grammar[sym]:
                                new = (sym, tuple(prod), 0, i, ())
                                if new not in chart[i]:
                                    chart[i].add(new); added = True
                        elif i < n and tokens[i] == sym:  # terminal
                            lexema = self.valores[i] if sym in ["num", "id"] else tokens[i]
                            new = (lhs, rhs, dot+1, origin,
                                   children + ((sym, (lexema,)),))
                            chart[i+1].add(new)
                    else:  # Reducción
                        for st in list(chart[origin]):
                            l2, r2, d2, o2, c2 = st
                            if d2 < len(r2) and r2[d2] == lhs:
                                new = (l2, r2, d2+1, o2,
                                       c2 + ((lhs, children),))
                                if new not in chart[i]:
                                    chart[i].add(new); added = True
        for state in chart[n]:
            if state[0] == self.start and state[3] == 0 and \
               state[1] == tuple(self.grammar[self.start][0]) and \
               state[2] == len(state[1]):
                return (self.start, state[4])
        return None

    def construir_grafo(self, tree):
        G = nx.DiGraph()
        def add(node):
            if isinstance(node, tuple) and len(node) == 2 and isinstance(node[1], tuple):
                simbolo, hijos = node
                nid = id(node)
                G.add_node(nid, label=simbolo)
                for h in hijos:
                    cid = add(h)
                    G.add_edge(nid, cid)
                return nid
            else:
                nid = id(node) ^ hash(node)
                G.add_node(nid, label=str(node))
                return nid
        root = add(tree)
        return G, root

    def jerarquia(self, G, root, x=0, y=0, dx=1.0, dy=-1.0, pos=None, level=0):
        if pos is None:
            pos = {root: (x, y)}
        neighbors = list(G.successors(root))
        if neighbors:
            width = dx * (len(neighbors) - 1)
            nextx = x - width / 2
            for i, child in enumerate(neighbors):
                pos[child] = (nextx + i * dx, y + dy)
                self.jerarquia(G, child, nextx + i * dx, y + dy, dx/2, dy, pos, level+1)
        return pos

    def dibujar(self, G, root, cadena):
        pos = self.jerarquia(G, root, dx=4.0, dy=-1.5)
        labels = nx.get_node_attributes(G, 'label')
        nx.draw(G, pos, labels=labels, with_labels=True,
                node_color="lightblue", node_size=1200,
                font_size=9, arrows=False)
        plt.title(f"Árbol de sintaxis: {cadena}")
        plt.show()

def tokenizar(cadena):
    tokens, valores = [], []
    i = 0
    while i < len(cadena):
        if cadena[i].isspace():
            i += 1
        elif cadena[i] in "+-*/()":
            tokens.append(cadena[i]); valores.append(cadena[i]); i += 1
        elif cadena[i].isdigit():
            num = ""
            while i < len(cadena) and cadena[i].isdigit():
                num += cadena[i]; i += 1
            tokens.append("num"); valores.append(num)
        else:
            var = ""
            while i < len(cadena) and cadena[i].isalnum():
                var += cadena[i]; i += 1
            tokens.append("id"); valores.append(var)
    return tokens, valores


def main():
    parser = EarleyParser("gra.txt")
    print("Ingrese 'salir' para terminar")

    while True:
        cadena = input("\nCadena: ").strip()
        if cadena.lower() == "salir":
            break
        tokens, valores = tokenizar(cadena)
        tree = parser.parse(tokens, valores)
        if tree:
            print("ACEPTADA")
            G, root = parser.construir_grafo(tree)
            parser.dibujar(G, root, cadena)
        else:
            print("NO ACEPTADA")

if __name__ == "__main__":
    main()
