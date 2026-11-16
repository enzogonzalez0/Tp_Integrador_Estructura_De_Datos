#TP7: estructura de Grafo No dirigido y pesado (Lista de Adyacencia)

class Grafo:
    def __init__(self):
        self.adj = {}

    def agregar_vertice(self, vertice):
        """Agrega un libro al grafo si no existe."""
        if vertice not in self.adj:
            self.adj[vertice] = {}

    def agregar_arista(self, origen, destino, peso=1.0):
        """Conecta dos libros con un peso de similitud (bidireccional)."""
        self.agregar_vertice(origen)
        self.agregar_vertice(destino)
        
        self.adj[origen][destino] = peso
        self.adj[destino][origen] = peso

    def obtener_vecinos(self, vertice):
        """Devuelve los libros conectados y el peso de su relacion."""
        if vertice in self.adj:
            return self.adj[vertice]
        return {}

def bfs(self, inicio):
        """Recorrido BFS (Anchura) - Devuelve los nodos ordenados por nivel de cercanía."""
        visitados = set()
        cola = [inicio]
        visitados.add(inicio)
        orden = []

        while cola:
            actual = cola.pop(0)
            orden.append(actual)
            
            for vecino in self.adj.get(actual, {}):
                if vecino not in visitados:
                    visitados.add(vecino)
                    cola.append(vecino)
                    
        return orden

    def dfs(self, inicio):
        """Recorrido DFS (Profundidad) - Explora las ramas en profundidad."""
        visitados = set()
        orden = []

        def _dfs_recursivo(nodo):
            visitados.add(nodo)
            orden.append(nodo)
            for vecino in self.adj.get(nodo, {}):
                if vecino not in visitados:
                    _dfs_recursivo(vecino)

        _dfs_recursivo(inicio)
        return orden
