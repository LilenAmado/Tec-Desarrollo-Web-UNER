# Ejercicio 4
# Dada la siguiente lista: países = [“Argentina,”Brasil”, “Bolivia”,”Paraguay”,”Venezuela”], realizar lo siguiente:
# a. Imprimir la cantidad de elementos que tiene la lista.
# b. Imprimir el primer y último elemento.
# c. Imprimir el resto.
# d. Permitir que el usuario ingrese un país e imprimir el índice si el país se encuentra en la lista. Si no se encuentra, imprimir un mensaje advirtiendo al usuario.
# e. Permitir al usuario ingresar un número igual o menor a la cantidad de elementos de la lista. Quitar el elemento correspondiente de esa posición.
# f. Imprimir la lista en orden inverso.
# g. Vaciar la lista.

# Lista:
paises = ["Argentina", "Brasil", "Bolivia", "Paraguay", "Venezuela"]

# a. Imprimir la cantidad de elementos que tiene la lista.
print(f'La cantidad de países en la lista es: {len(paises)}')

# b. Imprimir el primer y último elemento.
print(f'Primer elemento: {paises[0]}. Ultimo elemento: {paises[-1]}')

# c. Imprimir el resto.
print(f'El resto de los elementos son: ')
for i in paises[1:4]:
    print(i)

# d. Permitir que el usuario ingrese un país e imprimir el índice si el país se encuentra en la lista. Si no se encuentra, imprimir un mensaje advirtiendo al usuario.

pais_usuario = input("Ingrese un pais: ")
pais_usuario = pais_usuario.capitalize()

if pais_usuario in paises:
    print(f'El índice de {pais_usuario} es {paises.index(pais_usuario)}')
else: 
    print("Ese país no se encuentra en la lista.")

# e. Permitir al usuario ingresar un número igual o menor a la cantidad de elementos de la lista. Quitar el elemento correspondiente de esa posición.

num_usuario = int(input("Ingrese una posición para quitar el elemento: "))

if num_usuario < len(paises): 
    print(f'Se eliminó la posición: {num_usuario}. País: {paises[num_usuario]}')
    del paises[num_usuario]
    print(f'La lista actual: {paises}')
else: 
    print(f'La posición {num_usuario} no existe en la lista.')

# f. Imprimir la lista en orden inverso.
paises.reverse()
print(f'Lista invertida: {paises}')

# g. Vaciar la lista.
paises.clear()
print(f'Lista vacía: {paises}')