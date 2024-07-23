# MODULOS # ES UNA LIBRERIA EL LUGAR DONDE TENGO FUNCIONES Y LAS IMPORTO

from math import pi as PI_VALUE # VAMOS DIRECTAMENTE A LA FUNCION MATH A LA FUNCION PI

import math # IMPORTAMOS LA PALABRA RESERVADA MATH INCLUYE OPERACIONES MATEMATICAS

from my_module import sumValue, printValue #ACCEDEMOS A OTRO FICHERO, no se aceptan ficheros que comiencen con numeros
                                           
import my_module # IMPORTAMOS EL ARCHIVO

my_module.sumValue(5, 3, 1) # ACCESO A LAS DOS FUNCIONES DEL FICHERO
my_module.printValue("Hola Python!")

print("")
sumValue(5, 3, 1) # LE PASO VALORES A LA FUNCION IMPORTADA Y RESPONDE
printValue("Hola python") # LE PASO VALORES A LA FUNCION IMPORTADA Y RESPONDE

print("")
print(math.pi)
print(math.pow(2, 8))

print("")
print(PI_VALUE)

