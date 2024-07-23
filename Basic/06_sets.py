# SETS #

# DEFINICION

my_set = set() # UN SETS TIENE DE BASE UNA ARRAIZ, PYTHON NO TIENE ARRAIZ O SEA ES UNA LISTA
my_other_set = {} # DECLARO UN DICCIONARIO

print(type(my_set)) # ES TIPO DE DATO SET
print(type(my_other_set))  # Inicialmente es un diccionario

my_other_set = {"Brais", "Moure", 35}
print(type(my_other_set))

print(len(my_other_set)) # CUENTA LOS ELEMENTOS

# INSERCION

print("")
print(my_other_set) # IMPRIMO EL ORIGINAL
my_other_set.add("MoureDev") # LE AGREGO UN ELEMENTO Y ABAJO LO MUESTRO

print(my_other_set)  # Un set no es una estructura ordenada

my_other_set.add("MoureDev")  # Un set no admite repetidos

print(my_other_set)


# BUSQUEDA
print("Moure" in my_other_set) # DEVUELVE TRUE
print("Mouri" in my_other_set) # DEVUELVE FALSE


# ELIMINACION
print(my_other_set)
my_other_set.remove("Moure") # ELIMINO MOURE
print(my_other_set)

my_other_set.clear()
print(len(my_other_set)) # TENEMOS 0 ELEMENTOS, EL CLEAR LOS ELIMINA

# del my_other_set # BORRA LA PROPIEDAD SET
# print(my_other_set) NameError: name 'my_other_set' is not defined

# TRANSFORMACION
print("")
my_set = {"Brais", "Moure", 35}
my_list = list(my_set)
print(my_list)
print(my_list[0])

my_other_set = {"Kotlin", "Swift", "Python"}

# OTRAS OPERACIONES
print("OTRAS OPERACIONES")
my_new_set = my_set.union(my_other_set)
print(my_new_set.union(my_new_set).union(my_set).union({"JavaScript", "C#"}))
print(my_new_set.difference(my_set))

