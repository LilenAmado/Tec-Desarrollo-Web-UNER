# Ejercicio 3:
# Que nos calcule el total de una factura tras aplicarle el IVA. La función debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar, y devolver el total de la factura. Si se invoca la función sin pasarle el porcentaje de IVA, deberá aplicar un 21%

# Verificar si lo ingresado es un número:

def es_numero(num, default=None):
    if num.isalpha():
        num = input("No es un número. Ingrese un número: ")
        return es_numero(num)
    elif num.strip() == "":
        # Esto es para verificar si no ingresó nada, dependiendo si es el iva debería ponerme por default el 21. Entonces consulto por la variable "precio" declarada luego, entra en la segunda condición, pero si es por "iva" entra por la primera. Esto porque la variable "iva" le doy por defecto que si no es agregado nada sea "21".
        if default is not None:
            return default
        else:
            num = input("No ingresó nada. Ingrese un número: ")
            return es_numero(num)

    elif int(num) < 0: 
        num = input("Ingresó un número negativo. Vuelva a ingresar: ")
        return es_numero(num)
    elif int(num) == 0: 
        num = input("Ingresó el número 0. Vuelva a ingresar: ")
        return es_numero(num)
    else: 
        return num



# Calcular precio sin IVA: 
precio = input("Ingrese un precio sin IVA: ")
# Llama función:
precio = es_numero(precio)
# Convertir a float:
precio = float(precio)





# Calcular porcentaje del IVA: 
iva = input("Ingrese el número de porcentaje del IVA (Por defecto es 21): ")
# Llama función:
iva = es_numero(iva, default = 21)
# Convertir a float:
iva = float(iva)



# Función para calcular precio final con iva: 

def calcular_iva (precio, iva):
    resultado = precio * (iva / 100)
    resultado = precio + resultado
    return resultado

# Llamo la función:
precio_final = calcular_iva (precio, iva)

# Pantalla:
print("Precio sin IVA:", precio)
print("Porcentaje del IVA:", iva)
print("El total a pagar seran:", precio_final)