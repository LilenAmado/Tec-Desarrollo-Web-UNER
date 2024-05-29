# Ejercicio 6
# Programe una aplicación de consola Python que brinde al usuario la posibilidad de a partir de una lista vacía:
# a. Agregar un elemento al final.
# b. Agregar un elemento al principio.
# c. Quitar un elemento al final.
# d. Quitar un elemento al principio

lista = []

############# a. Agregar un elemento al final. #############

elemento = input("Agregue un elemento al final de la lista: ")

lista.append(elemento)

print(f'Lista: {lista}')

############# b. Agregar un elemento al principio. #############

elemento = input("Agregue un elemento al principio de la lista: ")

lista.insert(0, elemento)

print(f'Lista: {lista}')

############# c. Quitar un elemento al final. #############

del lista[-1]

print(f'Se elimina el elemento final de la lista: {lista}')

############# d. Quitar un elemento al principio #############

del lista[0]

print(f'Se elimina el primer elemento de la lista: {lista}')