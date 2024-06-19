# Lilén Amado - Programación I - Parcial

# GRUPO 1 - EJERCICIO 1
# Escribe un programa que lea las calificaciones de un grupo de estudiantes (el usuario ingresará las calificaciones una a una y usará el valor “FIN” para finalizar la entrada de datos). 
# El programa debe cumplir con los siguientes requisitos:
# Requisitos:
# ● Utilizar una lista para almacenar las calificaciones.
# ● Imprimir las calificaciones ordenadas de menor a mayor.
# ● Calcular y mostrar el promedio por pantalla.
# ● Contar el número de calificaciones ingresadas.
# ● Convertir todas las calificaciones a strings y unirlas en una sola cadena(string) separada
# por comas.
# ● Contar cuántos alumnos han aprobado la materia (sacaron una nota mayor o igual a 6).
# ● Calcular la calificación más baja y la más alta e Imprimir por pantalla un mensaje con el siguiente formato: “La calificación más baja fue XX y la más alta XX.”
# ● Vaciar la lista.

################################################ Funciones: ################################################

# Función para realizar separadores en la consola (para un mejor entendimiento en el resultado): 
def separador(elemento): 
    print(elemento * 80)  


# Función para verificar si es un número:
def es_numero(num):
    if num.isalpha():
        num = input("No es un número. Ingrese nuevamente la calificación: ")
        return es_numero(num)
    elif num.strip() == "":
        num = input("No ingresó nada. Ingrese nuevamente la calificación: ")
        return es_numero(num)
    elif "." in num or "," in num: 
        num = num.replace(',', '.')
        num = float(num)
        return num
    elif int(num) < 0: 
        num = input("Ingresó un número negativo. Vuelva a ingresar: ")
        return es_numero(num)
    else: 
        return num

################################################## Lista: #################################################
calificaciones = [] # ● Utilizar una lista para almacenar las calificaciones.

# Variables utilizadas:
contador = 1
cantidad_calificaciones = 0
suma_calificaciones = 0 
aprobados = 0 
calificaciones_str = "" 

################################################ Programa: ################################################
separador("*")
print("Sistema de calificaciones - Ingrese las calificaciones")
separador("*")

while True:
    
    calificacion = input(f'Ingrese la {contador}° calificación (Escriba "Fin" para terminar el programa):  ')

    separador("-")

    if calificacion.lower() == "fin":
        break 

    calificacion = es_numero(calificacion)
    calificacion = float(calificacion) # Convierto en num flotante
    calificaciones.append(calificacion) # Lo añado a la lista de calificacines
    
    suma_calificaciones += calificacion # Suma de valores
    contador += 1
    cantidad_calificaciones += 1

    # Almaceno la cant de aprobados en la variable:
    if calificacion >= 6: 
        aprobados += 1

separador("_")

# print(calificaciones)
# print(contador)
# print(suma_calificaciones)
# print(cantidad_calificaciones)

################################################ Requisitos: ################################################

############################################################
# ● Imprimir las calificaciones ordenadas de menor a mayor.
############################################################

calificaciones.sort()
print(f'Las calificaciones ordenasdas de menor a mayor: {calificaciones}')
separador("_")

#################################################
# ● Calcular y mostrar el promedio por pantalla.
#################################################

promedio = suma_calificaciones / cantidad_calificaciones 
print(f'El promedio es: {promedio}')
separador("_")

###################################################
# ● Contar el número de calificaciones ingresadas.
###################################################

print(f'La cantidad de calificaciones ingresadas son: {cantidad_calificaciones}')
separador("_")

##########################################################################################################
# ● Convertir todas las calificaciones a strings y unirlas en una sola cadena(string) separada por comas.
##########################################################################################################

for indice in range(len(calificaciones)):
    if indice == 0:
        calificaciones_str += str(calificaciones[indice])
        #print(calificaciones_str)
    else:
        calificaciones_str += "," + str(calificaciones[indice])
        #print(calificaciones_str)

print(calificaciones_str)
separador("_")

#########################################################################################
# ● Contar cuántos alumnos han aprobado la materia (sacaron una nota mayor o igual a 6).
#########################################################################################

print(f'Cantidad de alumnos aprobados: {aprobados}')
separador("_")

####################################################################################################################
# ● Calcular la calificación más baja y la más alta e Imprimir por pantalla un mensaje con el siguiente formato: “La calificación más baja fue XX y la más alta XX.”
####################################################################################################################
max = max(calificaciones)
min = min(calificaciones)

print(f'La calificación más baja fue {min} y la más alta {max}.')
separador("_")

########################
# ● Vaciar la lista.
########################
calificaciones.clear()

    #calificaciones = []
    #print(calificaciones)

print("Lilén Amado - Programación I - Parcial")