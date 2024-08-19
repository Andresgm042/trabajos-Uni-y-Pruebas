class vehiculos:
    def __init__(self, marca, modelo):  #clase padre 
        self.marca = marca
        self.modelo = modelo
    
    def arrancar(self):
        return f"{self.marca} {self.modelo} esta arrancando" 
    
class coche(vehiculos): #clase hijo
    def acelerar(self):
        return f"{self.marca} {self.modelo} esta acelerando"
    
class motocicleta(vehiculos):
    def acrobacia(self):
        return f"{self.marca} {self.modelo} esta haciendo una acrobacia"
    
auto = coche("Toyota", "Camary")
moto = motocicleta("Honda", "XR")

print(f"Coche, marca y modelo: {auto.marca}, {auto.modelo}")
print(f"Motocicleta, marca y modelo: {moto.marca}, {moto.modelo}")

print(auto.acelerar())
print(moto.arrancar())

#polimorfismo
print(auto.arrancar())
print(moto.arrancar())