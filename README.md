# Sistema de Gestión de Biblioteca

Programa en Python que permite gestionar una biblioteca simple. Permite agregar, mostrar, buscar y eliminar libros desde la terminal.

## Características

- Agregar libros con **nombre**, **autor** y **categoría**.
- Mostrar todos los libros registrados.
- Buscar libros por nombre (búsqueda parcial o completa).
- Eliminar libros por número de lista.
- Manejo de entradas vacías para evitar errores.

## Requisitos

- Python 3.7 en adelante.

## Uso

1. Clonar o descargar el repositorio.
2. Abrir la terminal y navegar hasta la carpeta donde se encuentra el archivo *biblioteca.py*.
3. Ejecutar el programa con: python biblioteca.py

Se mostrará un menú con las siguientes opciones:

1. Agregar libro.
2. Mostrar libros.
3. Buscar libro.
4. Eliminar libro.
5. Salir.

## Detalles de las opciones

**Agregar libro:** Solicita el nombre, autor y categoría. Si se deja un campo vacío, el programa vuelve a pedirlo.

**Mostrar libros:** Lista todos los libros agregados con su número, nombre, autor y categoría.

**Buscar libro:** Permite buscar libros por nombre (la búsqueda no distingue mayúsculas/minúsculas).

**Eliminar libro:** Muestra los libros con número y permite eliminar uno seleccionando su número.

**Salir:** Termina la ejecución del programa.

## Ejemplo de uso

Sistema de Gestión de Biblioteca
1. Agregar libro
2. Mostrar libros
3. Buscar libro
4. Eliminar libro
5. Salir

- Ingrese una opción: 1
- Ingrese el nombre del libro: Kokoro
- Ingrese el autor del libro: Natsume Soseki
- Ingrese la categoría del libro: Romance
- Libro 'Kokoro' agregado correctamente.

## Notas

* Los libros se almacenan en memoria mientras el programa está en ejecución. Para que se guarden permanentemente, se puede agregar funcionalidad de guardado en archivos o bases de datos.
* Está diseñado para ejecutarse en la terminal y es compatible con sistemas Windows, macOS y Linux.

