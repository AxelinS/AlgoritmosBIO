import random

class hormiga:
    def __init__(self,posicion) -> None:
        self.nombre = random.choice(list(["Pepe","Ramon","Horacio","Miguelito","Halfonso","Juancholin","Juan"]))
        self.posicion = posicion
        self.visitados = [posicion]

class nodo:
    def __init__(self,id:str,vecinos,feromona=1) -> None:
        self.id = id
        self.feromona = feromona
        self.vecinos = vecinos

class Grafo:
    def __init__(self):
        self.grafo = []
        self.indexes = {}

    def agregar_arista(self, nodo_origen:str, nodo_destino:str, peso:int):
        if self.grafo:
            found_origen = False
            existe_destino = False
            for n in self.grafo:
                if n.id == nodo_origen:
                    found_origen = True
                    n.vecinos[nodo_destino] = peso
                if n.id == nodo_destino: existe_destino=True
            if not found_origen:
                self.grafo.append(nodo(id=nodo_origen,vecinos={nodo_destino:peso}))
                self.indexes[nodo_origen] = len(self.indexes)
                self.grafo.append(nodo(id=nodo_destino,vecinos={nodo_origen:peso}))
                self.indexes[nodo_destino] = len(self.indexes)
            if not existe_destino:
                self.grafo.append(nodo(id=nodo_destino,vecinos={nodo_origen:peso}))
                self.indexes[nodo_destino] = len(self.indexes)
        else:
            self.grafo.append(nodo(id=nodo_origen,feromona=1,vecinos={nodo_destino:peso}))
            self.indexes[nodo_origen] = len(self.indexes)
            self.grafo.append(nodo(id=nodo_destino,vecinos={nodo_origen:peso}))
            self.indexes[nodo_destino] = len(self.indexes)
    
    def set_indexes(self):
        for i,n in enumerate(self.grafo):
            self.indexes[n.id] = i

    def mostrar_grafo(self):
        for nodo in self.grafo:
            print(f"{nodo.id}: Feromonas {nodo.feromona}  ||  vecinos:{nodo.vecinos}. ")

def depositar_fero(hormiga):
    peso_total = 1
    nodos_vistos = hormiga.visitados

    for i in range(len(nodos_vistos)-1):
        peso_total += g.grafo[g.indexes[nodos_vistos[i]]].vecinos[nodos_vistos[i+1]]
    
    Ttij = cantidad_fero_gen/peso_total

    for n in nodos_vistos:
        nuevo_val = (1-coeficiente_desaparicion)*g.grafo[g.indexes[n]].feromona + Ttij
        g.grafo[g.indexes[n]].feromona = nuevo_val

def calcular_movimiento(hormiga):
    posicion = hormiga.posicion

    node = g.grafo[g.indexes[posicion]]

    if node.id == nodo_destino:
        depositar_fero(hormiga)
        hormiga.visitados = []
        hormiga.posicion = "A"
    else:
        probabilidades = []
        nodes = []

        stuck = True
        for n in node.vecinos:
            if n not in hormiga.visitados:
                stuck = False

        for v in node.vecinos:
            probabi = []
            if stuck:
                for i in node.vecinos:
                    nodes.append(i)
                    probabilidades.append(100/len(node.vecinos))
            elif v not in hormiga.visitados:
                n = g.grafo[g.indexes[v]]
                nodes.append(v)
                for prob in node.vecinos:
                    if prob not in hormiga.visitados:
                        probabi.append(((n.feromona**fortaleza)*((1/node.vecinos[prob])**heuristica)))
                P = ((n.feromona**fortaleza)*((1/node.vecinos[v])**heuristica)) / sum(probabi)
                probabilidades.append(P)
        next_node = random.choices(nodes, weights=probabilidades, k=1)[0]
        hormiga.visitados.append(next_node)
        hormiga.posicion = next_node
        next_node = g.grafo[g.indexes[next_node]]
        
def actualizar_hormiga():
    for h in colonia:
        calcular_movimiento(h)

def actualizar_feromona():
    for n in g.grafo:
        if n.feromona > 1:
            n.feromona = (1-coeficiente_desaparicion)*n.feromona
        else: n.feromona = 1

g = Grafo()
g.agregar_arista("A", "B", 1)
g.agregar_arista("A", "C", 2)
g.agregar_arista("B", "C", 1)
g.agregar_arista("B", "D", 4)
g.agregar_arista("C", "D", 1)
g.agregar_arista("D", "E", 3)
g.agregar_arista("A", "F", 3)
g.agregar_arista("B", "F", 5)
g.agregar_arista("C", "G", 2)
g.agregar_arista("D", "H", 6)
g.agregar_arista("E", "H", 4)
g.agregar_arista("F", "G", 2)
g.agregar_arista("G", "H", 1)
g.agregar_arista("H", "I", 3)
g.agregar_arista("E", "I", 2)
g.agregar_arista("F", "I", 5)

print("Grafo al inicio:")
g.mostrar_grafo()

hormigas = 3
epocas = 20
colonia = []
fortaleza = 1
heuristica = 2
coeficiente_desaparicion = 0.6
cantidad_fero_gen = 100
nodo_destino = "I"

for i in range(hormigas):
    colonia.append(hormiga("A"))

for _ in range(epocas):
    actualizar_feromona()
    actualizar_hormiga()

print("\nGrafo al final:")

g.mostrar_grafo()

nombres_h = []
for h in colonia:
    nombres_h.append([{h.nombre:h.posicion}])

print("\nSaluda a las poderosas hormigas: ", nombres_h)