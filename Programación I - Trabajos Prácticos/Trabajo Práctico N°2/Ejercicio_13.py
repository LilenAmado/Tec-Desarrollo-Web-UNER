# Ejercicio 13
# Que resuelva el siguiente problema: los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. El grupo A está formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el resto. Escribir un programa que pregunte al usuario su nombre y sexo y muestre por pantalla el grupo que le corresponde.

nombre_usuario = input("Ingrese su nombre: ")
sexo_usuario = input("Ingrese su sexo (M/F): ")

# Transformar en mayuscula lo ingresado:
nombre = nombre_usuario.upper()
sexo = sexo_usuario.upper()

# Sexo:
sexo_persona = "" 

if sexo[0] == "F":
    sexo_persona = "Mujer" 
elif sexo[0] == "M": 
    sexo_persona = "Hombre" 
else: 
    print("No ingreso un sexo válido.")

# Nombre:

# Mujeres: 
grupo_A_mujeres = 'abcdefghijklABCDEFGHIJKL'
# Hombres: 
grupo_A_hombres = 'opqrstuvwxyzOPQRSTUVWXYZ'

if sexo_persona == "Mujer":
    if nombre[0] in grupo_A_mujeres:
        nombre_persona = True
    else:
        nombre_persona = False 
elif sexo_persona == "Hombre":
    if nombre[0] in grupo_A_hombres:
        nombre_persona = True
    else:
        nombre_persona = False 

# Ubicación de grupos: 

if sexo_persona == "Mujer" and nombre_persona == True:
    print("Sos del grupo A")
elif sexo_persona == "Hombre" and nombre_persona == True:
    print("Sos del grupo A")
else: 
    print("Sos del grupo B")
    

# M y N tanto de mujer y hombres no se encuentran incluídos por el enunciado. 