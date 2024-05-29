# Ejercicio 3
# Dada la siguiente lista de frutas [“banana”, “manzana”, “pera”], permitir al usuario ingresar 3 frutas más para agregarlas al final de lista. Luego, mostrar por pantalla la lista completa y debajo la misma lista pero sólo con las frutas que añadió el usuario.

# Lista:
frutas = ["banana", "manzana", "pera"]

# Añadir 3 frutas del usuario 
i = 1

while i < 4 :
    fruta = input(f'Ingrese la {i}° fruta: ')
    frutas.append(fruta)
    i = i + 1

print(f'La lista completa: {frutas}')

# Mostrar unicamente las frutas que añadió el usuario (eliminar las por default)
def borra_lista(frutas):
    del frutas[0]

a = 0
while a < 3 :
    borra_lista(frutas)
    a = a + 1

print(f'Las frutas que añadió el usuario: {frutas}')