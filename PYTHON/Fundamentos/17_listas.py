lista_num = [1, 2, 3 ,4 , 5]
lista_str = ["yo", "buenas", "FPGA"]
lista_mixta = [1, "dato str", 3.99]

print(lista_num[2]) #imprime tercer dato de la lista
print("lista str sin cambio:", lista_str)
lista_str[0] = "TU" #reemplaza el primer dato de la lista 
print("lista con cambio en el primer dato:", lista_str)

#.append para agregar datos a la lista
lista_num.append(10)
lista_str.append("microcontrolador")
print("lista de enteros con el dato agregado:", lista_num)
print("lista de str con el dato agregado:", lista_str)

#del para eliminar un dato 
del lista_num[0]     #elimina primer dato de la lista
print("lista de enteros con dato borrado:", lista_num)