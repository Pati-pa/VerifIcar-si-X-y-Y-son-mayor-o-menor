# Verificar si un numero X es mayor que Y


print("----------------------------------")
print("-------------Mayor o Menor----------")
print("----------------------------------")
#input

X= int(input("Ingrese X: "))
Y = int(input("INGRESE Y: "))


#Processing

print("-------------------------------")
print("------------RESULTADO----------")
print("-------------------------------")
if X==Y:
    print("Son iguales")
else:
    if X>Y:
        print("El numero " + str(X) + " es mayor que el numero " + str(Y))
    else:
        print("El numero " + str(Y) + " es mayor que el numero " + str(X))