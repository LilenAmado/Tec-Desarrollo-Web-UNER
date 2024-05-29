# Ejercicio 2
# Pedir al usuario que ingrese 5 números para luego almacenarlos en una lista y ordenarlos. Imprimir por pantalla el resultado.

numeros = []

# Verificar si lo ingresado es un número:

def es_numero(num):
    if num.isalpha():
        num = input("No es un número. Ingrese un número: ")
        return es_numero(num)
    elif num.strip() == "":
        num = input("No ingresó nada. Ingrese un número: ")
        return es_numero(num)
    else: 
        return num

i = 1

while i < 6 :
    num = input(f'Ingrese el {i}° número: ')
    num = es_numero(num)
    num = float(num)
    numeros.append(num)
    i = i + 1

def ordenar_lista():
    numeros.sort()
    print(numeros)

ordenar_lista()