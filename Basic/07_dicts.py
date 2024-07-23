# DICCIONARIOS #

# DEFINICION

my_dict = dict() # ES UNA ESTRUCTURA QUE PODEMOS ALMACENAR DATOS DE TIPO CLASE VALOR
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {"Nombre": "Brais", "Apellido": "Moure", "Edad": 35, 1: "Python"}

my_dict = {
    "Nombre": "Brais",
    "Apellido": "Moure",
    "Edad": 35,
    "Lenguajes": {"Python", "Swift", "Kotlin"},
    1: 1.77
}

print(my_other_dict)
print(my_dict)

print(len(my_other_dict))
print(len(my_dict))

# BUSQUEDA
print("BUSCAMOS")
print(my_dict[1]) # TIENE ASOCIADO LA ALTURA QUE ES EL INDICE 1
print(my_dict["Nombre"])

print("Moure" in my_dict) # HAY QUE BUSCAR POR CLAVE NO POR VALOR, FALSE
print("Apellido" in my_dict) # DICE TRUE, BUSCA POR APELLIDO

# INSERCION
print("INSERTAMOS CALLE")
my_dict["Calle"] = "Calle MoureDev"
print(my_dict)

# ACTUALIZAR
print("ACTUALIZAMOS EL CAMPO NOMBRE")
my_dict["Nombre"] = "Pedro"
print(my_dict["Nombre"])

# ELIMINAR
print("ELIMINAMOS EL CAMPO CALLE")
del my_dict["Calle"]
print(my_dict)

# OTRAS OPERACIONES
print("OTRAS OPERACIONES")
print(my_dict.items()) # TENEMOS UN LISTADO CON CADA UNO DE LOS ITEMS
print(my_dict.keys()) # TENEMOS LA KEYS
print(my_dict.values()) # TENEMOS TODOS LOS VALORES
print("")
my_list = ["Nombre", 1, "Piso"]

my_new_dict = dict.fromkeys((my_list)) #CREAMOS UN DICCIONARIO SIN VALORES USANDO UNA LISTA
print(my_new_dict)
my_new_dict = dict.fromkeys(("Nombre", 1, "Piso")) # LO CREAMOS DE OTRA MANERA
print((my_new_dict))
print(" ")

my_new_dict = dict.fromkeys(my_dict) # MUESTRA LOS CAMPOS SOLOS DE my_dict
print((my_new_dict))
print(" ")

my_new_dict = dict.fromkeys(my_dict, "MoureDev") # LE PONE MOUREDEV A TODAS LAS CLAVES COMO VALOR
print((my_new_dict))

print(" ")
print(" ")

my_values = my_new_dict.values()
print(type(my_values))
print("")
print(my_new_dict.values())
print(list(dict.fromkeys(list(my_new_dict.values())).keys()))
print(tuple(my_new_dict))
print(set(my_new_dict))
