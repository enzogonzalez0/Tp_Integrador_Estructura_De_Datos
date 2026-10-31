# TP6: Cola de Prioridad / Heap Binario 

class HeapMax:
    def __init__(self):
        self.elementos = []  #

    def _padre(self, i):
        return (i - 1) // 2

    def _hijo_izq(self, i):
        return 2 * i + 1

    def _hijo_der(self, i):
        return 2 * i + 2

    def insertar(self, prioridad, item):
        """Inserta un elemento con su respectiva prioridad y reajusta el heap."""
        self.elementos.append((prioridad, item))
        self._flotar(len(self.elementos) - 1)

    def _flotar(self, i):
        """Sube el elemento si es mayor que su padre (propiedad de Max-Heap)."""
        padre = self._padre(i)
        while i > 0 and self.elementos[i][0] > self.elementos[padre][0]:
            self.elementos[i], self.elementos[padre] = self.elementos[padre], self.elementos[i]
            i = padre
            padre = self._padre(i)

    def obtener_cima(self):
        """Devuelve el elemento con mayor prioridad sin extraerlo."""
        if not self.elementos:
            return None
        return self.elementos[0]

    def extraer_cima(self):
        """Extrae y devuelve el elemento máximo, reestructurando el heap."""
        if not self.elementos:
            return None
        if len(self.elementos) == 1:
            return self.elementos.pop()

        raiz = self.elementos[0]
        self.elementos[0] = self.elementos.pop()
        self._hundir(0)
        return raiz

    def _hundir(self, i):
        """Baja el elemento si es menor que alguno de sus hijos."""
        mayor = i
        izq = self._hijo_izq(i)
        der = self._hijo_der(i)
        n = len(self.elementos)

        if izq < n and self.elementos[izq][0] > self.elementos[mayor][0]:
            mayor = izq
        if der < n and self.elementos[der][0] > self.elementos[mayor][0]:
            mayor = der

        if mayor != i:
            self.elementos[i], self.elementos[mayor] = self.elementos[mayor], self.elementos[i]
            self._hundir(mayor)

    def obtener_top_n(self, n):
        """Devuelve los N elementos con mayor prioridad de forma eficiente."""
        copia_heap = list(self.elementos)
        resultado = []
        temp_heap = HeapMax()
        temp_heap.elementos = list(self.elementos)
        
        for _ in range(min(n, len(temp_heap.elementos))):
            resultado.append(temp_heap.extraer_cima())
            
        return resultado

    def __len__(self):
        return len(self.elementos)
