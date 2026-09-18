import time

#Algoritmo de Busqueda Secuencial
#Recorre la lista elemento por elemento. Complejidad: O(N)
def busqueda_secuencial(lista_libros, titulo_buscado):
    titulo_buscado = titulo_buscado.lower()
    for libro in lista_libros:
        if libro.get_titulo().lower() == titulo_buscado:
            return libro
    return None

#Experimentacion / Medicion de tiempos
#Mide el tiempo de ejecucion en milisegundos
def ejecutar_experimento_secuencial(lista_libros, titulo_a_buscar):
    inicio = time.perfcounter()
    resultado = busqueda_secuencial(lista_libros, titulo_a_buscar)
    fin = time.perfcounter()
    
    tiempo_ms = (fin - inicio) * 1000  
    return tiempo_ms

#Bloque de pruebas con 1.000, 10.000 y 100.000 elementos para la tabla
if __name__ == "__main__":
    tamanios = [1000, 10000, 100000]
    
    for n in tamanios:
        lista_prueba = [Libro(f"Libro {i}") for i in range(n)]

#Busca el ultimo elemento para evaluar el peor caso O(N)
        buscado = f"Libro {n - 1}"
        
        tiempo = ejecutar_experimento_secuencial(lista_prueba, buscado)
        print(f"N = {n} elementos -> Tiempo: {tiempo:.4f} ms")
