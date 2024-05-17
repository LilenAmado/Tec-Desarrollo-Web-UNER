# Ejercicio 16:
# Que imprima el siguiente patrón

# print(5,4,3,2,1)
# print(4,3,2,1)
# print(3,2,1)
# print(2,1)
# print(1)

x = [5,4,3,2,1]

for i in x: 
    if i == 5:
        print(5,4,3,2,1)
        i -= 1
    elif i == 4:
        print(4,3,2,1)
        i -= 1
    elif i == 3:
        print(3,2,1)
        i -= 1
    elif i == 2:
        print(2,1)
        i -= 1
    elif i == 1:
        print(1)
    else:
        pass

    
    