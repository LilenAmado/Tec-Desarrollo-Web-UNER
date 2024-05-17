# Ejercicio 12:
# Pedir al usuario que ingrese un día de la semana e imprimir un mensaje si es lunes, otro mensaje diferente si es viernes, otro mensaje diferente si es sábado o domingo. Si el día ingresado no es ninguno de esos, imprimir otro mensaje

dia_semana = input("Ingrese un día de la semana: ")

if dia_semana == "lunes" or dia_semana == "Lunes":
    print("Eligió el día Lunes, BUUU")
elif dia_semana == "viernes" or dia_semana == "Viernes":
    print("Es viernes y tu cuerpo lo sabe")
elif dia_semana == "sabado" or dia_semana == "Sabado" or dia_semana == "sábado" or dia_semana == "Sábado":
    print("Sabadunguiiiii")
elif dia_semana == "domingo" or dia_semana == "Domingo":
    print("Domingo, mañana hay que volver a trabajar :(")
else: 
    print("No es ni Lunes, Viernes, Sábado ni Domingo")