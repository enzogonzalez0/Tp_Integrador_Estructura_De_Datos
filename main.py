import sys
from estructuras.TP4avl import AVL
from estructuras.TP5arbol_general import ArbolGeneral

def cargar_datos_demo(arbol_avl, arbol_cat):
    libros = [
       "El Principito",
        "Rebelion en la Granja",
        "El Extranjero",
        "Crónica de una Muerte Anunciada",
        "Un Mundo Feliz",
        "Dracula",
        "La Metamorfosis",
    ]
    for libro in libros:
        arbol_avl.insertar(libro)

    arbol_cat.agregar_raiz("Categorias")
    arbol_cat.agregar_hijo("Categorias", "Ficcion")
    arbol_cat.agregar_hijo("Categorias", "No Ficcion")

    arbol_cat.agregar_hijo("Ficcion", "Ciencia Ficcion")
    arbol_cat.agregar_hijo("Ficcion", "Novela")

    arbol_cat.agregar_hijo("No Ficcion", "Historia")
    arbol_cat.agregar_hijo("No Ficcion", "Ensayos")


def menu_principal():
    avl = AVL()
    categorias = ArbolGeneral()
    cargar_datos_demo(avl, categorias)

    while True:
        print("\n=== BOOKFINDER - SISTEMA DE BUSQUEDA Y CATEGORIAS ===")
        print("1. Buscar libro (Usando AVL)")
        print("2. Explorar categorias (Usando Arbol General)")
        print("3. Ver recorrido Inorder de libros (AVL)")
        print("4. Salir")

        opcion = input("Seleccione una opcion: ").strip()

        if opcion == "1":
            titulo = input("Ingrese el titulo a buscar: ").strip()
            hallado = avl.buscar(titulo)
            if hallado:
                print(f"El libro '{titulo}' esta disponible en el catalogo.")
            else:
                print(f"El libro '{titulo}' no se encuentra en el catalogo.")

        elif opcion == "2":
            print("\nCategorias disponibles (BFS / Anchura):")
            lista_cat = categorias.recorrido_anchura()
            print(" -> ".join(lista_cat))

            cat_buscar = input("\nIngrese categoria para ver si existe: ").strip()
            nodo = categorias.buscar_nodo(cat_buscar)
            if nodo:
                hijos = [h.nombre for h in nodo.hijos]
                print(f"Subcategorias de '{nodo.nombre}': {hijos if hijos else 'Sin subcategorias'}")
            else:
                print("La categoria no existe.")

        elif opcion == "3":
            print("\nCatalogo ordenado alfabeticamente:")
            print(avl.inorder())

        elif opcion == "4":
            print("Saliendo del sistema...")
            sys.exit()

        else:
            print("Opcion invalida. Intente de nuevo.")


if __name__ == "__main__":
    menu_principal()


# BOOKFINDER - SISTEMA INTEGRADOR FINAL 

from estructuras.heap import HeapMax
from estructuras.grafo import Grafo

def mostrar_menu():
    print("\n" + "="*60)
    print(" BOOKFINDER - SISTEMA INTEGRADOR DE ESTRUCTURAS DE DATOS")
    print("="*60)
    print(" 1. [TP1 - TP2] Busqueda Secuencial e Indexada en Catalogo")
    print(" 2. [TP3 - TP5] Visualizacion y Gestion de Estructuras Jerarquicas (Arboles)")
    print(" 3. [TP6] Ranking Dinamico de Libros (Heap Maximo / Top-N)")
    print(" 4. [TP7] Red de Afinidad y Relaciones (Grafo No Dirigido)")
    print(" 5. [TP8] Exploracion de Conexiones (Recorridos BFS y DFS)")
    print(" 6. [TP9] Optimizacion de Recomendaciones (Camino Minimo - Dijkstra)")
    print(" 7. Salir del Sistema")
    print("="*60)

