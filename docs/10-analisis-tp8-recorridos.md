Analisis de recorridos en Grafos (BFS y DFS) 

1. BFS (Breadth-First Search / Recorrido en Anchura)
- ¿que hace?: Explora el grafo nivel por nivel, visitando primero a todos los vecinos directos antes de pasar a los nodos de niveles mas profundos. Utiliza una cola (Queue).
- cuando conviene (caso de uso real): Encontrar la pelicula o libro relacionado mas cercano o con la menor cantidad de saltos de conexión (por ejemplo, "¿cual es el libro recomendado mas cercano a matrix?").
- complejidad temporal y espacial: O(V + E) donde V son los vertices y E las aristas.

2. DFS (Depth-First Search / Recorrido en profundidad)
- ¿que hace?: Explora lo mas profundo posible a lo largo de cada rama antes de retroceder (backtracking). Utiliza una pila (Stack) o recursion.
- Cuando conviene (caso de uso real): explorar en profundidad todas las conexiones encadenadas de un genero o tematica a partir de un punto de partida (por ejemplo, "explora todas las derivaciones posibles de libros relacionados con Matrix").
- Complejidad temporal y espacial: O(V + E).

3. Diferencias principales:
- BFS prioriza amplitud (camino mas corto en aristas) usando una cola FIFO, mientras que DFS prioriza profundidad usando una pila LIFO.
