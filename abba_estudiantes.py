from itertools import product
from collections import deque

"""
Facundo Torino: 
"""

class GrafoDirigido:
    def __init__(self) -> None:
        self.vertices: list = []
        self.vecinos: dict = {}

    def agregar_vertice(self, vertice: str) -> None:
        if vertice not in self.vecinos:
            self.vertices.append(vertice)
            self.vecinos[vertice] = set()

    def agregar_arista(self, origen: str, destino: str) -> None:
        if origen not in self.vecinos:
            self.agregar_vertice(origen)

        if destino not in self.vecinos:
            self.agregar_vertice(destino)

        self.vecinos[origen].add(destino)

    def get_adjacent(self, vertice: str) -> set:
        return self.vecinos[vertice]

    def get_nodes(self) -> list:
        return self.vertices

    def __eq__(self, other: "GrafoDirigido") -> bool:
        """compara dos grafos dirigidos (sin tener en cuenta el orden de los conjuntos de vertices y aristas)"""

        if len(self.vecinos.keys()) != len(other.vecinos.keys()):
            return False

        for vertice, vecinos in self.vecinos.items():
            if vertice not in other.vecinos:
                return False

            if vecinos != other.vecinos[vertice]:
                return False

        return True


def es_palindromo(s: str) -> bool:
    return s == s[::-1]


def generar_G_r(n: int, alfabeto: list[str]) -> GrafoDirigido | None:
    """
    Genera el grafo de reemplazos para todas las cadenas posibles de longitud `n`
    construidas a partir de un conjunto de caracteres (alfabeto) dado.

    En el grafo de reemplazos, los nodos representan todas las combinaciones
    posibles de caracteres de longitud `n` generadas a partir del alfabeto.
    Dos nodos `s` y `s'` están conectados mediante una arista dirigida de `s` a `s'`
    si `s'` puede obtenerse de `s` mediante una operación de reemplazo que cambia
    todas las ocurrencias de un carácter `char1` por otro carácter `char2`.

    Args:
        n (int): La longitud de las cadenas que forman los nodos del grafo.
        alfabeto (list[str]): Lista de caracteres usados para generar todas las
                              combinaciones posibles de longitud `n`.

    Returns:
        GrafoDirigido | None: El grafo de reemplazos generado. Retorna `None` si
                              `n` es 0 o si el alfabeto está vacío, ya que no
                              pueden generarse cadenas en estos casos.
    """
    if n <= 0 or len(alfabeto) == 0:
        return None

    grafo = GrafoDirigido()

    # Hago el producto de todos los elementos del alfabeto para generar todos los posibles vertices
    producto_cartesiano = product(alfabeto, repeat=n)
    vertices = ["".join(c) for c in producto_cartesiano]

    for vertice in vertices:
        v = vertice
        grafo.agregar_vertice(v)

    # Generar aristas de reemplazo
    for cadena in grafo.get_nodes():
        for char1 in set(cadena):  # Solo los caracteres que están en la cadena actual
            for char2 in alfabeto:
                if char1 != char2:
                    reemplazada = cadena.replace(char1, char2)
                    grafo.agregar_arista(cadena, reemplazada)

    return grafo


def distancia_a_palindromo(grafo: GrafoDirigido, start: str) -> int:
    """utiliza un algoritmo BFS para encontrar la minima distancia desde start
    a un palindromo en el grafo de reemplazos"""

    if es_palindromo(start):
        return 0

    visitados = []
    cola = deque([(start, 0)])  # Vertice actual y la distancia

    while len(cola) != 0:
        vertice, distancia = cola.popleft()

        if es_palindromo(vertice):
            return distancia

        if vertice not in visitados:
            visitados.append(vertice)

            for vecino in grafo.get_adjacent(vertice):
                if vecino not in visitados:
                    cola.append((vecino, distancia + 1))

    # No se encontró ningun palíndromo
    return -1


grafo = generar_G_r(2, ["a", "b"])
print(grafo.vecinos)

# Ejemplo Básico:
# grafo = generar_G_r(4, ["o", "n", "c", "e"])
# print(grafo.vecinos)
# print(distancia_a_palindromo(grafo, "once"))  # Deberia devolver 2.
