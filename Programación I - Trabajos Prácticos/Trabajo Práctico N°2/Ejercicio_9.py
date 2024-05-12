# Ejercicio 9:
# Que el usuario ingrese dos números y muestre cuál de los dos es menor. Considerar el caso en que ambos números son iguales.

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

if num_1 < num_2: 
    print(f'El primer número ({num_1}) es menor que el segundo ({num_2})')
elif num_2 < num_1:
    print(f'El segundo número ({num_2}) es menor que el primero ({num_1})')
else: 
    print(f'Ambos números son iguales ({num_1})')