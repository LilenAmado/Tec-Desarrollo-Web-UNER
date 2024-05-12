# Ejercicio 2:
# Que reciba un número entero positivo y una potencia a elevar y que nos devuelva el resultado
#https://www.freecodecamp.org/espanol/news/operadores-basicos-en-python-con-ejemplos/
# https://platzi.com/tutoriales/4227-python/31266-metodos-de-strings-en-python-domina-el-poder-de-las-cadenas-de-texto/

# Función para ver si es un núm positivo entero: 

def es_numero(num):
    if num.isalpha():
        num = input("No es un número. Ingrese un número entero positivo: ")
        return es_numero(num)
    elif num.strip() == "":
        num = input("No ingresó nada. Ingrese un número entero positivo: ")
        return es_numero(num)
    elif "." in num or "," in num: 
        num = input("No ingresó un número entero positivo. Vuelva a ingresar: ")
        return es_numero(num)
    elif int(num) < 0: 
        num = input("Ingresó un número negativo. Vuelva a ingresar: ")
        return es_numero(num)
    elif int(num) == 0: 
        num = input("Ingresó el número 0. Vuelva a ingresar: ")
        return es_numero(num)
    else: 
        return num

# Num positivo entero:
num_entero_positivo = input("Ingrese un número entero positivo: ")
num_entero_positivo = es_numero(num_entero_positivo)

# Num potencia:
num_potencia = input("Ingrese un número entero positivo para la potencia: ")
num_potencia = es_numero(num_potencia)

# Muestra de pantalla: Para verificación de como viene
print("El número que eligió es:", num_entero_positivo)
print("El número de potencia que eligió es:", num_potencia)

# Convierto a num:
num = int(num_entero_positivo)
potencia = int(num_potencia)

# Ecuación:
resultado = num ** potencia

# Muestro por pantalla:
print(f'El resultado es: {resultado}')
