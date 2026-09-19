Import time

class nodo:
  def __init__(self, libro):
    self.libro = libro
    self.izquierdo = None
    self.derecho = None

class ArbolBusqueda:
  def __init__(self):
    self.raiz = None

  #Ordenamos de forma alfabetica.
  def insert(self, libro):
    self.raiz = self._insert(self.raiz, libro)

  def insert(self, nodo, libro):_
    if nodo is None
      return nodo(libro)
    
titulo_nuevo = libro.get_titulo().lower()
    titulo_actual = nodo.libro.get_titulo().lower()

#Al estar ordenados de forma alfabetica los que vengan antes, estaran ordenados del lado izquierdo.
    if titulo_nuevo < titulo_actual:
      nodo.izquierdo = self._insert(nodo.izquierdo, libro)
 #Y caso contrario, los que vengan despues, estaran ordenados del lado derecho.     
    elif titulo_nuevo > titulo_actual:
      nodo.derecho = self._insert(nodo.derecho, libro)
    return nodo

def buscar(self, titulo_buscado):
  return selfg.buscar(self.raiz, titulo_buscado.lower))

def buscar(self, nodo, titulo_buscado):
#Si no encontramos el libro buscado, devolvemos que el libro no existe.
  if nodo is None:
    return None

  titulo_actual =nodo.libro.get_titulo().lower()

#En caso de que encontremos el libro buscado, devolvemos el libro.
if titulo_buscado == titulo_actual:
  return nodo.libro

if titulo_buscdado < tiutulo_actual:
  return self.buscar(nodo.izquierdo, titulo_buscado)

return self._buscar(nodo.derecho, titulo_buscado])
