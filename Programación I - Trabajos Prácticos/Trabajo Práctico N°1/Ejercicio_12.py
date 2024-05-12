# Ejercicio 12:
# Pedir al usuario que ingrese una fecha en formato dd/mm/aaaa e imprimir en pantalla
# el día, mes y año. Ej: 
# Usuario ingresa: 17/05/1985
# Programa imprime: Día: 17, Mes: 05 y Año: 1985

# Fecha:
fecha = input("Ingrese una fecha con formato dd/mm/aaaa: ")

# Dividir la fecha en día, mes y año
dia, mes, año = fecha.split('/')

# Imprimir en pantalla el día, mes y año
print("Día:", dia)
print("Mes:", mes)
print("Año:", año)
