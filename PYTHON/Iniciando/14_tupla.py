tupla = (("Julio", 16), ("Felipe", 20), ("Adrian", 19))
#las tuplas son parecidas a listas pero son inmutables

for nombre, edad in tupla:
    if edad > 18:
        print(f"Se llama {nombre} y tiene {edad} años") #f es para formatos (.__format__)