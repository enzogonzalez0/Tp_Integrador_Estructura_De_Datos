#script de prueba para el TP7: red de Recomendaciones por grafos
from estructuras.grafo import Grafo

def probar_grafo():
    print("--- RED DE RELACIONES (GRAFOS) - BOOKFINDER ---")
    
    red_libros = Grafo()
    
    red_libros.agregar_arista("Matrix", "Inception", peso=0.9)
    red_libros.agregar_arista("Matrix", "Terminator", peso=0.85)
    red_libros.agregar_arista("Inception", "Interstellar", peso=0.95)
    red_libros.agregar_arista("Terminator", "Alien", peso=0.8)
    
    print("\nConsultando recomendaciones relacionadas a 'Matrix':")
    vecinos = red_libros.obtener_vecinos("Matrix")
    
    for libro, similitud in vecinos.items():
        print(f" - Relacionado con: '{libro}' (Afinidad: {similitud})")

if __name__ == "__main__":
    probar_grafo()
