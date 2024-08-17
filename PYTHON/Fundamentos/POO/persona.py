class persona: #Palabra reservada que se utiliza para definir una nueva clase
    def __init__(self, nombre, edad): #metodo por defecto
        self.nombre = nombre
        self.edad = edad

    def saludar(self): #metodo
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")

#instancia de la clase persona
persona1 = persona("Juan", 30)
persona1 = persona1.saludar()

#otra instancia persona
persona2 = persona("Maria", 25)

#llamar metodo saludar
persona2.saludar()
