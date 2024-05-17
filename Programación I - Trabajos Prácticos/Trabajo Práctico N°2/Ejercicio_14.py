# Ejercicio 14: 
# 14. Que pida un año y que escriba si es bisiesto o no. Les recordamos que los años bisiestos son múltiplos de 4, pero los múltiplos de 100 no lo son, aunque los múltiplos de 400 sí. Algunos ejemplos de posiblesrespuestas: 2012 es bisiesto, 2010 no es bisiesto, 2000 es bisiesto, 1900 no es bisiesto

# Función de num entero positivo:
def es_numero(num):
    if num.isalpha():
        num = input("No es un número. Ingrese un número entero positivo: ")
        return es_numero(num)
    elif num.strip() == "":
        num = input("No ingresó nada. Ingrese un número entero positivo: ")
        return es_numero(num)
    elif "." in num or "," in num: 
        num = input("No ingresó un número entero positivo. Vuelva a ingresar: ")
        return es_numero(num)
    elif int(num) < 0: 
        num = input("Ingresó un número negativo. Vuelva a ingresar: ")
        return es_numero(num)
    elif int(num) == 0: 
        num = input("Ingresó el número 0. Vuelva a ingresar: ")
        return es_numero(num)
    else: 
        return num

num_usuario = input("Ingrese un año para saber si es bisiesto o no: ")
num_usuario = es_numero(num_usuario)
num_usuario = int(num_usuario)

# Bisiesto o no:

if num_usuario % 4 == 0:  
    if num_usuario % 100 == 0:  
        if num_usuario % 400 == 0:  
            print(f'El año {num_usuario} es bisiesto')  
        else:
            print(f'El año {num_usuario} no es bisiesto')  
    else:
        print(f'El año {num_usuario} es bisiesto')  
else:
    print(f'El año {num_usuario} no es bisiesto')  

