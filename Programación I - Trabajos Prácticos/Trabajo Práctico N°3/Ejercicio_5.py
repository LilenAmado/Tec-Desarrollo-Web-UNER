# Ejercicio 5
# Escriba un programa Python que solicite al usuario el ingreso de números enteros. Cuando el usuario ingrese la palabra “fin” el programa deberá concluir con la carga de datos. Cada uno de los números ingresados por el usuario deberá ser almacenado en una lista. A continuación, realice las siguientes tareas:
# a. Determinar el máximo.
# b. Obtener segundo valor máximo. Es decir el que le sigue al máximo.
# c. Determinar el mínimo.
# d. Calcular la multiplicación de todos los números de la lista.
# e. Contar los valores pares e impares.
# f. Remover los elementos repetidos.

# Verificar si es un número entero:
def es_numero(num):
    if num != "fin" or num != "Fin" or num != "FIN":
        return num
    elif num.isalpha():
        num = input("No es un número. Ingrese un número entero positivo: ")
        return es_numero(num)
    elif num.strip() == "" :
        num = input("No ingresó nada. Ingrese un número entero positivo: ")
        return es_numero(num)
    elif "." in num or "," in num: 
        num = input("No ingresó un número entero positivo. Vuelva a ingresar: ")
        return es_numero(num)
    else: 
        return num

# Defino lista:
lista = []

# Programa para que el usuario ingrese los números a la lista:
i = ''
while i != "fin" and i != "Fin" and i != "FIN":
    usuario = input('Ingrese un número entero (Cuando escriba "Fin" termina el programa): ')
    i = es_numero(usuario)
    lista.append(i)

# Elimino el último valor de la lista que sería el "Fin":
del lista [-1]
    # print(lista)

# Convierto los numeros de la lista de string a int:
for e in range(len(lista)):
    lista[e] = int(lista[e])

    # print(lista)

# Lista final
lista.sort()
print(f'La lista final: {lista}')

##### a. Determinar el máximo.#####
valor_maximo = max(lista)
print(f'Valor máximo: {valor_maximo}')

##### b. Obtener segundo valor máximo. Es decir el que le sigue al máximo.
print(f'El segundo valor máximo: {lista[-2]}')

##### c. Determinar el mínimo. #####
valor_min = min(lista)
print(f'Valor mínimo: {valor_min}')

##### d. Calcular la multiplicación de todos los números de la lista. #####
multiplicacion = 1
for a in range(len(lista)):
    multiplicacion = multiplicacion * lista[a]

print(f'La multiplicación de todos los números da: {multiplicacion}')

##### e. Contar los valores pares e impares. #####

par = 0
impar = 0 

for n in lista:
    #lista[n] 
    if n % 2 == 0: 
        par = par + 1
        #print(n, "es par.")
    else:
        impar = impar + 1
        #print(n, "no es par.")
print(f'La lista actual: {lista}')
print(f'Hay {par} pares y {impar} impares.')


##### f. Remover los elementos repetidos. #####

lista_sin_duplicados = set(lista)
#lista_sin_duplicados.sort()
lista_sin_duplicados = sorted(list(lista_sin_duplicados))
print(f'Lista sin duplicados: {lista_sin_duplicados}')