# Ejercicio 17:
# 17. Que muestre todos los números primos entre 0 y 100 e imprima cuántos números primos hay.

print("Números primos entre el 0 y 100: ")

contador = 0

for num in range(1, 101):
    es_primo = True  
    
    for i in range(2, num):
        if num % i == 0:
            es_primo = False  # No es primo
            break
    
    if es_primo:
        print(num, end=" ")  # Es num primo
        contador += 1

# Pantalla
print("\nTotal de números primos:", contador)

