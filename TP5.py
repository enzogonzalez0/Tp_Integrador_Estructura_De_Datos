# clase nodo para el arbol general
class NodoArbolGeneral:
    def __init__(self, nombre):
        self.nombre = nombre
        self.hijos = [] 

# clase arbol general
class ArbolGeneral:
    def __init__(self, raiz_nombre=None):
        if raiz_nombre:
            self.raiz = NodoArbolGeneral(raiz_nombre)
        else:
            self.raiz = None

    def agregar_raiz(self, nombre):
        if not self.raiz:
            self.raiz = NodoArbolGeneral(nombre)
        return self.raiz

    def agregar_hijo(self, nombre_padre, nombre_hijo):
        padre = self.buscar_nodo(nombre_padre)
        if padre:
            nuevo_hijo = NodoArbolGeneral(nombre_hijo)
            padre.hijos.append(nuevo_hijo)
            return True
        return False

    def buscar_nodo(self, nombre):
        return self._buscar_rec(self.raiz, nombre)

    def _buscar_rec(self, nodo_actual, nombre):
        if not nodo_actual:
            return None
        if nodo_actual.nombre.lower() == nombre.lower():
            return nodo_actual

        for hijo in nodo_actual.hijos:
            resultado = self._buscar_rec(hijo, nombre)
            if resultado:
                return resultado
        return None

    # recorrido en profundidad
    def recorrido_profundidad(self):
        resultado = []
        self._dfs_rec(self.raiz, resultado)
        return resultado

    def _dfs_rec(self, nodo_actual, resultado):
        if nodo_actual:
            resultado.append(nodo_actual.nombre)
            for hijo in nodo_actual.hijos:
                self._dfs_rec(hijo, resultado)

    # recorrido en anchura
    def recorrido_anchura(self):
        if not self.raiz:
            return []

        resultado = []
        cola = [self.raiz]

        while cola:
            nodo_actual = cola.pop(0)
            resultado.append(nodo_actual.nombre)
            for hijo in nodo_actual.hijos:
                cola.append(hijo)

        return resultado
