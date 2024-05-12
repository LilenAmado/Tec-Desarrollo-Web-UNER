# Ejercicio 4:
# Que dada la base y altura de un triángulo nos calcule su área


# Función para ver si es un núm positivo entero: 

def es_numero(num):
    if num.isalpha():
        num = input("No es un número. Ingrese un número entero positivo: ")
        return es_numero(num)
    elif num.strip() == "":
        num = input("No ingresó nada. Ingrese un número entero positivo: ")
        return es_numero(num)
    elif int(num) < 0: 
        num = input("Ingresó un número negativo. Vuelva a ingresar: ")
        return es_numero(num)
    elif int(num) == 0: 
        num = input("Ingresó el número 0. Vuelva a ingresar: ")
        return es_numero(num)
    else: 
        return num
    
# Base: 
# Pido la base: 
base = input("Ingrese base: ")
# Llama función:
base = es_numero(base)
# Convertir a float:
base = float(base)

# Altura: 
# Pido la altura: 
altura = input("Ingrese altura: ")
# Llama función:
altura = es_numero(altura)
# Convertir a float:
altura = float(altura)

# Calculo área del triangulo:

area = (base * altura) / 2

# Pantalla
print("El área del trabajo es: ", area)