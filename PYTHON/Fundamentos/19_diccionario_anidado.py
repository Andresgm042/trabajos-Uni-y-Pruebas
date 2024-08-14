# Diccionario anidado
personas = {
    "persona1":{
        "nombre" : "Juan",
        "edad" : 18,
        "ciudad" : "Guaduas"
    },
    "persona2":{
        "nombre" : "Julio",
        "edad" : 20,
        "ciudad" : "Honda"
    },
    "persona3":{
        "nombre" : "Julian",
        "edad" : 22,
        "ciudad" : "La paz"
    }
}

datos = personas["persona2"]
print(datos)
print(datos["nombre"])

persona = {
    "nombre" : None,
    "edad" : None,
    "ciudad" : None
}
#rellenar diccionario
persona["nombre"] = input("nombre: ")
persona["edad"] = input("edad: ")
persona["ciudad"] = input("ciudad: ")

print(persona)