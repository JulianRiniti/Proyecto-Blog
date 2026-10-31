from blog.datos import posts
from blog.menu import mostrar_menu
from blog.operaciones import listar_posts, buscar_por_titulo, filtrar_por_tag
from blog.validaciones import validar_post

if __name__ == "__main__":
    while True:
        opcion = mostrar_menu()

        if opcion == 1:
            listar_posts(posts)

        elif opcion == 2:
            termino = input("Ingrese el título a buscar: ").strip()
            buscar_por_titulo(posts, termino)

        elif opcion == 3:
            tag = input("Ingrese el tag a filtrar: ").strip()
            filtrar_por_tag(posts, tag)

        elif opcion == 4:
            print("\n--- VALIDACIÓN DE POSTS ---")
            for i, post in enumerate(posts, start=1):
                es_valido, error = validar_post(post)
                if es_valido:
                    print(f"Post {i}: válido")
                else:
                    print(f"Post {i}: error - {error}")

        elif opcion == 5:
            print("\n¡Gracias por usar el sistema de blog! Hasta luego.")
            break

        else:
            if opcion is not None:
                print("Opción inválida. Por favor, elija un número entre 1 y 5.")