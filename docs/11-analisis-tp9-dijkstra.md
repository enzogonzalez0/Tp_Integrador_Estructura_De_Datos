Analisis de pptimización y camino Minimo 

1. significado de "Costo" en el Dominio:
- representa el grado de similitud inverso (o "distancia tematica"). Si un peso alto indica alta afinidad, el costo se define como el inverso o penalización (por ejemplo, 1.0 - similitud), donde un costo menor significa que dos obras estan fuertemente conectadas de forma directa.

2. Algoritmo Seleccionado (Dijkstra):
- Justificación: Es ideal para grafos ponderados (con pesos positivos en las aristas) no dirigidos. Permite encontrar el camino mínimo acumulado desde un libro de origen hasta cualquier otro del catalogo. Se descartan algoritmos de pesos negativos (como Bellman-Ford) ya que las métricas de afinidad no admiten valores negativos.

3. Complejidad:
- O((V + E) log V) utilizando una cola de prioridad eficiente.
