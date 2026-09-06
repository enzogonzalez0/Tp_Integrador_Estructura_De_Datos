# Tp_Integrador_Estructura_De_Datos
# Repositorio destinado al desarrollo del trabajo practico Estructura de Datos

## Entrega 1: TP0 — Propuesta del Proyecto

### 1. Nombre del Proyecto y Dominio Elegido
* **Nombre del proyecto:** BookFinder 
* **Dominio:** Gestión bibliográfica y recomendación personalizada de libros.
* **Justificación:** Se eligio este dominio porque permite aplicar estructuras de datos para organizar colecciones de informacion (listas, diccionarios) junto con algoritmos de busqueda, filtrado y ordenamiento segun criterios de puntuación.

### 2. Problema que Resuelve y Usuario Objetivo
* **Problema:** La dificultad de organizar catalogos bibliograficos y la falta de mecanismos eficientes para descubrir lecturas basadas en preferencias o calificaciones previas.
* **Usuario Objetivo:** Estudiantes, lectores frecuentes y administradores de pequeñas bibliotecas.

### 3. Funcionalidades Iniciales
1. **Carga y persistencia:** Lectura y guardado de libros desde un archivo JSON.
2. **Búsqueda general:** Busqueda de libros por coincidencia en título o autor.
3. **Filtrado dinámico:** Filtrado por genero literario y calificación minima.
4. **Gestión de catálogo:** Alta (agregar) y baja (eliminar) de libros.
5. **Sistema de recomendación:** Generación de un ranking ordenado por puntaje segun generos preferidos.

### 4. Boceto de la Interfaz de Terminal
```text
========================================
    SISTEMA DE GESTIÓN DE BIBLIOTECA
========================================
1. Listar todos los libros
2. Buscar libro (por título o autor)
3. Filtrar por género / calificación
4. Agregar libro
5. Eliminar libro
6. Generar Recomendaciones
0. Salir

Seleccione una opción: _
classDiagram
    class Libro {
        - str id
        - str titulo
        - str autor
        - str genero
        - float calificacion
        - int anio
        + to_dict()
        + from_dict(data)
    }

    class Biblioteca {
        - list libros
        + cargar_desde_json(ruta)
        + guardar_en_json(ruta)
        + agregar_libro(libro)
        + eliminar_libro(id)
        + buscar(texto)
        + filtrar(genero, calificacion)
    }

    class SistemaRecomendacion {
        + recomendar(biblioteca, genero, calificacion_min)
    }

    Biblioteca "1" *-- "many" Libro
    SistemaRecomendacion ..> Biblioteca
