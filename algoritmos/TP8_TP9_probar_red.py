from estructuras.grafo import Grafo

def probar_red_completa():
    print("--- PRUEBA DE RECORRIDOS Y CAMINO MÍNIMO - BOOKFINDER ---")
    
    red = Grafo()
    
    red.agregar_arista("Matrix", "Inception", peso=0.2)
    red.agregar_arista("Matrix", "Terminator", peso=0.5)
    red.agregar_arista("Inception", "Interstellar", peso=0.1)
    red.agregar_arista("Interstellar", "Arrival", peso=0.3)
    red.agregar_arista("Terminator", "Alien", peso=0.2)

    print("\n--- TP8: RECORRIDOS (BFS / DFS) ---")
    print("BFS desde 'Matrix' (Búsqueda por niveles/cercanía):", red.bfs("Matrix"))
    print("DFS desde 'Matrix' (Exploración en profundidad):", red.dfs("Matrix"))

    print("\n--- TP9: CAMINO MÍNIMO (DIJKSTRA) ---")
    costos = red.dijkstra("Matrix")
    print("Costos mínimos acumulados desde 'Matrix':")
    for libro, costo in costos.items():
        print(f" - Hasta '{libro}': Costo total = {costo:.2f}")

if __name__ == "__main__":
    probar_red_completa()
