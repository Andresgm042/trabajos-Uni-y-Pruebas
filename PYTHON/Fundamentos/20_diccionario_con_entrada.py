#"nombre", "edad", "direccion" y "telefono".
datos_personales = {
    "Nombre" : None,
    "Edad" : None,
    "Direccion" : None,
    "Telefono" : None
}

datos_personales["Nombre"] = input("Inserte Nombre: ")
datos_personales["Edad"] = input("Inserte Edad: ")
datos_personales["Direccion"] = input("Inserte Direccion: ")
datos_personales["Telefono"] = input("Inserte Telefono: ")

print("\n")
print("Tu nombre es", datos_personales["Nombre"])
print("Tienes", datos_personales["Edad"], "años de edad") 
print("Tu direccion es", datos_personales["Direccion"]) 
print("Tu numero telefonico es", datos_personales["Telefono"])