# Proyecto Blog - Preentrega 6 (POO y Persistencia JSON)

Sistema de blog por consola desarrollado en Python, refactorizado utilizando Programación Orientada a Objetos (POO) y persistencia de datos mediante archivos JSON.

## Estructura del Proyecto
El proyecto mantiene una estructura modular y organizada en paquetes:
- `main.py`: Punto de entrada principal que coordina el menú interactivo con la clase `Blog`.
- `posts.json`: Archivo externo para la persistencia de las publicaciones.
- `blog/`: Paquete que contiene la lógica del sistema:
  - `modelos.py`: Define las clases principales del sistema (`Autor`, `Post` y `Blog`).
  - `datos.py`: Se encarga de la serialización, carga y guardado de los datos hacia `posts.json`.
  - `operaciones.py` / `validaciones.py`: Módulos de soporte para listados, búsquedas y validaciones.

## Clases Principales
1. **Autor**: Representa al creador del post (`nombre`, `bio`), permitiendo serialización y deserialización a diccionarios.
2. **Post**: Representa una publicación individual (`id`, `titulo`, `contenido`, `autor`, `tags`, `estado`), conteniendo una instancia de la clase `Autor`.
3. **Blog**: Centraliza la colección de publicaciones (`posts`) y expone métodos para listar, buscar por título, filtrar por etiqueta y agregar nuevos posts.

## Cómo Ejecutar el Programa
1. Asegurate de tener activado tu entorno virtual (`venv`).
2. Ejecutá el script principal desde la terminal:
   ```bash
   python main.py