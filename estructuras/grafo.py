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
