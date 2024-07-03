# main.py

# Clase base Vehiculo
class Vehiculo:
    def __init__(self, marca, modelo):
        self._marca = marca  # Atributo encapsulado
        self._modelo = modelo  # Atributo encapsulado

    # Método para obtener la marca
    def get_marca(self):
        return self._marca

    # Método para obtener el modelo
    def get_modelo(self):
        return self._modelo

    # Método que será sobrescrito en la clase derivada (Polimorfismo)
    def descripcion(self):
        return f"Vehículo de marca {self._marca} y modelo {self._modelo}"


# Clase derivada Coche
class Coche(Vehiculo):
    def __init__(self, marca, modelo, num_puertas):
        super().__init__(marca, modelo)  # Llamada al constructor de la clase base
        self.num_puertas = num_puertas

    # Sobrescribir el método descripcion (Polimorfismo)
    def descripcion(self):
        return f"Coche de marca {self._marca}, modelo {self._modelo} y con {self.num_puertas} puertas"


# Crear instancias de las clases y demostrar la funcionalidad
def main():
    # Crear una instancia de Vehiculo
    vehiculo1 = Vehiculo("Toyota", "Corolla")
    print(vehiculo1.descripcion())

    # Crear una instancia de Coche
    coche1 = Coche("Honda", "Civic", 4)
    print(coche1.descripcion())


if __name__ == "__main__":
    main()
