# Ejercicio 10:
# Escriba un programa que indique si un texto es palíndromo, es decir, 
# se escribe igual al derecho que al revés. Por ejemplo: rayar, kayak, somos

# Validar si es un palíndromo:
def es_palindromo(texto):
    # Texto a minúsculas para poder comparar
    texto = texto.lower().replace(" ", "")
    # Comparar con texto al reverso
    return texto == texto[::-1]

# Texto:
texto = input("Ingrese un texto para verificar si es un palíndromo: ")

# Verificación:
if es_palindromo(texto):
    print("El texto es un palíndromo.")
else:
    print("El texto no es un palíndromo.")