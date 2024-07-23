# File Handling = MANEJO DE FICHEROS#

import xml
import csv
import json
import os

# .txt file
# Leer, escribir y sobrescribir si ya existe
txt_file = open("__pycache__/Intermediate/mi_fichero.txt", "w+") # COMBINAMOS LETRAS W+ PARA LEER Y RESTO, INTENTA ABRIR EL ARCHIVO SI NO EXISTE LO CREA Y LE INGRESA LOS SIGUENTES DATOS

txt_file.write("Mi nombre es Jose\nMi Apellido es Rando\nMi edad 46 Años\nMi lenguaje es Python")

#print(txt_file.read()) # MUESTRA EN PANTALLA EL CONTENIDO DEL FICHERO
#print(txt_file.read(10)) # LEE SOLAMENTE LOS 10 PRIMEROS CARACTERES
#print(txt_file.readline())
#print(txt_file.readline()) # LEE LA PRIMER LINEA SOLAMENTE
#print(txt_file.readlines()) # LO LEE COMO ARRAIZ
for line in txt_file.readlines():
    print(line)

txt_file.write("\nAunque tambien me gusta JavaScript")
print(txt_file.readline())

txt_file.close()

#os.remove("__pycache__/Intermediate/mi_fichero.txt") # CON ESTA LINEA ELIMINA EL ARCHIVO .TXT

#-----------------------------------------------------------------------------------------#
# .json file


json_file = open("__pycache__/Intermediate/my_file.json", "w+") # CREAMOS UN FICHERO JSON

json_test = {              # CREAMOS UN ARCHIVO JSON = DICT
    "name": "Brais",
    "surname": "Moure",
    "age": 35,
    "languages": ["Python", "Swift", "Kotlin"],
    "website": "https://moure.dev"}

#json_file.write(json_test) # TYPEERROR: WRITE() ARGUMENT MUST BE STR, NOT DICT

json.dump(json_test, json_file,indent=2) # AHORA TENEMOS MAPEADO UN JSON Y LO IDENTAMOS CON 2 ESPACIOS DELANTE

json_file.close()

with open("__pycache__/Intermediate/my_file.json") as my_other_file: # NOS PERMITE ABRIR EL ARCHIVO Y LEERLO
    for line in my_other_file.readlines():
        print(line)

json_dict = json.load(open("__pycache__/Intermediate/my_file.json")) # ABRO EL ARCHIVO JSON Y LO ASIGNO A UNA VARIABLE COMO DICCIONARIO
print(json_dict) # CON ESTE COMANDO NOS MUSTRA TODO EL DICCIONARIO
print(type(json_dict)) # CON ESTE COMANDO NOS DICE EL TYPO, CLASS DICT
print(json_dict["name"]) # NOS MUESTRA EL NAME SOLAMENTE DEL DICT
print(len(json_dict))

# .csv file   ARCHIVOS DE EXCEL


csv_file = open("__pycache__/Intermediate/my_file.csv", "w+")

csv_writer = csv.writer(csv_file)
csv_writer.writerow(["name", "surname", "age", "language", "website"])
csv_writer.writerow(["Brais", "Moure", 35, "Python", "https://moure.dev"])
csv_writer.writerow(["Roswell", "", 2, "COBOL", ""])

csv_file.close()

with open("__pycache__/Intermediate/my_file.csv") as my_other_file:
    for line in my_other_file.readlines():
        print(line)


# .xlsx file


# import xlrd # Debe instalarse el módulo

# .xml file