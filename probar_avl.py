import time
from estructuras.avl import AVL


class NodoBSTSimple:
    def __init__(self, clave):
        self.clave = clave
        self.izq = None
        self.der = None


class BSTSimple:
    def __init__(self):
        self.raiz = None

    def insertar(self, clave):
        self.raiz = self._insertar_rec(self.raiz, clave)

    def _insertar_rec(self, nodo, clave):
        if not nodo:
            return NodoBSTSimple(clave)
        if clave < nodo.clave:
            nodo.izq = self._insertar_rec(nodo.izq, clave)
        else:
            nodo.der = self._insertar_rec(nodo.der, clave)
        return nodo

    def obtener_altura(self, nodo):
        if not nodo:
            return 0
        return 1 + max(self.obtener_altura(nodo.izq), self.obtener_altura(nodo.der))


def probar_comparacion():
    print("Iniciando experimento de comparación entre BST simple y AVL...")

    datos_ordenados = [f"Libro {i:04d}" for i in range(1000)]

    bst = BSTSimple()
    avl = AVL()

    t_inicio = time.perfcounter()
    for d in datos_ordenados:
        bst.insertar(d)
    t_bst = (time.perfcounter() - t_inicio) * 1000

    t_inicio = time.perfcounter()
    for d in datos_ordenados:
        avl.insertar(d)
    t_avl = (time.perfcounter() - t_inicio) * 1000

    print(f"BST Simple -> Altura: {bst.obtener_altura(bst.raiz)} | Tiempo inserción: {t_bst:.4f} ms")
    print(f"Árbol AVL  -> Altura: {avl.obtener_altura(avl.raiz)} | Tiempo inserción: {t_avl:.4f} ms")
    print("Conclusion: El AVL mantiene una altura baja de ~10 niveles gracias a las rotaciones, mientras que el BST simple se degrada a una altura de 1000 niveles (O(N)).")


if __name__ == "__main__":
    probar_comparacion()
