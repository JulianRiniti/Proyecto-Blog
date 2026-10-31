import json
import os
from blog.modelos import Post

RUTA_JSON = "posts.json"

def cargar_posts():
    """Carga los posts desde el archivo JSON y los convierte en objetos Post."""
    if not os.path.exists(RUTA_JSON):
        return []
    
    try:
        with open(RUTA_JSON, "r", encoding="utf-8") as archivo:
            contenido = archivo.read()
            if not contenido.strip():
                return []
            datos = json.loads(contenido)
            return [Post.desde_diccionario(p) for p in datos]
    except (json.JSONDecodeError, Exception) as e:
        print(f"Aviso: No se pudo leer el archivo de datos correctamente ({e}). Se iniciará vacío.")
        return []

def guardar_posts(posts):
    """Recibe la lista de objetos Post, los pasa a diccionarios y los guarda en JSON."""
    try:
        datos = [p.a_diccionario() for p in posts]
        with open(RUTA_JSON, "w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f"Error al intentar guardar los posts: {e}")