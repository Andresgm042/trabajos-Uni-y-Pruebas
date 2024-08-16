# Solicita al usuario que ingrese un dato
entrada = input("Introduce un dato: ")

# Verifica si la entrada es numérica
if entrada.isdigit():
    print("El dato ingresado es numérico (int).")
else:
    print("El dato ingresado es una cadena de texto (str).")

"""
    if (A == 1): hacer esto
    elif (B == 2): hacer aquello
    else: si no se cumple ninguna de las condiciones anteriores, hacer otra cosa
"""
