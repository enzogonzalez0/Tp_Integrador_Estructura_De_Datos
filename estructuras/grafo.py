class Grafo:
    def __init__(self):
        self.adj_list = {}

    def agregar_vertice(self, vertice):
        if vertice not in self.adj_list:
            self.adj_list[vertice] = {}

    def agregar_arista(self, origen, destino, peso=1.0):
        self.agregar_vertice(origen)
        self.agregar_vertice(destino)
        self.adj_list[origen][destino] = peso
        self.adj_list[destino][origen] = peso  # No dirigido

    def obtener_vecinos(self, vertice):
        return self.adj_list.get(vertice, {})

    def bfs(self, inicio):
        if inicio not in self.adj_list:
            return []
        
        visitados = []
        cola = [inicio]
        visitados_set = {inicio}

        while cola:
            actual = cola.pop(0)
            visitados.append(actual)
            for vecino in self.adj_list[actual]:
                if vecino not in visitados_set:
                        visitados_set.add(vecino)
                        cola.append(vecino)
        return visitados

    def dfs(self, inicio):
        if inicio not in self.adj_list:
            return []
        
        visitados = []
        pila = [inicio]
        visitados_set = set()

        while pila:
            actual = pila.pop()
            if actual not in visitados_set:
                visitados_set.add(actual)
                visitados.append(actual)
                # Agregar vecinos en orden inverso para mantener consistencia en la pila
                for vecino in sorted(self.adj_list[actual].keys(), reverse=True):
                    if vecino not in visitados_set:
                        pila.append(vecino)
        return visitados

    def dijkstra(self, origen):
        import heapq
        
        distancias = {vertice: float('inf') for vertice in self.adj_list}
        if origen not in distancias:
            return distancias
            
        distancias[origen] = 0
        pq = [(0, origen)]

        while pq:
            dist_actual, actual = heapq.heappop(pq)

            if dist_actual > distancias[actual]:
                continue

            for vecino, peso in self.adj_list[actual].items():
                distancia = dist_actual + peso

                if distancia < distancias[vecino]:
                    distancias[vecino] = distancia
                    heapq.heappush(pq, (distancia, vecino))

        return distancias
