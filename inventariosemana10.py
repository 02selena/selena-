import os

class Inventario:
    def __init__(self, archivo='inventario.txt'):
        self.archivo = archivo
        self.productos = {}
        self.cargar_inventario()

    def agregar_producto(self, codigo, nombre, cantidad, precio):
        self.productos[codigo] = {'nombre': nombre, 'cantidad': cantidad, 'precio': precio}
        self.guardar_inventario()

    def actualizar_producto(self, codigo, nombre=None, cantidad=None, precio=None):
        if codigo in self.productos:
            if nombre is not None:
                self.productos[codigo]['nombre'] = nombre
            if cantidad is not None:
                self.productos[codigo]['cantidad'] = cantidad
            if precio is not None:
                self.productos[codigo]['precio'] = precio
            self.guardar_inventario()
        else:
            print(f"Producto con código {codigo} no encontrado.")

    def eliminar_producto(self, codigo):
        if codigo in self.productos:
            del self.productos[codigo]
            self.guardar_inventario()
        else:
            print(f"Producto con código {codigo} no encontrado.")

    def mostrar_inventario(self):
        for codigo, datos in self.productos.items():
            print(f"Código: {codigo}, Nombre: {datos['nombre']}, Cantidad: {datos['cantidad']}, Precio: {datos['precio']}")

    def cargar_inventario(self):
        if os.path.exists(self.archivo):
            try:
                with open(self.archivo, 'r') as archivo:
                    for linea in archivo:
                        partes = linea.strip().split(',')
                        if len(partes) == 4:
                            codigo, nombre, cantidad, precio = partes
                            self.productos[codigo] = {
                                'nombre': nombre,
                                'cantidad': int(cantidad),
                                'precio': float(precio)
                            }
            except (FileNotFoundError, PermissionError) as e:
                print(f"Error al leer el archivo de inventario: {e}")
        else:
            print("Archivo de inventario no encontrado. Se creará uno nuevo.")

    def guardar_inventario(self):
        try:
            with open(self.archivo, 'w') as archivo:
                for codigo, datos in self.productos.items():
                    linea = f"{codigo},{datos['nombre']},{datos['cantidad']},{datos['precio']}\n"
                    archivo.write(linea)
        except (FileNotFoundError, PermissionError) as e:
            print(f"Error al escribir en el archivo de inventario: {e}")
          





def main():
    inventario = Inventario()

    while True:
        print("\nOpciones:")
        print("1. Agregar producto")
        print("2. Actualizar producto")
        print("3. Eliminar producto")
        print("4. Mostrar inventario")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            codigo = input("Código del producto: ")
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            inventario.agregar_producto(codigo, nombre, cantidad, precio)
            print("Producto agregado exitosamente.")
        elif opcion == '2':
            codigo = input("Código del producto a actualizar: ")
            nombre = input("Nuevo nombre (dejar en blanco para no cambiar): ") or None
            cantidad = input("Nueva cantidad (dejar en blanco para no cambiar): ")
            cantidad = int(cantidad) if cantidad else None
            precio = input("Nuevo precio (dejar en blanco para no cambiar): ")
            precio = float(precio) if precio else None
            inventario.actualizar_producto(codigo, nombre, cantidad, precio)
            print("Producto actualizado exitosamente.")
        elif opcion == '3':
            codigo = input("Código del producto a eliminar: ")
            inventario.eliminar_producto(codigo)
            print("Producto eliminado exitosamente.")
        elif opcion == '4':
            inventario.mostrar_inventario()
        elif opcion == '5':
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()

