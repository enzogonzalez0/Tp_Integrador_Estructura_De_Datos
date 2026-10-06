import time

class NodoAVL:
  # representa cada elemento guardado dentro del arbol AVL. Ademas de los punteros a izquierda y derecha.
    def __init__(self, libro):
        self.libro = libro
        self.clave = libro.get_titulo().lower() if hasattr(libro, "get_titulo") else str(libro).lower()
        self.izquierda = None  
        self.derecha = None    
        self.altura = 1       

# clase principal
class AVL:
    
    def __init__(self):
        self.raiz = None  

    # funciones auxiliares de altura y balance
    def obtener_altura(self, nodo):
        if not nodo:
            return 0
        return nodo.altura

    def obtener_balance(self, nodo):
        if not nodo:
            return 0
        return self.obtener_altura(nodo.izquierda) - self.obtener_altura(nodo.derecha)

    # rotaciones para restaurar el balance 
    def _rotacion_derecha(self, y):
        x = y.izquierda
        T2 = x.derecha
        x.derecha = y
        y.izquierda = T2
        y.altura = 1 + max(self.obtener_altura(y.izquierda), self.obtener_altura(y.derecha))
        x.altura = 1 + max(self.obtener_altura(x.izquierda), self.obtener_altura(x.derecha))

        return x  

    def _rotacion_izquierda(self, x):
        y = x.derecha
        T2 = y.izquierda
        y.izquierda = x
        x.derecha = T2
        x.altura = 1 + max(self.obtener_altura(x.izquierda), self.obtener_altura(x.derecha))
        y.altura = 1 + max(self.obtener_altura(y.izquierda), self.obtener_altura(y.derecha))

        return y  

    # intersecion balanceada
    def insertar(self, libro):
        self.raiz = self._insertar_recursivo(self.raiz, libro)

    def _insertar_recursivo(self, nodo, libro):
        clave = libro.get_titulo().lower() if hasattr(libro, "get_titulo") else str(libro).lower()
        if not nodo:
            return NodoAVL(libro)

        if clave < nodo.clave:
            nodo.izquierda = self._insertar_recursivo(nodo.izquierda, libro)
        elif clave > nodo.clave:
            nodo.derecha = self._insertar_recursivo(nodo.derecha, libro)
        else:
            return nodo

        nodo.altura = 1 + max(self.obtener_altura(nodo.izquierda), self.obtener_altura(nodo.derecha))
        balance = self.obtener_balance(nodo)
      
        if balance > 1 and clave < nodo.izquierda.clave:
            return self._rotacion_derecha(nodo)

        if balance < -1 and clave > nodo.derecha.clave:
            return self._rotacion_izquierda(nodo)
          
        if balance > 1 and clave > nodo.izquierda.clave:
            nodo.izquierda = self._rotacion_izquierda(nodo.izquierda)
            return self._rotacion_derecha(nodo)

        if balance < -1 and clave < nodo.derecha.clave:
            nodo.derecha = self._rotacion_derecha(nodo.derecha)
            return self._rotacion_izquierda(nodo)

        return nodo 
      
    # busqueda eficiente
    def buscar(self, titulo):
        return self._buscar_recursivo(self.raiz, titulo.lower())

    def _buscar_recursivo(self, nodo, clave):
        if not nodo or nodo.clave == clave:
            return nodo.libro if nodo else None
        
        if clave < nodo.clave:
            return self._buscar_recursivo(nodo.izquierda, clave)
        return self._buscar_recursivo(nodo.derecha, clave)

    # recorridos del arbol
    def inorder(self):
        resultado = []
        self._inorder_rec(self.raiz, resultado)
        return resultado

    def _inorder_rec(self, nodo, resultado):
        if nodo:
            self._inorder_rec(nodo.izquierda, resultado)
            resultado.append(nodo.libro)
            self._inorder_rec(nodo.derecha, resultado)

    def preorder(self):
        resultado = []
        self._preorder_rec(self.raiz, resultado)
        return resultado

    def _preorder_rec(self, nodo, resultado):
        if nodo:
            resultado.append(nodo.libro)
            self._preorder_rec(nodo.izquierda, resultado)
            self._preorder_rec(nodo.derecha, resultado)

    def postorder(self):
        resultado = []
        self._postorder_rec(self.raiz, resultado)
        return resultado

    def _postorder_rec(self, nodo, resultado):
        if nodo:
            self._postorder_rec(nodo.izquierda, resultado)
            self._postorder_rec(nodo.derecha, resultado)
            resultado.append(nodo.libro)
