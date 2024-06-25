# Programa para calcular el índice de masa corporal (IMC)

def calcular_imc(peso_kg, altura_m):
    """
    Calcula el índice de masa corporal (IMC) dado el peso en kg y la altura en metros.

    :param peso_kg: Peso de la persona en kilogramos (float)
    :param altura_m: Altura de la persona en metros (float)
    :return: Valor del IMC calculado (float)
    """
    imc = peso_kg / (altura_m ** 2)
    return imc


# Función principal
def main():
    # Solicitar al usuario que ingrese el peso y la altura
    peso = float(input("Ingresa tu peso en kg: "))
    altura = float(input("Ingresa tu altura en metros: "))

    # Calcular el IMC utilizando la función calcular_imc
    indice_imc = calcular_imc(peso, altura)

    # Mostrar el resultado del IMC
    print(f"Tu índice de masa corporal (IMC) es: {indice_imc:.2f}")


if __name__ == "__main__":
    main()
