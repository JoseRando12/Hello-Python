# CONDICIONALES #

# IF
print("")
my_condition = False

if my_condition:  # Es lo mismo que if my_condition == True:
    print("Se ejecuta la condición del if")

my_condition = 5 * 5

if my_condition == 10:
    print("Se ejecuta la condición del segundo if")

# IF, ELIF, ELSE

if my_condition > 10 and my_condition < 20:
    print("Es mayor que 10 y menor que 20")
elif my_condition == 25: # NECESITA SI O SI UNA CONDICION
    print("Es igual a 25")
else: # NO NECESITA UNA CONDICION
    print("Es menor o igual que 10 o mayor o igual que 20 o distinto de 25")

print("La ejecución continúa") # LA TABULACION ESTA FUERA DEL ELSE NO LA TOMA
print("")

# CONDICIONAL CON ISPECCION DE VALOR

my_string = "" # SI ACA PONGO EL MISMOS STRING ME DARIA QUE SON IDENTICAS

if not my_string: # NIEGO LA CONDICION O SEA SI ES NO VACIO, ES TRUE AVANZA
    print("Mi cadena de texto es vacía")

if my_string == "Mi cadena de textoooooo":
    print("Estas cadenas de texto coinciden")

