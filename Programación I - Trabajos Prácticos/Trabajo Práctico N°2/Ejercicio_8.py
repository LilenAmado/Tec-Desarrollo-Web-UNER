# Ejercicio 8:
# Pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.

# Función para ver si es un núm positivo entero: 

def es_numero(num):
    if num.isalpha():
        num = input("No es un número. Vuelva a ingresar una edad válida: ")
        return es_numero(num)
    elif num.strip() == "":
        num = input("No ingresó nada. Vuelva a ingresar una edad válida: ")
        return es_numero(num)
    elif "." in num or "," in num: 
        num = input("El número no es valido. Vuelva a ingresar una edad válida: ")
        return es_numero(num)
    elif int(num) < 0: 
        num = input("Ingresó un número negativo. Vuelva a ingresar una edad válida: ")
        return es_numero(num)
    elif int(num) == 0: 
        num = input("Ingresó el número 0. Vuelva a ingresar una edad válida: ")
        return es_numero(num)
    else: 
        return num

# Num positivo entero:

edad = input("¿Cúal es su edad? ")
edad = es_numero(edad)
edad = int(edad)

# Condición: 

if edad < 18: 
    print("Usted es menor de edad")
else:
    print("Usted es mayor de edad")