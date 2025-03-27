import tensorflow as tf #libreria para machine learning
import numpy as np #libreria para analisis de datos y calculos
import matplotlib.pyplot as plt #libreria para graficar

celsius = np.array([-40, -10, 0, 8, 15, 22, 38], dtype=float) #array de numpy con los valores de celsius
fahrenheit = np.array([-40, 14, 32, 46, 59, 72, 100], dtype=float)#lo mismo de arriba pero de fahrenheit

capa = tf.keras.layers.Dense(units=1, input_shape=[1]) #capa de la red neuronal, units neurona de salida 
modelo = tf.keras.Sequential([capa]) #modelo de la red neuronal

modelo.compile(  #compilacion del modelo
    optimizer=tf.keras.optimizers.Adam(0.1), #optimizador de la red neuronal
    loss='mean_squared_error' #funcion de perdida, en este caso error cuadratico medio
)

print("Comenzando entrenamiento...")    
historial = modelo.fit(celsius, fahrenheit, epochs=800, verbose=False) #entrenamiento de la red neuronal, epochs cantidad de veces que se va a entrenar, verbose=False para que no muestre el proceso
print("Modelo entrenado!")

plt.xlabel("# Epoca") #nombre del eje x
plt.ylabel("Magnitud de perdida") #nombre del eje y
plt.plot(historial.history["loss"]) #grafica de la perdida
plt.show() #mostrar la grafica

while True:
    print("Prediccion de la red neuronal: ")
    entrada = float(input("Escribe el valor en celsius: ")) #valor de entrada
    entrada_array = np.array([entrada]) #valor de entrada en un array de numpy
    resultado = modelo.predict(entrada_array) #prediccion de la red neuronal
    print("El resultado es ", str(resultado), "fahrenheit") #mostrar el resultado 

    print("Pesos de la red neuronal: ", capa.get_weights()) #mostrar los pesos de la red neuronal