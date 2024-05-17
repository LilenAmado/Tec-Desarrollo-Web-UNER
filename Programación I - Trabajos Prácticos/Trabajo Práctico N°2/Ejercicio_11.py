# Ejercicio 11 
# 11. Que solicite al usuario ingresar una frase. Luego, que imprima la cantidad de vocales que se encuentran en dicha frase

frase = input("Ingrese una frase: ")

# ['a', 'e', 'i', 'o', 'u'] 

vocales = 'aeiouAEIOUáéíóúüÁÉÍÓÚÜ'
x = ''

for i in frase:
    if i in vocales:
        x += i

print (f'Cantidad: {len(x)}.')
print (f'Las vocales encontradas: {x}.')