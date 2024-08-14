#funciones para las operaciones
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

while True:
    print("\n")
    numero1 = float(input("Escribe el primer número: "))
    numero2 = float(input("Escribe el segundo número: "))
    #menu de operaciones
    print("Operaciones:")
    print("1. Suma (+)")
    print("2. Resta (-)")
    print("3. Multiplicación (*)")
    print("4. División (/)")

    Eleccion = input("Selecciona operación a realizar (+, -, *, /): ")

    if Eleccion == "+" :
        print("\nResultado: ", suma(numero1, numero2))
    elif Eleccion == "-":
        print("\nResultado: ", resta(numero1, numero2))
    elif Eleccion == "*":
        print("\nResultado: ", multiplicacion(numero1, numero2))
    elif Eleccion == "/":
        print("\nResultado: ", division(numero1, numero2))
    else:
        print("Opción no válida")