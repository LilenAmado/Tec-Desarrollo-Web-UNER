# Ejercicio 7:
# Pida al usuario un número x de días y luego mostrar por pantalla cuántas horas, minutos y 
# segundos son esos números de días.

print("Ingrese la cantidad de días")

dias = int(input())

horas = dias * 24

minutos = horas * 60

segundos = minutos * 60

print("Días:", dias)
print("Horas:", horas)
print("Minutos:", minutos)
print("Segundos:", segundos)