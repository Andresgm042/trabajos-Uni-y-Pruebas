class calculadora:
    def suma (self, num1, num2):
        return num1 + num2

    def resta (self,num1, num2):
        return num1 - num2
    
    def multi (self, num1, num2):
        return num1 * num2
    
    def divi (self, num1, num2):
        if num2 == 0:
            return num1 / num2
        else:
            "Error: division por 0"

num1 = int(input("Numero 1:" ))
num2 = int(input("Numero 2: "))

Calculadora = calculadora()

resultado_suma = Calculadora.suma(num1, num2)
resultado_resta = Calculadora.resta(num1, num2)
resultado_multi = Calculadora.multi(num1, num2)
resultado_divi = Calculadora.divi(num1, num2)

print(resultado_suma)
print(resultado_resta)
print(resultado_multi)
print(resultado_divi)

