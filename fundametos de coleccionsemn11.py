class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id_producto}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}"

       def get_id(self):
               return self.id_producto

           def get_nombre(self):
                      return self.nombre

                 def get_cantidad(self):
                          return self.cantidad

                 def get_precio(self):
                           return self.precio
   
                        def set_nombre(self, nombre):
                                       self.nombre = nombre

                       def set_cantidad(self, cantidad):
                                   self.cantidad = cantidad

                           def set_precio(self, precio):
                                              self.precio = precio
  

import json

class Inventario:
    def __init__(self):
        self.productos = {}

    def añadir_producto(self, producto):
        self.productos[producto.get_id()] = producto

    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
        else:
            print("Producto no encontrado.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        if id_producto in self.productos:
            producto = self.productos[id_producto]
            if cantidad is not None:
                producto.set_cantidad(cantidad)
            if precio is not None:
                producto.set_precio(precio)
        else:
            print("Producto no encontrado.")

    def buscar_producto_por_nombre(self, nombre):
        encontrados = [producto for producto in self.productos.values() if nombre.lower() in producto.get_nombre().lower()]
        return encontrados

    def mostrar_todos_los_productos(self):
        for producto in self.productos.values():
            print(producto)

    def guardar_en_archivo(self, nombre_archivo):
        with open(nombre_archivo, 'w') as archivo:
            productos_serializados = {id: producto.__dict__ for id, producto in self.productos.items()}
            json.dump(productos_serializados, archivo, indent=4)

    def cargar_desde_archivo(self, nombre_archivo):
        with open(nombre_archivo, 'r') as archivo:
            productos_serializados = json.load(archivo)
            self.productos = {id: Producto(**datos) for id, datos in productos_serializados.items()}



def menu():
    inventario = Inventario()
    archivo = "inventario.json"

    while True:
        print("\n--- Sistema de Gestión de Inventario ---")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar todos los productos")
        print("6. Guardar inventario")
        print("7. Cargar inventario")
        print("8. Salir")
        
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            id_producto = input("ID del producto: ")
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.añadir_producto(producto)
            print("Producto añadido.")
        
        elif opcion == "2":
            id_producto = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)
            print("Producto eliminado.")
        
        elif opcion == "3":
            id_producto = input("ID del producto a actualizar: ")
            cantidad = input("Nueva cantidad (deja en blanco para no cambiar): ")
            precio = input("Nuevo precio (deja en blanco para no cambiar): ")
            inventario.actualizar_producto(id_producto, cantidad=int(cantidad) if cantidad else None, precio=float(precio) if precio else None)
            print("Producto actualizado.")
        
        elif opcion == "4":
            nombre = input("Nombre del producto a buscar: ")
            productos_encontrados = inventario.buscar_producto_por_nombre(nombre)
            if productos_encontrados:
                for producto in productos_encontrados:
                    print(producto)
            else:
                print("No se encontraron productos con ese nombre.")
        
        elif opcion == "5":
            inventario.mostrar_todos_los_productos()
        
        elif opcion == "6":
            inventario.guardar_en_archivo(archivo)
            print("Inventario guardado.")
        
        elif opcion == "7":
            inventario.cargar_desde_archivo(archivo)
            print("Inventario cargado.")
        
        elif opcion == "8":
            break
        
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    menu()
