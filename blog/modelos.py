class Autor:
    def __init__(self, nombre, bio=""):
        self.nombre = nombre
        self.bio = bio

    def a_diccionario(self):
        """Convierte el objeto Autor a un diccionario para poder guardarlo en JSON."""
        return {
            "nombre": self.nombre,
            "bio": self.bio
        }

    @classmethod
    def desde_diccionario(cls, d):
        """Reconstruye un objeto Autor a partir de un diccionario cargado de JSON."""
        return cls(nombre=d.get("nombre", "Desconocido"), bio=d.get("bio", ""))


class Post:
    def __init__(self, id_post, titulo, contenido, autor, tags=None, estado="borrador"):
        self.id = id_post
        self.titulo = titulo
        self.contenido = contenido
        self.autor = autor 
        self.tags = tags if tags is not None else []
        self.estado = estado

    def a_diccionario(self):
        """Convierte el post y su autor a diccionarios para guardar en JSON."""
        return {
            "id": self.id,
            "titulo": self.titulo,
            "contenido": self.contenido,
            "autor": self.autor.a_diccionario(),  
            "tags": self.tags,
            "estado": self.estado
        }

    @classmethod
    def desde_diccionario(cls, d):
        """Reconstruye un Post y su Autor a partir de un diccionario."""
        autor_data = d.get("autor", {})
        if isinstance(autor_data, dict):
            autor_obj = Autor.desde_diccionario(autor_data)
        else:
            autor_obj = Autor(nombre=str(autor_data))

        return cls(
            id_post=d.get("id"),
            titulo=d.get("titulo", ""),
            contenido=d.get("contenido", ""),
            autor=autor_obj,
            tags=d.get("tags", []),
            estado=d.get("estado", "borrador")
        )


class Blog:
    def __init__(self):
        self.posts = []  # Lista que contendrá objetos de tipo Post

    def agregar_post(self, post):
        self.posts.append(post)

    def listar_posts(self):
        return self.posts

    def buscar_por_titulo(self, texto):
        texto = texto.lower()
        return [p for p in self.posts if texto in p.titulo.lower()]

    def filtrar_por_tag(self, tag):
        tag = tag.lower()
        return [p for p in self.posts if any(tag == t.lower() for t in p.tags)]