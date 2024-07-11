import os


class FileHandler:
    def __init__(self, filename):
        self.filename = filename
        self.file = None  # Inicializamos el atributo file

        try:
            self.file = open(self.filename, 'r')  # Intentamos abrir el archivo en modo lectura
            print(f"Archivo '{self.filename}' abierto correctamente.")
        except IOError as e:
            print(f"No se pudo abrir el archivo '{self.filename}': {e}")

    def read_content(self):
        if self.file:
            return self.file.read()
        else:
            return "No se pudo leer el archivo. No está abierto correctamente."

    def __del__(self):
        if self.file:
            self.file.close()  # Cerramos el archivo en el destructor si está abierto
            print(f"Archivo '{self.filename}' cerrado correctamente.")
        else:
            print(f"No se requirió cerrar el archivo '{self.filename}'.")


# Ejemplo de uso
def main():
    # Creamos una instancia de FileHandler
    file_handler = FileHandler("ejemplo.txt")

    # Intentamos leer el contenido del archivo
    content = file_handler.read_content()
    print(f"Contenido del archivo: {content}")

    # La instancia de FileHandler se destruirá al salir del bloque main
    # El destructor se llamará automáticamente para cerrar el archivo


if __name__ == "__main__":
    main()
