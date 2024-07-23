# LIST COMPREHENSION #
print("")
my_original_list = [0, 1, 2, 3, 4, 5, 6, 7] # CREO UNA LISTA CON EL FORMATO TRADICIONAL
print(my_original_list) # MUSTRO LA LISTA

my_range = range(8) # DEFINO LA VARIABLE,CREO LA MISMA LISTA CON RANGE DANDOLE LOS 8 ELEMENTOS
print(list(my_range)) # ACA MUESTRO CON LA PALABRA RESERVADA LIST

# DEFINICION
print("")
my_list = [i + 1 for i in range(8)] # LE SUMA 1 A CADA ELEMENTO QUE TIENE LA LISTA Y LUEGO LOS MUESTRA
print(my_list)

my_list = [i * 2 for i in range(8)] # LE MULTIPLICO 2 A CADA ELEMENTO DE LA LISTA
print(my_list)

my_list = [i * i for i in range(8)] # LE MULTIPLICO EL MISMO ELEMENTO AL ELEMENTO
print(my_list)

def sum_five(number): # CREO UNA FUNCION QUE SUME 5 AL ELEMENTO
    return number + 5

my_list = [sum_five(i) for i in range(8)] # A LA VARIABLE MY_LIST LE INDICAMOS QUE EJECUTE LA FUNCION CON EL NUMERO DEL ELEMENTO
print(my_list) # QUE IMPRIMA EL VALOR DE LA VARIABLE (5, 6 ,7, 8, 9, 10, 11, 12)
