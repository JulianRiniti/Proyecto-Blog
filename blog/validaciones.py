from blog.datos import estados_post

def validar_post(post):
    """Verifica si un post cumple con toda la estructura y reglas de negocio requeridas.
       Retorna (True, "") si es válido, o (False, mensaje_error) si tiene fallas."""
    
    if not isinstance(post, dict):
        return False, "el post no es un diccionario"

    claves_obligatorias = ["id", "titulo", "contenido", "autor", "tags", "estado"]
    for clave in claves_obligatorias:
        if clave not in post:
            return False, f"falta la clave '{clave}'"

    titulo = post.get("titulo")
    if not isinstance(titulo, str) or not titulo.strip():
        return False, "el título está vacío o no es texto"

    contenido = post.get("contenido")
    if not isinstance(contenido, str) or not contenido.strip():
        return False, "el contenido está vacío o no es texto"

    autor = post.get("autor")
    if not isinstance(autor, dict):
        return False, "el autor no es un diccionario"
    if "nombre" not in autor:
        return False, "al autor le falta la clave 'nombre'"

    tags = post.get("tags")
    if not isinstance(tags, list):
        return False, "el campo 'tags' no es una lista"

    estado = post.get("estado")
    if estado not in estados_post:
        return False, f"el estado '{estado}' no es válido"

    return True, ""