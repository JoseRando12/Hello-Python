# DATES #

# DATE TIME

from datetime import timedelta
from datetime import date
from datetime import time # IMPORTAMOS TIME PARA ACTUAR CON TIME

from datetime import datetime # IMPORTAMOS LA PARTE DE DATETIME DEL MODULO DATETIME

now = datetime.now() # DEFINIMOS LA VARIABLE NOW, EL DIA DE HOY CON LA FUNCION NOW()


def print_date(date):
    print(date.year)
    print(date.month)
    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.second)
    print(date.timestamp()) # ES EL MOMENTO EN EL QUE SE CORRESPONDE DESDE 1970


print_date(now)

print("")
year_2025 = datetime(2025, 1, 1) # ACA LE INDICAMOS UNA FECHA PRECISA SI NO PONEMOS NADA EN LA HORA POR DEFECTO ES 0
print_date(year_2025) # MUESTRA 2023, 1 , 1, 0, 0, 0

#------------------------------------------------------------------------------------#

# TIME
print("TIME")

now_time = now.time() # INDICAMOS LA HORA ACTUAL

print(now_time.hour) # MOSTRAMOS LA HORA
print(now_time.minute) # MOSTRAMOS LOS MINUTOS
print(now_time.second) # MOSTRAMOS LOS SEGUNDOS

current_time = time(21, 6, 0) # DEFINIMOS UNA HORA PRECISA

print(current_time.hour)
print(current_time.minute)
print(current_time.second)
print("")
#--------------------------------------------------------------------------------------#
# DATE
print("DATE")

current_date = date.today()

print(current_date.year) # MUESTRA EL AÑO
print(current_date.month) # MUESTRA EL MES
print(current_date.day) #MUESTRA EL DIA

current_date = date(2024, 7, 12) # ACA LE PASO LOS PARAMETRO A MOSTRAR

print(current_date.year)
print(current_date.month)
print(current_date.day)

current_date = date(current_date.year, current_date.month + 1, current_date.day)

print(current_date.month) # ACA MUESTRO QUE SE PUEDE MODIFICAR UN FECHA, LE SUME 1
print("")
#-------------------------------------------------------------------------------------#
# OPERACIONES CON FECHAS #

print("Operaciones con fechas")

diff = year_2025 - now
print(diff)

diff = year_2025.date() - current_date
print(diff)
print("")

#-------------------------------------------------------------------------------------#
# TIMEDELTA
print("TIMEDELTA")

start_timedelta = timedelta(200, 100, 100, weeks=10) # LE DEFINO VALORES AL TIMEDELTA, Y TMB SEMANA
end_timedelta = timedelta(300, 100, 100, weeks=13)

print(end_timedelta - start_timedelta) # RESTA FRANJAS DE FECHAS DEFINIDAS
print(end_timedelta + start_timedelta) # SUMA FRANJAS DE FECHAS DEFINIDAS

