# Ejercicio 5:
# Que dado tres números ingresados por el usuario nos devuelva el promedio

# Función para ver si es un núm: 

def es_numero(num):
    if num.isalpha():
        num = input("No es un número. Ingrese nuevamente: ")
        return es_numero(num)
    elif num.strip() == "":
        num = input("No ingresó nada. Ingrese nuevamente: ")
        return es_numero(num)
    else: 
        return num
    
# Num 1: 
num_1 = input("Ingrese el primer número: ")
num_1 = es_numero(num_1)
num_1 = float(num_1)

# Num 2: 
num_2 = input("Ingrese el segundo número: ")
num_2 = es_numero(num_2)
num_2 = float(num_2)

# Num 3: 
num_3 = input("Ingrese el tercer número: ")
num_3 = es_numero(num_3)
num_3 = float(num_3)

# Calcular promedio: 

def promedio(num_1, num_2, num_3):
    resultado = (num_1 + num_2 + num_3) / 3
    return resultado

promedio = promedio(num_1, num_2, num_3)

# Pantalla.
print("El primer número ingresado: ", num_1)
print("El segundo número ingresado: ", num_2)
print("El tercer número ingresado: ", num_3)
print("El promedio total es: ", promedio)