# Ejercicio 13:
# Programe una aplicación de consola que solicite al usuario su nombre, después su apellido y
# a continuación su año de nacimiento. Con esos datos deberá generar una sugerencia de 
# usuario y contraseña. Por ejemplo: nombre: Martín, apellido: Francisconi, Año nacimiento: 
# 1985 -> Usuario: mfrancisconi, Contraseña: mf.1985

# Nombre:
print("¿Cúal es tu nombre?")
nombreUsuario = input()

# Apellido:
print("¿Cúal es tu apellido?")
apellidoUsuario = input()

# Año:
print("¿Cúal es tu año de nacimiento?")
anioUsuario = input()

usuario_sugerido = str(nombreUsuario[:1] + apellidoUsuario[:1] + "." + anioUsuario)

print("El usuario sugerido es: ", usuario_sugerido)

