# Ejercicio 6:
# Programe una aplicación de consola que pregunte el precio total de la cuenta, luego 
# pregunte cuántos comensales hay. A continuación deberá dividir la cuenta total por el 
# número de comensales y mostrar cuánto debe pagar cada persona.

# Total:
print("¿Cuál es el precio total de la cuenta? Ejemplo: 9.56")
total = float(input())

# Cant. Personas:
print("¿Cuántas personas consumieron?")
personas = int(input())

resultado = total / personas

print("Cada persona deberá pagar:", resultado)