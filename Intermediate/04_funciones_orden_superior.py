# Higher Order Functions #

from functools import reduce


def sum_one(value):  # CREO UNA FUNCION QUE SUMA 1 AL VALOR QUE LE ENTRA
    return value + 1


def sum_five(value): # CREO OTRA FUNCION QUE SUME 5 AL VALOR QUE LE INDICO
    return value + 5


def sum_two_values_and_add_value(first_value, second_value, f_sum): # LE PASAMOS F_SUM COMO FUNCION DENTRO DE LA FUNCION PRINCIPAL
    return f_sum(first_value + second_value)


print(sum_two_values_and_add_value(5, 2, sum_one)) # LLAMO A LA FUNCION Y DENTRO LLAMA A LA OTRA FUNCION
print(sum_two_values_and_add_value(5, 2, sum_five)) # LLAMO A LA FUNCION DE ORDEN SUPERIOR, FUNCIONES Q SON CAPACES DE EJECUTAR OTRAS FUNCIONES


# Closures #
print("")

def sum_ten(original_value):
    def add(value):
        return value + 10 + original_value
    return add # closures, es una funcion que retorna una funcion 

add_closure = sum_ten(1)
print(add_closure(5))
print((sum_ten(5))(1))


# Built-in Higher Order Functions #
print("MAP")

numbers = [2, 5, 10, 21, 3, 30] # CREAMOS UNA LISTA DE NUMEROS

# Map

def multiply_two(number): # DEFINIMOS UNA FUNCION QUE MULTIPLIQUE X 2
    return number * 2

print(map(multiply_two, numbers)) # MUESTRA QUE ES UN OBJETO
print(list(map(multiply_two, numbers))) # MOSTRAMOS LA LISTA LLAMAMOS AL MAP DE LA FUNCION
print(list(map(lambda number: number * 2, numbers))) # HACEMOS LOS MISMO PER CON UNA LAMBDA

# Filter

print("FILTER")

def filter_greater_than_ten(number):
    if number > 10:
        return True
    return False

print(filter(filter_greater_than_ten, numbers)) # FILTER ES UN OBJETO
print(list(filter(filter_greater_than_ten, numbers))) # LLAMAMOS A LA FUNCION QUE FILTRA LOS NUMEROS
print(list(filter(lambda number: number > 10, numbers))) # LO MISMOS CON LAMBDA

# Reduce
print("REDUCE")

def sum_two_values(first_value, second_value): 
    print(first_value)
    print(second_value)
    return first_value + second_value # REDUCE OPERA CON LOS VALORES QUE TIENE LA LISTA

print(reduce(sum_two_values, numbers)) # LLAMAMOS LA FUNCION REDUCE LA CUAL LLAMA A LA FUNCION SUM_TWO_VALUES Y SUMA NUMBERS
