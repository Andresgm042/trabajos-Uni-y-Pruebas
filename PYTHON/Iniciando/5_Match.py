while True:  #bucle infinito, como el while (1) en C.

    Numero = int(input("Inserte numero: "))

    match (Numero):
        case 0: 
                print("Se inserto numero 0.")
        case Numero if Numero % 2 == 0: #% Residuo del resultado de la division
            print("El numero es par.")
        case Numero if Numero % 2 != 0:
            print("Numero no es par.")
        case _:
            print("Numero no reconocido.")

