# Regular Expressions #

import re

# MATCH

my_string = "Esta es la lección número 7: Lección llamada Expresiones Regulares"
my_other_string = "Esta no es la lección número 6: Manejo de ficheros"

match = re.match("Esta es la lección", my_string, re.I)
print(match)
print(match.span()) # NOS DICE QUE ESTA ENTRE LA CADENA 0-18
start, end = match.span()
print(my_string[start:end])


print("")
match = re.match("Esta no es la lección", my_other_string)
#if not(match == None): # Otra forma de comprobar el None
#if match != None: # Otra forma de comprobar el None
if match is not None:
    print(match)
    start, end = match.span()
    print(my_other_string[start:end])

print(re.match("Expresiones Regulares", my_string))
print("")

# SEARCH

search = re.search("lección", my_string, re.I)
print(search)
start, end = search.span()
print(my_string[start:end])

# FINDALL
print("")
findall = re.findall("lección", my_string, re.I) # BUSCA TODAS LAS EXPRESIONES CON LA PALABRA LECCION, INDISTINTAMENTE MAY DE MIN
print(findall)                                   # RE.I le da lo mismo mayuscula de minuscula


# SPLIT
print("")
print(re.split(":", my_string)) # el split busca un patron (:) y los divide a partir de ahi en una lista

# DUB
print("")
print(re.sub("[l|L]ección", "LECCIÓN", my_string)) # SUSTITUYE LAS PALABRAS
print(re.sub("Expresiones Regulares", "RegEx", my_string)) # SUSTITUYE EL STRING COMPLETO POR OTRO

#-----------------------------------------------------------------------------------------#

# Regular Expressions Patterns #

# Para aprender y validar expresiones regulares: https://regex101.com
print("---------------------------------EXPRESIONES REGULARES--------------------------------------------------")

pattern = r"[lL]ección"
print(re.findall(pattern, my_string)) # BUSCA LA EXPRESION L l EN EL TEXTO my_string Y LOS MUESTRA

pattern = r"[lL]ección|Expresiones"   # LA r ES UNA PALABRA RESERVADA DE PYTHON
print(re.findall(pattern, my_string)) # COMBINA CON | ( O ) Y LOS MUESTRA EN FORMATO ARRAIZ

pattern = r"[0-9]"
print(re.findall(pattern, my_string)) # BUSCA LOS NUMEROS DE 0-9, DEVUELVE EL 7
print(re.search(pattern, my_string)) # ENCONTRO EL 7 ENTRE EL CARACTER 26-27

pattern = r"\d"
print(re.findall(pattern, my_string)) 

pattern = r"\D"
print(re.findall(pattern, my_string))

pattern = r"[l].*"
print(re.findall(pattern, my_string)) # MUESTRA TODO LO QUE VIENE DESPUES DE LA l

print("")
email = "mouredev@mouredev.com"
pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z-.]+$" # r(EXPRESION REGULAR)"^ QUE EMPIEZA POR CUALQUIER COSA QUE SE AZ MAY Y MIN Y TODO LO DEMAS
print(re.match(pattern, email)) # CON MATCH LOS BUSCA Y ENCUENTRA EL MAIL
print(re.search(pattern, email)) # CON SEARCH LO BUSCA Y TMB LO ENCUENTRA
print(re.findall(pattern, email)) # NOS DEVUELVE EL MAIL SOLAMENTE

email = "mouredev@mouredev.com.mx"
print(re.findall(pattern, email))
