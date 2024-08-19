class calculadora:
    def __init__(self, num): #metodo de inicializacion
        self.resultado = num
        
    def suma (self, num):
        self.resultado += num

    def resta (self, num):
        self.resultado -= num
    
    def multi (self, num):
        self.resultado *= num

    def division (self, num):
        if num != 0 :
            self.resultado /= num
        else:
            print("Error: Division por 0")

    def resultado (self):
        return self.resultado  
    
calculo = calculadora(0)
calculo.suma(5)
calculo.resta(2)
calculo.multi(4)
calculo.division(2)

resultado = calculo.resultado
print("Resultado es:", resultado)
