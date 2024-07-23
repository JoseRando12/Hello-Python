# variables

mi_variable_string="esto es un variable string"
print(mi_variable_string)

mi_variable_entero=5
print(mi_variable_entero)

mi_variable_bool=False
print(mi_variable_bool)

print(mi_variable_string, mi_variable_entero,mi_variable_bool) 

my_int_to_str_variable = str(mi_variable_entero) # str: transforma la variable entera a string
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

# CONCATENACION DE VARIABLES EN UN PRINT
print ("Concatenamos las variables: ",mi_variable_string, mi_variable_entero, mi_variable_bool)

# ALGUNAS FUNCIONES DE SISTEMA
print (len(mi_variable_string))  # CUENTA LOS CARACTERES DE LAS VARIABLES

# VARIABLES EN UNA SOLA LINEA
name, surname, alias, age = "Jose", "Rando","Josecito",46;
print("Me llamo:",name, surname,",mi edad es",age,"años", "y mi Alias es",alias)

# SISTEMA DE INPUT DE DATOS
primer_nombre = input ('Cual es tu nombre:? ')
age = input ('y tu edad:? ')

print ("Tu nombre es: ", primer_nombre)
print ("y tu edad es: ", age,"años")

# CAMBIAMOS EL TIPO DE DATOS A LAS VARIABLES
primer_nombre = 12
age = "Milo"
print ("Tu nombre es: ", primer_nombre)
print ("y tu edad es: ", age,"años")
# PYTHON LO INTERPRETA IGUAL, SIGNIFICA QUE NO ES UN LENGUAJE FUERTEMENTE TIPADO

# FORZAMOS EL TIPO DE DATO
direccion: str = "Vergara 2764"
direccion = 32
print(type(direccion))
# PYTHON NO FUNCIONA EL FORZAR EL TIPADO, PORQUE SE QUEDARIA CON EL ULTIMO ASIGNADO
