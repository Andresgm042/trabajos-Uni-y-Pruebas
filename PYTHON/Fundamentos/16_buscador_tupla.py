palabra = ("cerveza", "coca-cola", "yogurt", "hamburguesa")

while True:   
    palabra_buscar = input("Inserte palabra a buscar:")
    if  palabra_buscar == palabra:  #puedo poner in en vez de == y tendre el mismo resultado 
        print("la palabra ingresada esta en la tupla")
    else:
        print("la palabra ingresada no esta en la tupla")