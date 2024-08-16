frase = "escribo cualquier cosa"
longitud = len(frase) #len cuenta el número de elementos (caracteres, digitos)
print(longitud)

palabras = frase.split() #.split divide una cadena en una lista de palabras
print(palabras)
mayuscula = frase.upper()
print(mayuscula)     #convierte a mayuscula
minuscula = frase.lower()
print(minuscula)   #convierte a minuscula

frase2 = "otra cosa"
print(frase2)
cambio = frase2.replace("cosa", "palabra")  #("-lo que quiero cambiar-", "-el cambio-")
print(cambio)

for x in frase2:
    print(x)