class palabras:
    def __init__(self):
        self.count = 0  # Inicializa el contador en 0

    def contador(self, texto):
        frase = texto.split()  # Esto divide el texto en palabras usando el espacio como delimitador
        self.count += len(frase)  # Cuenta el número de palabras obtenidas con .split() y las añade al contador

    def resultado(self):
        return self.count  # Devuelve el valor actual del contador

frase_count = palabras()
frase = "lo que sea, no se"
frase_count.contador(frase)
print(f"Nº de palabras:", frase_count.resultado())
