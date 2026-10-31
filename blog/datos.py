perfil_autor = {
    "nombre": "Julian Riniti",
    "bio": "Estudiante de Python",
    "especialidad": "Numeros y estadisticas",
    "redes sociales": ["@julianriniti", "@julianmatiasriniti"]
}

estados_post = ("borrador", "publicado", "archivado")

etiquetas_blog = {"Python", "Django", "Web", "Backend"}

posts = [
    {
        "id": 1,
        "titulo": "Primeros pasos con Python",
        "contenido": "video tutorial",
        "autor": perfil_autor,
        "tags": ["Python", "Principiantes"],
        "estado": "publicado"
    },
    {
        "id": 2,
        "titulo": "Qué es Django",
        "contenido": "manuales de estudio",
        "autor": perfil_autor,
        "tags": ["Python", "Django", "Web"],
        "estado": "borrador"
    },
    {
        "id": 3,
        "titulo": "Organizando datos con diccionarios",
        "contenido": "organizador de datos",
        "autor": perfil_autor,
        "tags": ["Python", "Diccionarios"],
        "estado": "archivado"
    },
    {
        "id": 4,
        "titulo": "",  # ERROR: Título vacío intencional
        # FALTA la clave "contenido" intencionalmente
        "autor": "Julian Riniti",  # ERROR: Autor como texto en vez de diccionario
        "tags": "Python",  # ERROR: Tags debería ser una lista y es string
        "estado": "invalido"  # ERROR: Estado que no pertenece a la tupla
    }
]