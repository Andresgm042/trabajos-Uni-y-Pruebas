from machine import Pin, PWM
from time import sleep_ms

freq = 50  # 20ms
servo = PWM(Pin(5), freq)

while True:
    # Solicitar al usuario que ingrese el nuevo valor del ciclo de trabajo
    new_duty = int(input("Ingrese el nuevo valor de ciclo de trabajo (21-131): "))

    # Asegurarse de que el valor esté dentro del rango permitido
    new_duty = min(1023, max(21, new_duty))

    # Configurar el nuevo ciclo de trabajo
    servo.duty(new_duty)
    
    # Imprimir el valor del ciclo de trabajo actual
    print("Ciclo de trabajo actual:", new_duty)

    # Esperar un tiempo antes de solicitar el próximo valor
    sleep_ms(100)  # Espera 100 milisegundos antes de solicitar el próximo valor