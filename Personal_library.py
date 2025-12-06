library = [
    ["La novela de Genji", "Murasaki Shikibu", "Histórica"],
    ["El elogio de la sombra", "Junichirō Tanizaki", "Ficción"],
    ["Indigno de ser humano", "Osamu Dazai", "Novela"],
    ["Kokoro", "Natsume Soseki", "Romance"],
    ["El color prohibido", "Yukio Mishima", "Erótico"]
]

while True:
    print("\nSistema de Gestión de Biblioteca")
    print("1. Agregar libro")
    print("2. Mostrar libros")
    print("3. Buscar libro")
    print("4. Eliminar libro")
    print("5. Salir")
    
    opcion = input("Ingrese una opción: ").strip()
    
    if opcion == "1":
        while True:
            name = input("Ingrese el nombre del libro: ").strip()
            if name:
                break
            print("El nombre no puede estar vacío.")
        
        while True:
            author = input("Ingrese el autor del libro: ").strip()
            if author:
                break
            print("El autor no puede estar vacío.")

        while True:
            category = input("Ingrese la categoría del libro: ").strip()
            if category:
                break
            print("La categoría no puede estar vacía.")
        
        library.append([name, author, category])
        print(f"Libro '{name}' agregado correctamente.")
    
    elif opcion == "2":
        if not library:
            print("No hay libros registrados.")
        else:
            print("\nLibros registrados:")
            for i, libro in enumerate(library, start=1):
                print(f"{i}. Nombre: {libro[0]}, Autor: {libro[1]}, Categoría: {libro[2]}")
    
    elif opcion == "3":
        search = input("Ingrese el nombre del libro a buscar: ").strip().lower()
        result = []
        
        for libro in library:
            if search in libro[0].lower():
                result.append(libro)
        
        if result:
            print("\nLibros encontrados:")
            for l in result:
                print(f"Nombre: {l[0]}, Autor: {l[1]}, Categoría: {l[2]}")
        else:
            print("No se encontraron libros con ese nombre.")
    
    elif opcion == "4":
        if not library:
            print("No hay libros para eliminar.")
        else:
            print("\nLibros registrados:")
            for i, libro in enumerate(library, start=1):
                print(f"{i}. Nombre: {libro[0]}, Autor: {libro[1]}, Categoría: {libro[2]}")
            
            delete = input("Ingrese el número del libro a eliminar: ").strip()
            if not delete.isdigit():
                print("Debe ingresar un número válido.")
                continue
            
            delete = int(delete)
            if 1 <= delete <= len(library):
                deleted = library.pop(delete - 1)
                print(f"Libro '{deleted[0]}' eliminado correctamente.")
            else:
                print("Número fuera de rango.")
    
    elif opcion == "5":
        print("Saliendo del sistema...")
        break
    
    else:
        print("Opción inválida. Por favor, ingrese un número del 1 al 5.")
