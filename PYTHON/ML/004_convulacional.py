import cv2
import tensorflow as tf
import os
import numpy as np

cap = cv2.VideoCapture(0)

lfw_path = "/home/jetson/Downloads/lfw/lfw-deepfunneled/lfw-deepfunneled"
my_path = "/home/jetson/Codigos/dataset_galindo"

#------------------------------------------------------------------------

def obt_frame():
    ret, frame = cap.read()
    if not ret or frame is None:
        print("Error en camara, a saber que...")
        return None
    return frame

def cargar_img(path, size=(250,250)):
    imagenes = []
    etiquetas = []

    for person in os.listdir(path):#recorre la carpeta
        person_path = os.path.join(path, person)#entra, directorio completo
        if os.path.isdir(person_path):#si es carpeta
            for img_name in os.listdir(person_path):#recorre imegenes
                img = cv2.imread(os.path.join(person_path, img_name))

                if img is not None:
                    img = cv2.resize(img, size)  # Redimensiona a 250x250
                    img = img / 255.0  # Normaliza (0 a 1)
                    imagenes.append(img)
                    etiquetas.append(0)  # Etiqueta 0 para LFW
        
        elif os.path.isfile(person_path):#si es archivo
            for img_name in os.listdir(person_path):#recorre imegenes
                img = cv2.imread(os.path.join(person_path, img_name))

                if img is not None:
                    img = cv2.resize(img, size)  # Redimensiona a 250x250
                    img = img / 255.0  # Normaliza (0 a 1)
                    imagenes.append(img)
                    etiquetas.append(0)  # Etiqueta 0 para LFW    

    if len(imagenes) == 0:
        print(f"En algo la cague: No se encontraron imágenes en {path}")

    return np.array(imagenes), np.array(etiquetas)
    #return np.array(imagenes, dtype=np.float32), np.array(etiquetas, dtype=np.int32)


#------------------------------------------------------------------------

lfw_images, lfw_labels = cargar_img(lfw_path)
my_images, my_labels = cargar_img(my_path)

# Unir listas verticalmente
X = np.concatenate((lfw_images, my_images), axis=0)
y = np.concatenate((lfw_labels, my_labels), axis=0)

#bueh, a configurar modelo convulacional

modelo = tf.keras.Sequential([

    #primera capa convulacional
#le aplica 32 filtros, Cada filtro es una pequeña ventana de 3x3 píxeles que se mueve 
#sobre la imagen, detectando características
    tf.keras.layers.Conv2D(32,(3,3),activation='relu',input_shape=(250,250,3)),
#reduccion de tamaño, reduce la img a la mitad. para que aprenda mas rapido pues.
    tf.keras.layers.MaxPooling2D(pool_size=(2,2)),

    #segunda capa convulacional
    tf.keras.layers.Conv2D(64,(3,3), activation='relu'),
    tf.keras.layers.MaxPooling2D(pool_size=(2,2)),

    #convierte la imagen en un vector 1D, lo "aplana" 
    tf.keras.Flatten(),

    #capa densa oculta
    tf.keras.layers.Dense(128, activation='relu'),

    #capa de salida con activación sigmoide (para clasificación binaria)
#sigmoide porque solo quiero que diga si soy yo o no
    tf.keras.layers.Dense(1, activation='sigmoid')
])

#compilacion del modelo
modelo.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Mostramos la estructura del modelo
modelo.summary()

print(f"Imágenes de LFW: {lfw_images.shape[0]}")
print(f"Imágenes tuyas: {my_images.shape[0]}")
