import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt 

fashion_mnist = tf.keras.datasets.fashion_mnist #Importamos el dataset de fashion_mnist
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data() #Cargamos el dataset de fashion_mnist

class_names = ['Camiseta/top', 'Pantalones', 'Jersey', 'Vestido', 'Abrigo',
               'Sandalia', 'Camisa', 'Zapatilla', 'Bolso', 'Botín']

# Crear una nueva figura
#plt.figure()
# Mostrar la primera imagen del conjunto de entrenamiento
#plt.imshow(train_images[0])
# Añadir una barra de color a la imagen
#plt.colorbar()
# Desactivar la cuadrícula
#plt.grid(False)
# Mostrar la imagen
#plt.show()

test_images = test_images / 255.0 #Normalizamos los datos de test
train_images = train_images / 255.0 #Normalizamos los datos de entrenamiento

plt.figure(figsize=(10,10)) #Creamos una figura de 10x10
for i in range(25): #Mostramos 25 imagenes
    plt.subplot(5,5,i+1) #esto es para mostrar las imagenes en una matriz de 5x5 en posicion i+1
    plt.xticks([]) #Quitar marcas en el eje x
    plt.yticks([]) #Quitar marcas en el eje y	
    plt.grid(False) #Quitar cuadricula
    plt.imshow(train_images[i], cmap=plt.cm.binary) #Mostrar imagen en escala de grises (blanco y negro)
    plt.xlabel(class_names[train_labels[i]]) #para poner nombre debajo
plt.show()

#se construye la red neuronal
model = tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)), #son 784 neuronas de entrada (28x28). flatten "aplana" 
    tf.keras.layers.Dense(128, activation='relu'), #128 neuronas en la capa oculta
    tf.keras.layers.Dense(10, activation='softmax') #10 neuronas en la capa de salida salida
])

# Compilar el modelo
model.compile(optimizer='adam', # Optimizador Adam
              loss='sparse_categorical_crossentropy', # Función de pérdida
              metrics=['accuracy']) # Métrica de precisión

print("Entrenando....")
model.fit(train_images, train_labels, epochs=10) #primero datos de entrada (imagenes), luego las etiquetas (que es lo que intenta aprender)
print("Modelo Entrenado")

# Evaluar el modelo en el conjunto de datos de prueba
test_loss, test_acc = model.evaluate(test_images, test_labels, verbose=2)

# Imprimir los resultados de la evaluación
print("Resultados:")
print(f'Pérdida en el conjunto de prueba: {test_loss}')
print(f'Precisión en el conjunto de prueba: {test_acc}')

while True:
    print("Hagamos una predicción")
    entrada = int(input("Escribe el indice de la imagen de prueba:")) # Pedir al usuario que ingrese el índice de la imagen de prueba

    prediccion = model.predict(test_images) # Obtener predicciones para el conjunto de prueba
    clase_predicha = np.argmax(prediccion[entrada]) # Clase predicha de la primera imagen

    # Imprimir la clase predicha
    print(f'Clase predicha para la primera imagen: {clase_predicha}')
    print(f'Nombre de la clase predicha: {class_names[clase_predicha]}')

    # Mostrar la imagen junto con el nombre de la clase predicha
    plt.figure()
    plt.imshow(test_images[entrada], cmap=plt.cm.binary) # Mostrar la primera imagen de prueba en escala de grises
    plt.title(f'Predicción: {class_names[clase_predicha]}') # Añadir el nombre de la clase predicha como título
    plt.xlabel(f'Clase real: {class_names[test_labels[entrada]]}') # Añadir el nombre de la clase real como etiqueta
    plt.show() # Mostrar la imagen