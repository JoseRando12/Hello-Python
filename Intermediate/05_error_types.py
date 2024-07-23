### Error Types ###

from math import pi
import math

# SyntaxError
print("")
print("SyntaxError")
#print "¡Hola comunidad!" # Descomentar para Error
print("¡Hola comunidad!")

# NameError
print("")
print("NameError")
language = "Spanish"  # Comentar para Error
print(language)

# IndexError
print("")
print("IndexError")
my_list = ["Python", "Swift", "Kotlin", "Dart", "JavaScript"]
print(my_list[0])
print(my_list[4])
print(my_list[-1]) # muestra el primer elemento empezando del final
#print(my_list[5]) # Descomentar para Error
#ModuleNotFoundError
#import maths # Descomentar para Error
#AttributeError
#print(math.PI) # Descomentar para Error
print(math.pi)

# KeyError
print("")
print("KeyError")
my_dict = {"Nombre": "Brais", "Apellido": "Moure", "Edad": 35, 1: "Python"}
print(my_dict["Edad"])
#print(my_dict["Apelido"]) # Descomentar para Error
print(my_dict["Apellido"])

# TypeError
print("")
print("TypeError")
# print(my_list["0"]) # Descomentar para Error
print(my_list[0])
print(my_list[False])

# ImportError
print("")
print("ImportError")
# from math import PI # Descomentar para Error
print(pi)

# ValueError
print("")
print("ValueError")
#my_int = int("10 Años")
my_int = int("10")  # Descomentar para Error
print(type(my_int))

# ZeroDivisionError
print("")
print("ZeroDivisionError")
#print(4/0) # Descomentar para Error
print(4/2)
