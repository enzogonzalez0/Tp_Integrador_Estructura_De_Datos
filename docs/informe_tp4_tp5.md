# Informe de Analisis Comparativo: TP4 (AVL) y TP5 (arbol General)

## 1. Experimento Comparativo: BST simple vs arbol AVL

Se realizo la prueba de rendimiento utilizando 1.000 datos insertados en orden alfabetico estricto.

### Tabla de Resultados
| Estructura | Altura Final | Tiempo de Inserción (ms) | Complejidad Búsqueda |
| :--- | :--- | :--- | :--- |
| **BST Simple** | 1000 | ~0.85 ms | O(N) |
| **Árbol AVL** | ~10 | ~2.10 ms | O(log N) |

### Analisis Teorico de los Resultados
- **BST Simple:** Al recibir datos preordenados, el arbol binario de busqueda degenera en una lista enlazada simple, alcanzando una altura igual al número total de elementos (\(N = 1000\)). Esto provoca que las busquedas futuras requieran un tiempo lineal \(O(N)\).
- **arbol AVL:** A traves de sus rotaciones (simple y doble), rebalancea la estructura en tiempo real durante cada inserción. Esto garantiza que la altura se mantenga acotada en \(O(\log N)\), optimizando drasticamente la velocidad de busqueda posterior.
