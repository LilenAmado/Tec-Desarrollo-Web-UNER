# Ejercicio 7
# Escriba un programa Python que cuente con dos listas, la primera de ellas almacenará strings con tareas pendientes y la segunda almacenará strings con tareas terminadas. Permita al usuario:
# a. Agregar nuevas tareas pendientes.
# b. Marcar las tareas pendientes como terminadas. Al hacer esto, la tarea deberá pasar de la lista de pendientes a la de terminadas.
# Nota: posterior a cada operación deberá mostrar por pantalla el estado actual de ambas listas.

###########################################################################

# Defino ambas listas:
lista_tareas_pendientes = []
lista_tareas_terminadas = []

###########################################################################
############## a. Agregar nuevas tareas pendientes. #############

# Tareas pendientes: 

while True:
    tarea_pendiente = input(f'¿Desea agregar una tarea pendiente a la lista? (Escriba "Fin" para terminar el programa):  ')

    if tarea_pendiente.lower() == "fin":
        break 

    lista_tareas_pendientes.append(tarea_pendiente)
    
            # print('Tareas pendientes ingresadas:')

            # for i in range(len(lista_tareas_pendientes)):
            #     print(f'{i} - {lista_tareas_pendientes[i]}')

# Separador en la consola:
print("__________________________________________________________________")

# Tareas finalizadas: 

while True:
    tarea_terminada = input(f'¿Desea agregar una tarea finalizadas a la lista? (Escriba "Fin" para terminar el programa):  ')

    if tarea_terminada.lower() == "fin":
        break 

    lista_tareas_terminadas.append(tarea_terminada)

# Separador en la consola:   
print("__________________________________________________________________")

# Mostrar por consola las tareas tanto finalizadas como pendientes: 

print('Tareas pendientes ingresadas:')

for i in range(len(lista_tareas_pendientes)):
    print(f'{i} - {lista_tareas_pendientes[i]}')

print('Tareas terminadas ingresadas:')

for i in range(len(lista_tareas_terminadas)):
    print(f'{i} - {lista_tareas_terminadas[i]}')

# Separador en la consola:   
print("__________________________________________________________________")

###########################################################################
######### b. Marcar las tareas pendientes como terminadas. Al hacer esto, la tarea deberá pasar de la lista de pendientes a la de terminadas. #######

# Esta función es para verificar si es un número entero. La hacemos para que el usuario pase de pendiente a finalizadas las tareas por medio de sus indices:
# Verificar si es un número entero:
def es_numero(num):
    if num != "fin" or num != "Fin" or num != "FIN":
        return num
    elif num.isalpha():
        num = input("No es un número. Ingrese un número entero positivo: ")
        return es_numero(num)
    elif num.strip() == "" :
        num = input("No ingresó nada. Ingrese un número entero positivo: ")
        return es_numero(num)
    elif "." in num or "," in num: 
        num = input("No ingresó un número entero positivo. Vuelva a ingresar: ")
        return es_numero(num)
    elif int(num) < 0 or int(num) >= len(lista_tareas_pendientes):
        # Para ver si el número que ingresa el usuario para pasar de pendiente a finalizada
        # Lo que realiza es fijarse si el numero ingresado por el usuario es menor a 0 o mayor o igual a la cantidad de valores dentro de la lista, devuelve volver a ingresar otro valor.
        num = input("No hay una tarea guardada en ese valor. Vuelva a ingresar: ")
        return es_numero(num)
    else: 
        return num
    

while True:
    # El usuario ingresa el número perteneciente a la tarea (índice):
    indice_usuario = input(f'Ingrese el número de la tarea que desea pasar de pendiente a finalizada (o escriba "fin" para terminar el programa): ')

    # Se verifica si el usuario quiere terminar:
    if indice_usuario.lower() == "fin":
        break

    # Llama a la función para verificar si es un número:
    indice = es_numero(indice_usuario)

    # Convierte en int el valor de la variable:
    indice = int(indice)
    
    if indice < len(lista_tareas_pendientes):
        # Función para mover tarea de pendiente a terminada:
        def pendiente_a_terminada(indice): 
            lista_tareas_terminadas.append(lista_tareas_pendientes[indice])
            del lista_tareas_pendientes[indice]

        # Llamo a la función para agregar la tarea pendiente a finalizada:
        pendiente_a_terminada(indice)

        # Separador en la consola:   
        print("__________________________________________________________________")

    ################# Nota: posterior a cada operación deberá mostrar por pantalla el estado actual de ambas listas. ############################

        # Mostramos las listas actualizadas:
        print('Tareas pendientes ingresadas:')
        if len(lista_tareas_pendientes) == 0:
            print("No hay tareas pendientes.")
        else:
            for i in range(len(lista_tareas_pendientes)):
                print(f'{i} - {lista_tareas_pendientes[i]}')

        print('Tareas terminadas ingresadas:')
        for i in range(len(lista_tareas_terminadas)):
            print(f'{i} - {lista_tareas_terminadas[i]}')

        # Separador en la consola:   
        print("__________________________________________________________________")

        if len(lista_tareas_pendientes) == 0:
            print("No hay más tareas para pasar. Fin del programa.")
            break

print("__________________________________________________________________")