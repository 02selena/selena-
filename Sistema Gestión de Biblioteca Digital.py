# Clase Libro
class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.titulo_autor = (titulo, autor)  # Usamos tupla para el título y autor
        self.categoria = categoria
        self.isbn = isbn
    
    def __str__(self):
        return f"'{self.titulo_autor[0]}' por {self.titulo_autor[1]}, Categoría: {self.categoria}, ISBN: {self.isbn}"


# Clase Usuario
class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []  # Lista para los libros prestados

    def prestar_libro(self, libro):
        self.libros_prestados.append(libro)

    def devolver_libro(self, libro):
        if libro in self.libros_prestados:
            self.libros_prestados.remove(libro)

    def __str__(self):
        return f"Usuario: {self.nombre}, ID: {self.id_usuario}, Libros prestados: {len(self.libros_prestados)}"


# Clase Biblioteca
class Biblioteca:
    def __init__(self):
        self.libros = {}  # Diccionario con ISBN como clave y objeto Libro como valor
        self.usuarios = {}  # Diccionario con ID de usuario como clave y objeto Usuario como valor
        self.ids_usuarios = set()  # Conjunto para IDs únicos de usuarios

    def añadir_libro(self, libro):
        if libro.isbn not in self.libros:
            self.libros[libro.isbn] = libro
            print(f"Libro añadido: {libro}")
        else:
            print("El libro ya existe en la biblioteca.")

    def quitar_libro(self, isbn):
        if isbn in self.libros:
            del self.libros[isbn]
            print(f"Libro con ISBN {isbn} ha sido removido.")
        else:
            print("El libro no existe en la biblioteca.")

    def registrar_usuario(self, usuario):
        if usuario.id_usuario not in self.ids_usuarios:
            self.usuarios[usuario.id_usuario] = usuario
            self.ids_usuarios.add(usuario.id_usuario)
            print(f"Usuario registrado: {usuario}")
        else:
            print("El usuario ya está registrado.")

    def dar_de_baja_usuario(self, id_usuario):
        if id_usuario in self.usuarios:
            del self.usuarios[id_usuario]
            self.ids_usuarios.remove(id_usuario)
            print(f"Usuario con ID {id_usuario} ha sido dado de baja.")
        else:
            print("El usuario no está registrado.")

    def prestar_libro(self, id_usuario, isbn):
        if id_usuario in self.usuarios and isbn in self.libros:
            usuario = self.usuarios[id_usuario]
            libro = self.libros[isbn]
            usuario.prestar_libro(libro)
            del self.libros[isbn]  # Remover el libro de los disponibles
            print(f"Libro '{libro.titulo_autor[0]}' prestado a {usuario.nombre}.")
        else:
            print("Usuario o libro no encontrado.")

    def devolver_libro(self, id_usuario, isbn, libro):
        if id_usuario in self.usuarios:
            usuario = self.usuarios[id_usuario]
            usuario.devolver_libro(libro)
            self.libros[isbn] = libro  # Devolver el libro a la biblioteca
            print(f"Libro '{libro.titulo_autor[0]}' devuelto por {usuario.nombre}.")
        else:
            print("Usuario no encontrado.")

    def buscar_libro(self, filtro, valor):
        resultados = [str(libro) for libro in self.libros.values() if getattr(libro, filtro) == valor]
        if resultados:
            print("Libros encontrados:")
            for resultado in resultados:
                print(resultado)
        else:
            print("No se encontraron libros con ese criterio.")

    def listar_libros_prestados(self, id_usuario):
        if id_usuario in self.usuarios:
            usuario = self.usuarios[id_usuario]
            if usuario.libros_prestados:
                print(f"Libros prestados a {usuario.nombre}:")
                for libro in usuario.libros_prestados:
                    print(libro)
            else:
                print(f"{usuario.nombre} no tiene libros prestados.")
        else:
            print("Usuario no encontrado.")


# Ejemplo de uso

# Crear libros
libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", "Ficción", "9788497592208")
libro2 = Libro("Don Quijote de la Mancha", "Miguel de Cervantes", "Clásico", "9788491050829")

# Crear usuarios
usuario1 = Usuario("Juan Pérez", "001")
usuario2 = Usuario("María González", "002")

# Crear biblioteca
biblioteca = Biblioteca()

# Añadir libros a la biblioteca
biblioteca.añadir_libro(libro1)
biblioteca.añadir_libro(libro2)

# Registrar usuarios
biblioteca.registrar_usuario(usuario1)
biblioteca.registrar_usuario(usuario2)

# Prestar libro
biblioteca.prestar_libro("001", "9788497592208")

# Listar libros prestados
biblioteca.listar_libros_prestados("001")

# Devolver libro
biblioteca.devolver_libro("001", "9788497592208", libro1)

# Buscar libros por categoría
biblioteca.buscar_libro("categoria", "Clásico")
