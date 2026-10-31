
def mostrar_menu():
    """Muestra el menú principal y retorna la opción elegida por el usuario de forma segura."""
    print("\n--- MENU DEL BLOG ---")
    print("1. Ver todos los posts")
    print("2. Buscar por título")
    print("3. Filtrar por tag")
    print("4. Validar posts")
    print("5. Salir")
    
    try:
        opcion = int(input("Seleccione una opción (1-5): "))
        return opcion
    except ValueError:
        print("Error: Debe ingresar un número válido.")
        return None