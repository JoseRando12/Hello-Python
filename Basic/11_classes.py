# CLASSES #

# DEFINICION

class MyEmptyPerson: # DEFINIMOS UNA CLASE, COMIENZAN EN MAYUSCULAS CAMELCASE, LA PRIMERA LETRA DE CADA PALABRA EN MAYUSCULA
    pass  # Para poder dejar la clase vacía


print(MyEmptyPerson)
print(MyEmptyPerson())


# CLASE CON CONSTRUCTOR, FUNCIONES Y PROPIEDADES PRIVADAS Y PUBLICAS

print("")
class Person:
    def __init__(self, name, surname, alias="Sin alias"): # CON __INIT__ CREAMOS UN COSTRUCTOR DE CLASE, SELF TIENE QUE ESTAR SIEMPRE AL DEFINIR EL CONSTRUCTOR
        self.full_name = f"{name} {surname} ({alias})"  # Propiedad pública, LE DECIMOS QUE EL ALIAS APAREZCA ENTRE PARENTESIS
        self.__name = name  # Propiedad privada

    def get_name(self):
        return self.__name

    def walk(self):
        print(f"{self.full_name} está caminando")


my_person = Person("Brais", "Moure") # DEFINIMOS NAME Y SURNAME
print(my_person.full_name) #LLAMO FULL_NAME QUE CONTIENE NAME, SURNAME Y ALIAS 
print(my_person.get_name()) # LLAMO A GET_NAME, EL CUAL LLAMA A NAME CON EL SELF
my_person.walk() # LLAMA A LA CLASE WALK, CON SELF FULL_NAME Y AGREGA ESTA CAMINANDO
print("")

my_other_person = Person("Brais", "Moure", "MoureDev")
print(my_other_person.full_name)
my_other_person.walk()
my_other_person.full_name = "Héctor de León (El loco de los perros)" # LE CAMBIAMOS EL VALOR AL CONSTRUCTOR
print(my_other_person.full_name)
print("")

my_other_person.full_name = 666 # LE CAMBIAMOS EL VALOR A MY_OTHER_PERSON A NUMERO Y LA MOSTRAMOS
print(my_other_person.full_name)
