# Ejercicio 15:
# 15. Que solicite al usuario una letra y, si es una vocal, muestre el mensaje “es vocal”. Se debe validar que el usuario ingrese sólo un carácter. Si ingresa un string de más de un carácter, informarle que no se puede procesar el dato

letra = input("Ingrese una letra: ")
letra = letra.lower()
vocales = 'aeiouáéíóúü'

if len(letra) > 1: 
    print("No se puede procesar el dato")
elif len(letra) == 0: 
    print("No se puede procesar el dato")
elif letra in vocales: 
    print("Es una vocal")
else: 
    print("No es una vocal")
