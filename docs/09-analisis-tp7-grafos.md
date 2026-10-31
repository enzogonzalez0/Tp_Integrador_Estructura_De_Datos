Definicion y Justificacion de Vértices:
Definicion: Cada vértice del grafo representa una obra literaria (libro) individual disponible en el catálogo del sistema BookFinder.
Justificacion: Se adopta esta abstracción porque el nucleo del sistema consiste en relacionar elementos del catalogo en función de sus caracteristicas temáticas y similitudes de contenido.

Definicion y Justificacion de Aristas:
Definicion: Una arista indica la conexion o relacion de similitud existente entre dos libros del catalogo.
Justificacion: Permite modelar de forma directa qué titulos comparten generos, universos narrativos o autores, habilitando la navegacion en red para las recomendaciones por afinidad.

Tipo de Grafo: ¿Dirigido o No Dirigido? no Dirigido
Justificacion: Se selecciona un grafo no dirigido porque la relacion de similitud entre libros es simetrica: si el libro A está relacionado con el libro B por compartir genero o tematica, conceptualmente el libro B se relaciona de la misma manera con el A. Se descarta un grafo dirigido, ya que no existe una dependencia unidireccional (como un "enlace de prelación" o una jerarquía estricta) donde la relación vaya de un sentido sin retorno.

Tipo de Grafo: ¿Pesado o No Pesado? Pesado
Justificación: Se opta por un grafo pesado incorporando un valor numerico en las aristas (por ejemplo, un peso de 0 a 1) que representa el grado de afinidad o similitud entre las obras. Se descarta un grafo no pesado, ya que tratar todas las conexiones por igual impediria diferenciar si dos libros son altamente compatibles o si su relación es meramente marginal, restandole precision al sistema de recomendacion.

Representacion: Lista de Adyacencia
Justificacion: Se utiliza una lista de adyacencia (implementada mediante un diccionario de diccionarios en Python). Se opta por esta estructura porque el grafo de recomendaciones es un grafo disperso (de baja densidad), ya que un libro se relaciona unicamente con un subconjunto acotado de obras afines y no con todo el catalogo. Esto la hace altamente eficiente en uso de memoria y en tiempo de busqueda de vecinos comparada con una matriz de adyacencia.
