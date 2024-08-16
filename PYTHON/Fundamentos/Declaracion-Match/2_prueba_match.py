while True:
    num = int(input("Escribe numero a clasificar:"))
    match num:
        case num if num < 0:
            print("El numero ingresado es menor a 0.")
        case num if 0 <= num < 10:
            print("El numero ingresado esta entre 0 y 10.")
        case num if num >= 10:
            print("El numero ingresado es igual o mayor a 10.")