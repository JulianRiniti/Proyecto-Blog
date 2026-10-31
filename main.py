from blog.modelos import Blog, Post, Autor
from blog.datos import cargar_posts, guardar_posts

def main():
    # 1. Instanciamos el Blog y cargamos los datos desde el JSON
    mi_blog = Blog()
    posts_cargados = cargar_posts()
    for p in posts_cargados:
        mi_blog.agregar_post(p)

    print("¡Bienvenido al Sistema de Blog con POO!")

    while True:
        print("\n--- MENU DEL BLOG ---")
        print("1. Ver todos los posts")
        print("2. Buscar por titulo")
        print("3. Filtrar por tag")
        print("4. Crear nuevo post")
        print("5. Guardar posts en JSON")
        print("6. Salir")

        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            posts = mi_blog.listar_posts()
            if not posts:
                print("No hay posts cargados.")
            else:
                for p in posts:
                    print(f"- [ID: {p.id}] '{p.titulo}' por {p.autor.nombre} (Estado: {p.estado})")

        elif opcion == "2":
            busqueda = input("Ingresá el título a buscar: ")
            resultados = mi_blog.buscar_por_titulo(busqueda)
            if not resultados:
                print("No se encontraron coincidencias.")
            else:
                for p in resultados:
                    print(f"- Encontrado: '{p.titulo}' (Autor: {p.autor.nombre})")

        elif opcion == "3":
            tag = input("Ingresá el tag que querés filtrar: ")
            resultados = mi_blog.filtrar_por_tag(tag)
            if not resultados:
                print(f"No hay posts con el tag '{tag}'.")
            else:
                for p in resultados:
                    print(f"- '{p.titulo}' (Tags: {', '.join(p.tags)})")

        elif opcion == "4":
            print("\n--- Crear Nuevo Post ---")
            try:
                id_p = input("ID del post: ").strip()
                titulo = input("Título: ").strip()
                contenido = input("Contenido: ").strip()
                nombre_autor = input("Nombre del autor: ").strip()
                bio_autor = input("Biografía del autor (opcional): ").strip()
                tags_input = input("Tags (separados por comas): ").strip()
                tags = [t.strip() for t in tags_input.split(",")] if tags_input else []

                # Creamos el objeto Autor y el objeto Post
                nuevo_autor = Autor(nombre=nombre_autor, bio=bio_autor)
                nuevo_post = Post(id_post=id_p, titulo=titulo, contenido=contenido, autor=nuevo_autor, tags=tags, estado="publicado")

                # Lo agregamos al blog
                mi_blog.agregar_post(nuevo_post)
                print("¡Post creado con éxito en la memoria!")
            except Exception as e:
                print(f"Error al crear el post: {e}")

        elif opcion == "5":
            guardar_posts(mi_blog.listar_posts())
            print("¡Posts guardados exitosamente en posts.json!")

        elif opcion == "6":
            # Guardado automático al salir
            guardar_posts(mi_blog.listar_posts())
            print("¡Gracias por usar el sistema del blog! Saliendo...")
            break
        else:
            print("Opción inválida. Ingresá un número del 1 al 6.")

if __name__ == "__main__":
    main()