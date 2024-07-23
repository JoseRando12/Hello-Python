# FUNCIONES #

# DEFINICION

def my_function():   # CON ESTO ES SUFICIENTE PARA DEFINIR UNA FUNCION 
    print("Esto es una función") # CREAMOS UM PRINT CON UN TEXTO


my_function() # LLAMAMOS A LA FUNCION 
my_function()
my_function()

# FUNCION CON PARAMETROS DE ENTRADA/ARGUMENTOS

print("")

def sum_two_values(first_value: int, second_value): # DEFINO LA FUNCION
    print(first_value + second_value) # TAREA SUMAR PRIMER VALUE CON EL SEGUNDO VALUE


sum_two_values(5, 7) # LLAMO LA FUNCION Y LE DOY LOS PARAMETROS, MUESTRA 12
sum_two_values(54754, 71231) # LLAMO A LA FUNCION CON ESTOS PARAMETROS, MUETRA 125985
sum_two_values("5", "7") # LE PASO 5 Y 7 COMO STRING, MUESTRA 57 LOS CONCATENA
sum_two_values(1.4, 5.2) # LE PASO 1.4 Y 5.2, MUESTRA 6.6

# FUNCION CON PARAMETROS DE ENTRADA/ARGUMENTOS Y RETORNO 

print("")
def sum_two_values_with_return(first_value, second_value):
    my_sum = first_value + second_value
    return my_sum


my_result = sum_two_values(1.4, 5.2)
print(my_result) # MUESTRA NONE

my_result = sum_two_values_with_return(10, 5) # ALMACENAMOS EN UNA VARIABLE EL RESULTADO DE LA FUNCION CON LOS PARAMETROS QUE LE INDICAMOS
print(my_result)

# FUNCION CON PARAMETROS DE ENTRADA7ARGUMENTOS POR CLAVE

print("")
def print_name(name, surname):
    print(f"{name} {surname}") # LE PASAMOS UN FORMATO A LA FUNCION


print_name(surname="Moure", name="Brais") # REORDENAMOS EL ORDEN PONIENDO LOS PARAMETROS DE LUGAR


# FUNCION CON PARAMETROS DE ENTRADA7ARGUMENTOS POR DEFECTO

print("")

def print_name_with_default(name, surname, alias="Sin alias"): # POR DEFECTO EL ALIAS ES SIN ALIAS
    print(f"{name} {surname} {alias}")


print_name_with_default("Brais", "Moure") # ACA LLAMO A LA FUNCION SIN ALIAS
print_name_with_default("Brais", "Moure", "MoureDev") # ACA LLAMO A LA FUNCION CON ALIAS


# FUNCION CON PARAMETROS DE ENTRADA7ARGUMENTOS ARBITRARIOS
print("")

def print_upper_texts(*texts): # AL PONER EL * LE INDICAMOS QUE PUEDEN SER CUALQUIER TEXTO
    print(type(texts))
    for text in texts: # ENTRA AL FOR Y LO PASA A MAYUSCULAS, Y ASI CON TODOS LOS PARAMETROS
        print(text.upper())


print_upper_texts("Hola", "Python", "MoureDev")
print_upper_texts("Hola")
