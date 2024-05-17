# Ejercicio 10:
# Que el usuario ingrese un número entero positivo y muestre por pantalla lo siguiente:
# a. Todos los números impares desde 1 hasta ese número separados por comas.
# b. La cuenta atrás desde ese número hasta cero separados por comas.
# c. Que indique si es primo o no.
# d. Por último,su factorial.


# Que el usuario ingrese un número entero positivo y muestre por pantalla lo siguiente:

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

num_usuario = input("Ingrese un número entero postivo:")
num_usuario = es_numero(num_usuario)
num_usuario = int(num_usuario)

print("Usted ingreso el número: ", num_usuario)

############################# Ejercicio A: #############################
# a. Todos los números impares desde 1 hasta ese número separados por comas.

print("__________________________")
print("Ejercicio A:")

for i in range(1, num_usuario):
    if i % 2 != 0:
        #print(i, ",")
        print(i, ",", end=" ")

print()

############################# Ejercicio B: #############################
# b. La cuenta atrás desde ese número hasta cero separados por comas.

print("__________________________")
print("Ejercicio B:")

num_usuario_2 = num_usuario

while num_usuario_2 >= 0: 
    #print(num_usuario_2, ",")
    print(num_usuario_2, ",", end=" ")
    num_usuario_2 = num_usuario_2 - 1

print()

############################# Ejercicio C: #############################
# c. Que indique si es primo o no.

print("__________________________")
print("Ejercicio C:")

num_primo = ...; 

# Proceso num primo:

if num_usuario > 1:
    for i in range(2, int(num_usuario**0.5) + 1):
        if num_usuario % i == 0:
            num_primo = False 
            break
        else:
            num_primo = True
else:
    num_primo = False

if num_primo == True: 
    print(f'{num_usuario} es un número primo.')
else: 
    print(f'{num_usuario} no es un número primo.')


############################# Ejercicio D: #############################
# d. Por último,su factorial.

print("__________________________")
print("Ejercicio D:")

def factorial(num_usuario):

    if num_usuario == 0:
        return 1
    
    return num_usuario * factorial(num_usuario-1)

num_usuario_factorial = factorial(num_usuario)

print(f'El factorial de {num_usuario} es {num_usuario_factorial}')

print("__________________________")