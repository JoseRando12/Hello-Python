# LISTAS

# DEFINICION

my_list = list() # LISTA = ARRAIZ = ARREGLOS
my_other_list = [] # ASI TMB ES UNA LISTA

print(len(my_list)) # MUESTRA LA LONGITUD DE LA LISTA, 0
print(" ")
my_list = [35, 24, 62, 52, 30, 30, 17] # PASO ESTOS DATOS AL ARRAIZ

print(my_list) # IMPRIME TODO LO QUE TIENE EL ARRAIZ
print(len(my_list)) # IMPRIME LA LONGUITUD DEL ARRAIZ
print(" ")
my_other_list = [35, 1.77, "Brais", "Moure"]

print(type(my_list)) # IMPRIME EL TIPO LA CLASE, LIST
print(type(my_other_list)) # IMPRIME EL TIPO LA CLASE, LIST
print(" ")

# ACCESO A ELEMENTOS Y BUSQUEDA
print("ACCESO A ELEMENTOS Y BUSQUEDA")
print(my_other_list[0]) # MUESTRA 35
print(my_other_list[1]) # MUESTRA 1.77
print(my_other_list[-1]) # MOURE
print(my_other_list[-4]) # 35
print(my_list.count(30)) # MUESTRA CUANTAS VECES SE REPITE ESE NUMERO, O SEA 2
# print(my_other_list[4]) IndexError 
# print(my_other_list[-5]) IndexError
print(" ")
print(my_other_list.index("Brais"))

age, height, name, surname = my_other_list # REDEFINIMOS LA VARIABLE
print(name) # MUESTRA BRAIS

name, height, age, surname = my_other_list[2], my_other_list[1], my_other_list[0], my_other_list[3]
print(age) # REFEDINIMOS LA LISTA CON LA POSICION DE LA LISTA, Y MUESTRA SEGUN LO QUE INDIQUEMOS
print(" ")
# CONCATENACION

print(my_list + my_other_list) # MUESTRA LAS DOS LISTAS CONCATENADAS
#print(my_list - my_other_list)
print(" ")

# CREACION, INSERCION, ACTUALIZACION Y ELEIMINACION
print("CREACION, INSERCION, ACTUALIZACION Y ELEIMINACION")

my_other_list.append("MoureDev") # CREA O AÑADE UN ELEMENTO EN LA LISTA
print(my_other_list)

my_other_list.insert(1, "Rojo") # INSERTA EN LA POSICION 1 AL ROJO Y EL RESTO SE CORREN
print(my_other_list)

my_other_list[1] = "Azul" # ACTUALIZA LA POSICION 1 CON AZUL
print(my_other_list)

my_other_list.remove("Azul") # ELIMINA AZUL DE LA LISTA
print(my_other_list)

my_list.remove(30) # ELIMINA EL PRIMER 30 QUE ENCUENTRA DE LA LISTA
print(my_list) #MUESTRA LA LISTA
print(" ")
print(my_list.pop()) # SACA DE LA LISTA EL ULTIMO ELEMENTO CON POP EL 17 Y LO MUESTRA
print(my_list) # IMPRIMIMOS LA LISTA Y YA NO ESTA EL 17
print(" ")

my_pop_element = my_list.pop(2) # GUARDAMOS EL ELEMETO EN UN VARIABLE, LE INDICAMOS QUE REALICE UN POP DEL ELEMENTO 2
print(my_pop_element) # MUESTRA EL ELEMENTO 2 QUE FUE ELIMINADO DE LA LISTA ALOJADO EN LA VARIABLE
print(my_list) # MUESTRA LA LISTA SIN EL ELEMENTO 2

del my_list[2] # ELIMINO EL INDICE 2 DE LA LISTA
print(my_list) # IMPRIMO LA LISTA

# OPERACIONES CON LISTAS

print("OPERACIONES CON LISTAS")
my_new_list = my_list.copy() # COPIA LA LISTA EN UNA VARIABLE LLAMADA my_new_list

my_list.clear() # BORRA my_list
print(my_list) # LA MUESTRA Y ESTA VACIA
print(my_new_list,"LISTA ORIGINAL") # IMPRIME LA OTRA LISTA Y ESTA CON LA COPIA QUE LE HABIAMOS ECHO

my_new_list.reverse() # LE INDICAMOS UN REVERSE
print(my_new_list) # MUESTRA LA LISTA DE REVERSA

my_new_list.sort() # LE INDICAMOS QUE LA ORDENA CON SORT
print(my_new_list) # LA MUESTRA ORDENADA
print(" ")

# SUBLISTAS

print(my_new_list[1:3]) # MUESTRA EL ELEMENTO QUE ESTA ENTRE ESOS NUMEROS INDICADOS

# CAMBIO DE TIPO

my_list = "Hola Python" # LE CAMBIAMOS EL TIPO DE DATO
print(my_list)
print(type(my_list))
