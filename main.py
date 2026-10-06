import sys
from estructuras.avl import AVL
from estructuras.arbol_general import ArbolGeneral


def cargar_datos_demo(arbol_avl, arbol_cat):
    # Carga de libros en el AVL
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

    # Carga de jerarquía en el Árbol General
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
