
def listar_posts(lista):
    """Recorre la lista de posts y muestra el título y el autor de cada uno."""
    print("\n--- Posts disponibles ---")
    for post in lista:
        titulo = post.get("titulo", "Sin título")
        autor_dict = post.get("autor", {})
        
        if isinstance(autor_dict, dict):
            nombre_autor = autor_dict.get("nombre", "Desconocido")
        else:
            nombre_autor = "Desconocido"
            
        print(f"- {titulo} | Autor: {nombre_autor}")


def buscar_por_titulo(lista, termino):
    """Busca publicaciones cuyo título contenga el término ingresado (ignorando mayúsculas/minúsculas)."""
    if not termino:
        print("La búsqueda no puede estar vacía.")
        return

    termino_minuscula = termino.lower()
    encontrado = False

    print(f"\n--- Resultados de la búsqueda: '{termino}' ---")
    for post in lista:
        titulo = post.get("titulo", "")
        if isinstance(titulo, str) and termino_minuscula in titulo.lower():
            autor_dict = post.get("autor", {})
            nombre_autor = autor_dict.get("nombre", "Desconocido") if isinstance(autor_dict, dict) else "Desconocido"
            print(f"Encontrado: {titulo} | Autor: {nombre_autor}")
            encontrado = True

    if not encontrado:
        print("No se encontraron posts con ese título.")


def filtrar_por_tag(lista, tag):
    """Filtra y muestra solo los posts que contengan el tag indicado (ignorando mayúsculas/minúsculas)."""
    if not tag:
        print("El tag a filtrar no puede estar vacío.")
        return

    tag_buscado = tag.lower()
    encontrado = False

    print(f"\n--- Posts con la etiqueta '{tag}' ---")
    for post in lista:
        tags = post.get("tags", [])
        if isinstance(tags, list):
            tags_minuscula = [t.lower() for t in tags if isinstance(t, str)]
            if tag_buscado in tags_minuscula:
                titulo = post.get("titulo", "Sin título")
                estado = post.get("estado", "desconocido")
                print(f"- {titulo} | Estado: {estado}")
                encontrado = True

    if not encontrado:
        print("No se encontraron posts con ese tag.")