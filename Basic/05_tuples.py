# TUPLAS #

# DEFINICION

my_tuple = tuple() # ESTAS SON LAS DOS FORMAS DE DEFINIR TUPLAS, UN CONJUNTO DE VALORES
my_other_tuple = ()

my_tuple = (35, 1.77, "Brais", "Moure", "Brais")
my_other_tuple = (35, 60, 30)

print(my_tuple)
print(type(my_tuple))

# ACCESO A ELEMENTOS Y BUSQUEDA

print(my_tuple[0])
print(my_tuple[-1])
# print(my_tuple[4]) IndexError
# print(my_tuple[-6]) IndexError

print(my_tuple.count("Brais")) # MUESTRA CUANTOS BRAIS HAY EN LA TUPLA
print(my_tuple.index("Moure")) # MUESTRA EL INDICE O POSICION EN LA TUPLA
print(my_tuple.index("Brais")) 

# my_tuple[1] = 1.80 'tuple' object does not support item assignment

# DIFERENCIA: EN LA LISTA SE PUEDEN VARIAR Y LA TUPLA ES INMUTABLE

# CONCATENACION
print("Concateno las tuplas las sumo")
my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)

# SUBTUPLAS
print("")
print(my_sum_tuple[3:6]) # MUESTRA UNA SUBTUPLE DESDE LA POSICION 3 A LA 6 

# TUPLA MUTABLE CON CONVERSION A LISTA

my_tuple = list(my_tuple) # TRANSFORMO LA TUPLA A LISTA
print(type(my_tuple)) # MUESTRA EL TIPO

my_tuple[4] = "MoureDev" # AGREGO A MOUREDEV EN EL INDICE 4
my_tuple.insert(1, "Azul") # AGREGO AZUL EN LA POSICION 1
my_tuple = tuple(my_tuple) # LA VUELVE A PASAR A TUPLE
print(my_tuple) 
print(type(my_tuple)) # MUESTRA EL TIPO DE DATO, TUPLA

# ELIMINACION

# del my_tuple[2] TypeError: 'tuple' object doesn't support item deletion

del my_tuple # BORRA LA VARIABLE, Y MUESTRA QUE NO ESTA DEFINIDA

# print(my_tuple)  NameError: name 'my_tuple' is not defined
