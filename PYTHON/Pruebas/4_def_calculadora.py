# Definir funciones para las operaciones
def suma(x, y):
    return x + y

def resta(x, y):
    return x - y

def multiplicacion(x, y):
    return x * y

def division(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: División por cero"

def main():
    print("Operaciones:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")

    Eleccion = input("Selecciona operación a realizar (1 - 4): ")

    if Eleccion in ["1", "2", "3", "4"]:  # Verifica si la opción es válida
        numero1 = float(input("Escribe el primer número: "))
        print(numero1)
        numero2 = float(input("Escribe el segundo número: "))
        print(numero2)

        if Eleccion == "1":
            print("Resultado: ", suma(numero1, numero2))
        elif Eleccion == "2":
            print("Resultado: ", resta(numero1, numero2))
        elif Eleccion == "3":
            print("Resultado: ", multiplicacion(numero1, numero2))
        elif Eleccion == "4":
            print("Resultado: ", division(numero1, numero2))
    else:
        print("Opción no válida")

if __name__ == "__main__":
    main()
