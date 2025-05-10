#Ejercicio 1 
for i in range(101):
    print(i)

#Ejercicio 2
num = input("Ingrese un número: ")
cantidad_digitos = len(num)
print(num + " tiene " + str(cantidad_digitos) + " dígitos")

#Ejercicio 3

num1 = int(input("Ingrese un número entero: "))
num2 = int(input("Ingrese otro mas: "))

suma = 0
if num2>num1:
    num2 -= 1
    while num2>num1:
        suma += num2
        print("sumo: "+str(num2))
        num2 -= 1

    print("La suma de los números intermedios es:", suma)
else:
    num1 -= 1
    while num1>num2:
        suma += num1
        print("sumo: "+str(num1))
        num1 -= 1

    print("La suma de los números intermedios es:", suma)
   
#Ejercicio 4
numIngresado = -1
total = 0
while numIngresado != 0:
    numIngresado = int(input("Ingrese un número entero positivo: "))
    total += numIngresado
print("La suma de los números ingresados es:", total)


#Ejercicio 5
import random
numAAdivinar = random.randint(0,9)
numero = -1
intentos = 0
while numero != numAAdivinar:
    numero = int(input("Ingrese un número entero del 1 al 9: "))
    intentos += 1

print("La cantidad de intentos hasta acertar fue de: ", intentos)
 

#Ejercicio 6
cien = 100
for cien in range(cien,0,-2):
    print(cien)

#Ejercicio 7
numIngresado = int(input("Ingrese un número entero positivo: "))
totalSuma = 0
while numIngresado != 0:
    totalSuma += numIngresado
    numIngresado -= 1
print("La suma de los números ingresados es:", totalSuma)


#Ejercicio 8
pares = 0
impares = 0
positivos = 0
negativos = 0

cantidad = 10  # 100

i = 1
while i <= cantidad:
    numero = int(input(f"Ingresá el número {i}: "))

    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1

    i += 1

print("Cantidad de números pares:", pares)
print("Cantidad de números impares:", impares)
print("Cantidad de números positivos:", positivos)
print("Cantidad de números negativos:", negativos)


#Ejercicio 9
suma = 0
cantidad = 10  #100

i = 1
while i <= cantidad:
    numero = int(input(f"Ingresá el número {i}: "))
    suma += numero
    i += 1

media = suma / cantidad
print("La media de los números ingresados es:", media)


#Ejercicio 10
numero = int(input("Ingresá un número entero positivo: "))

invertido = 0
while numero != 0:
    digito = numero % 10
    invertido = invertido * 10 + digito
    numero = numero // 10

print("El número invertido es:", invertido)