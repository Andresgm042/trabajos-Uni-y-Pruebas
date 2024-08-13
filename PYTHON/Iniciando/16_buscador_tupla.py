palabra = ("cerveza", "coca-cola", "yogurt", "hamburguesa")

while True:   
    palabra_buscar = input("Inserte palabra a buscar:")
    if  palabra_buscar in palabra:
        print("la palabra ingresada esta en la tupla")
    else:
        print("la palabra ingresada no esta en la tupla")