# LOOPS - BLUCLES - CICLOS #

# WHILE

my_condition = 0

while my_condition < 10:  # ACA IMPRIME 0, ENTRA EL BUCLE, SALE VALIENDO 2, 4, 6, 8 Y SALE DE L BUCLE
    print(my_condition)
    my_condition += 2
else:  # Es opcional
    print("Mi condición es mayor o igual que 10") # AL SALIR DEL BUCLE IMPRIME ESTO

print("La ejecución continúa") # SALE DEL BUCLE VALIENDO 10

while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        print("Se detiene la ejecución")
        break # INDICAMOS QUE PARE EL BUCLE, SALE DE LA CONDICION E IMPRIME LA MISMA
    print(my_condition)

print("La ejecución continúa")
print("")

# FOR
print("BUCLE FOR") # NOS SIRVE PARA INTERAR UN LISTADO DE ELEMENTOS
my_list = [35, 24, 62, 52, 30, 30, 17] # EL FOR SE VA A EJECUTAR TANTAS VECES COMO ELEMENTOS TENGA

for element in my_list:
    print(element)
print("")
print("TUPLA")
my_tuple = (35, 1.77, "Brais", "Moure", "Brais")

for element in my_tuple:
    print(element)
print("")
print("SET")
my_set = {"Brais", "Moure", 35}

for element in my_set:
    print(element)
print("")
print("DICCIONARIO")
my_dict = {"Nombre": "Brais", "Apellido": "Moure", "Edad": 35, 1: "Python"}

for element in my_dict:
    print(element)
    if element == "Edad":
        break # SALE DEL FOR
else:
    print("El bluce for para diccionario ha finalizado")

print("La ejecución continúa")

for element in my_dict:
    print(element)
    if element == "Edad":
        continue # CONTINUA CON EL FOR
    print("Se ejecuta")
else:
    print("El bluce for para diccionario ha finalizado")
    