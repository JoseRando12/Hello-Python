# OPERADORES ARITMETICOS#

print(5+3*2)
print(3-4)
print(3/4)
print(3*4)
print(2 ** 3 + 3 - 7 / 1 // 4)
print(" ")
print(10%2) # % OPERADOR DE MODULO, DIVIDE Y DICE EL RESTO
print(10//3) # FLOR DIVISION, SE INTENTA APROXIMAR AL ENTERO, NO DA EL DECIMAL
print(2**3) # EXPONENTE, 2 ELEVADO A LA 3
print(" ")
print("Hola " + "Python") # EL SIMBOLO + CONCATENA, LOS DEMAS DAN ERROR
# print("Hola" + 5) # ERROR NO CONCATENA UN STR CON UN INT
print("Hola " + str(5))
print("Hola-Python " * 5) # REPITE POR 5

my_float = 2.5 * 2  # 2.5 X 2 DA 5.0 UN FLOAT, POR ESO LOS PASAMOS A ENTERO
print("Hola " * int(my_float)) 

# OPERADORES COMPARATIVOS

print(3 > 4)  # DEVUELVE FALSE
print(3 < 4)  # DEVUELVE TRUE
print(3 >= 4) # DEVUELVE FALSE
print(4 <= 4) # DEVUELVE TRUE
print(3 == 4) # DEVUELVE FALSE
print(3 != 4) # DEVUELVE TRUE
print(" ")

# OPERADORES CON CADENA DE TEXTO

print("Hola" > "Python") 
print("Hola" < "Python")
print("aaaa" >= "abaa")  # Ordenación alfabética por ASCII
print(len("aaaa") >= len("abaa"))  # Cuenta caracteres
print("Hola" <= "Python")
print("Hola" == "Hola")
print("Hola" != "Python")
print(" ")

# OPERADORES LOGICOS AND-OR 

print(3 > 4 and "Hola" > "Python")
print(3 > 4 or "Hola" > "Python")
print(3 < 4 and "Hola" < "Python")
print(3 < 4 or "Hola" > "Python")
print(3 < 4 or ("Hola" > "Python" and 4 == 4))
print(not (3 > 4))
