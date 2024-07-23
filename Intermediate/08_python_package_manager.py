# Python Package Manager #

# PIP https://pypi.org

# pip install pip
# pip --version

# pip install numpy

import pandas

import requests

import numpy

print(numpy.version.version)

numpy_array = numpy.array([35, 24, 62, 52, 30, 30, 17]) # numpy hacemos un arraiz
print(type(numpy_array)) # mostramos el tipo

print(numpy_array * 2) 

# pip install pandas

# pip list
# pip uninstall pandas
# pip show numpy

# pip install requests

response = requests.get("https://pokeapi.co/api/v2/pokemon?limit=151")
print(response)
print(response.status_code)
print(response.json())

# Arithmetics Package
# pip install mypackage ( para installar el packete creado por nosotros)
from mypackage import arithmetics
print(arithmetics.sum_two_values(1, 4)) # LLAMO A LA FUNCION CREADA EN EL PAQUETE
print(arithmetics.sum_two_values(5, 5))
