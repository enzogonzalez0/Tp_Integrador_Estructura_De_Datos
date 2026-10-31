# script de prueba para el TP6
from estructuras.heap import HeapMax

def probar_heap():
    print("--- PRUEBA DE COLA DE PRIORIDAD (MAX-HEAP) - BOOKFINDER ---")
    
    ranking_libros = HeapMax()
    
    libros_con_rating = [
        (9.8, "Matrix (Edición Especial)"),
        (9.6, "Inception: Guía de Diseño"),
        (9.5, "Interstellar: Ciencia y Ficción"),
        (9.2, "Blade Runner: Director's Cut"),
        (9.0, "Ex Machina"),
        (8.5, "El Eternauta"),
        (9.9, "Dune: Parte 1")
    ]
    
    print("\nInsertando elementos en el Heap...")
    for rating, titulo in libros_con_rating:
        ranking_libros.insertar(rating, titulo)
        print(f"Insertado: {titulo} (Rating: {rating})")
        
    print(f"\nTotal de elementos en el Heap: {len(ranking_libros)}")
    
    print("\n--- TOP 5 DE ELEMENTOS MEJOR PUNTUADOS ---")
    top_5 = ranking_libros.obtener_top_n(5)
    
    for i, (rating, titulo) in enumerate(top_5, start=1):
        medalla = "🥇" if i == 1 else "🥈" if i == 2 else "🥉" if i == 3 else f"{i}."
        print(f"{medalla} {titulo} - Puntuación: {rating}")

if __name__ == "__main__":
    probar_heap()