def inicializar_sistema():
    ranking = HeapMax()
    ranking.insertar(9.8, "El Principito")
    ranking.insertar(9.6, "Rebelion en la Granja")
    ranking.insertar(9.5, "El Extranjero")
    ranking.insertar(9.9, "Cronica de una Muerte Anunciada")
    ranking.insertar(9.2, "Un Mundo Feliz")
    ranking.insertar(9.4, "Dracula")
    ranking.insertar(9.1, "La Metamorfosis")
    
    red = Grafo()
    red.agregar_arista("El Principito", "Rebelion en la Granja", peso=0.2)
    red.agregar_arista("El Principito", "El Extranjero", peso=0.5)
    red.agregar_arista("Rebelion en la Granja", "Un Mundo Feliz", peso=0.1)
    red.agregar_arista("Un Mundo Feliz", "Cronica de una Muerte Anunciada", peso=0.3)
    red.agregar_arista("El Extranjero", "La Metamorfosis", peso=0.2)
    red.agregar_arista("Dracula", "La Metamorfosis", peso=0.4)

    catalogo = [
        {"id": 1, "titulo": "El Principito", "genero": "Literatura Infantil / Filosofia", "stock": 5},
        {"id": 2, "titulo": "Rebelion en la Granja", "genero": "Satira Politica", "stock": 3},
        {"id": 3, "titulo": "El Extranjero", "genero": "Novela Filosofica", "stock": 4},
        {"id": 4, "titulo": "Cronica de una Muerte Anunciada", "genero": "Realismo Magico", "stock": 6},
        {"id": 5, "titulo": "Un Mundo Feliz", "genero": "Ciencia Ficcion / Distopia", "stock": 2},
        {"id": 6, "titulo": "Dracula", "genero": "Gotico / Terror", "stock": 4},
        {"id": 7, "titulo": "La Metamorfosis", "genero": "Novela Corta / Absurdo", "stock": 5}
    ]
    
    return ranking, red, catalogo

def main():
    ranking, red, catalogo = inicializar_sistema()
    
    while True:
        mostrar_menu()
        opcion = input("Ingrese una opcion (1-7): ").strip()
        
        if opcion == "1":
            print("\n" + "-"*40)
            print("--- [TP1 - TP2] BUSQUEDA SECUENCIAL E INDEXADA ---")
            print("-"*40)
            criterio = input("Ingrese termino a buscar (titulo o genero): ").lower()
            encontrados = [lib for lib in catalogo if criterio in lib["titulo"].lower() or criterio in lib["genero"].lower()]
            if encontrados:
                for lib in encontrados:
                    print(f"  [ID: {lib['id']}] Titulo: {lib['titulo']} | Genero: {lib['genero']} | Stock: {lib['stock']}")
            else:
                print("  [Aviso] No se encontraron coincidencias en el catalogo.")
                
        elif opcion == "2":
            print("\n" + "-"*40)
            print("--- [TP3 - TP5] ARBOLES Y ESTRUCTURAS JERARQUICAS ---")
            print("-"*40)
            print("  - Modulos de Arboles AVL y Arboles Generales cargados correctamente.")
            print("  - Para pruebas unitarias especificas, ejecute los scripts dedicados en la carpeta 'algoritmos/'.")
                
        elif opcion == "3":
            print("\n" + "-"*40)
            print("--- [TP6] RANKING DE LIBROS (HEAP MAXIMO) ---")
            print("-"*40)
            n_input = input("¿Cuantos libros principales desea ver en el Top-N? (Presione Enter para 5): ").strip()
            n = int(n_input) if n_input.isdigit() else 5
            top = ranking.obtener_top_n(n)
            for i, (rating, titulo) in enumerate(top, 1):
                print(f"  {i}. Titulo: {titulo} — Puntuacion: {rating}")
                
        elif opcion == "4":
            print("\n" + "-"*40)
            print("--- [TP7] RED DE AFINIDAD (GRAFOS) ---")
            print("-"*40)
            nodo = "El Principito"
            vecinos = red.obtener_vecinos(nodo)
            print(f"Relaciones directas para '{nodo}':")
            for vecino, peso in vecinos.items():
                print(f"  - Conectado con '{vecino}' (Peso/Distancia: {peso})")
                
        elif opcion == "5":
            print("\n" + "-"*40)
            print("--- [TP8] RECORRIDOS EN RED (BFS / DFS) ---")
            print("-"*40)
            inicio = "El Principito"
            print(f"BFS (Busqueda en Anchura / Por niveles desde '{inicio}'):")
            print("   -->", " -> ".join(red.bfs(inicio)))
            print(f"DFS (Busqueda en Profundidad desde '{inicio}'):")
            print("   -->", " -> ".join(red.dfs(inicio)))
                
        elif opcion == "6":
            print("\n" + "-"*40)
            print("--- [TP9] CAMINO MINIMO (ALGORITMO DE DIJKSTRA) ---")
            print("-"*40)
            origen = "El Principito"
            costos = red.dijkstra(origen)
            print(f"Costos minimos acumulados desde '{origen}':")
            for libro, costo in costos.items():
                print(f"  - Hacia '{libro}': Costo total acumulado = {costo:.2f}")
                
        elif opcion == "7":
            print("\nSaliendo del sistema...")
            break
        else:
            print("\n[Error] Opcion invalida. Por favor, ingrese un numero del 1 al 7.")

if __name__ == "__main__":
    main()
