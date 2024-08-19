class animales:
    def __init__(self, animal):
        self.animal = animal 
    
    def Animal(ABC):
        pass

class Perro(animales):
    def sonido(self):
        return "Guau"

class Gato(animales):
    def sonido(self):
        return "Miau"
    
canino = Perro("mongo")
felino = Gato("michi")

print(f"El perro se llama {canino.animal} y hace {canino.sonido()}")
print(f"El gat se llama {felino.animal} y hace {felino.sonido()}")