# STRINGS

my_string = "Mi String"
my_other_string = 'Mi otro String'

print("Tengo",len(my_string),"Caracteres") # Cuenta los caracteres
print("Mi Otros Strings tiene",len(my_other_string),"Caracteres" )
print(my_string + " " + my_other_string)

print(" ")

my_new_line_string = "Este es un String\ncon salto de línea"
print(my_new_line_string)

print(" ")

my_tab_string = "\tEste es un String con tabulación" # \t tabula al principio
print(my_tab_string)

print(" ")

my_scape_string = "\tEste es un String \n escapado" # SI LE AGREGO UNA \ DELANTE DE LA QUE TIENE LO PASA EN UNA LINEA
print(my_scape_string)

print(" ")

# FORMATEO


name, surname, age = "Jose", "Rando", 46

print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age)) # OTRA MANERA ES CON .format Y USANDO LLAVES
print("Mi nombre es %s %s y mi edad es %d" % (name, surname, age)) # EL %s COLOCA EL NAME EN ESE LUGAR SEGUN EL ORDEN QUE LO PONGAMOS
print("Mi nombre es " + name + " " + surname + " y mi edad es " + str(age)) # LOS COLOCA TODOS COMO STRING
print(f"Mi nombre es {name} {surname} y mi edad es {age}") # INFERENCIA DE DATOS CON LA f DELANTE LO FORMATEA
print(" ")

# DESEMPAQUETADO DE CARACTERES

language = "python"      # DESEMPAQUETA LOS CARACTERES DE LA VARIABLE Y LO DIVIDE EN LETRAS A-B-C-D-E-F Y MUESTRA LAS LETRAS QUE INDICAMOS
a, b, c, d, e, f = language
print(a)
print(e)
print(" ")

# DIVISION

language_slice = language[1:3] # MUESTRA LA Y T, DESDE 0 
print(language_slice)

language_slice = language[1:] # DE LA y EN ADELANTE
print(language_slice)

language_slice = language[-2] # LA SEGUNDA EMPEZANDO POR EL FINAL, AHI ARRANCA DE 1
print(language_slice)

language_slice = language[0:6:2] # 
print(language_slice)
print(" ")

# REVERSE

reversed_language = language[::-1] # LO IMPRIME DE REVES
print(reversed_language)
print(" ")

# FUNCIONES DEL LENGUAJE

print(language.capitalize()) # MUESTRS Python
print(language.upper()) # MUESTRA PYTHON
print(language.count("t")) # CUENTA CUANTAS T TIENE LA VARIABLE, MUESTRA 1
print(language.isnumeric()) # DICE SI ES UN NUMERO, FALSE
print("1".isnumeric()) # ACA DICE TRUE
print(language.lower()) # PASA A MINUSCULA
print(language.lower().isupper()) # PREGUNTA SI ES MAYUSCULA, FALSE
print(language.startswith("Py")) # NO EMPIEZA CON MAYUSCULA, FALSE
print("Py" == "py")  # No es lo mismo

print(" ")