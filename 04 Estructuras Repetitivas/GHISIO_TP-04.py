'''#Ejercicio 1 
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
 '''

#Ejercicio 6
cien = 100
for cien in range(cien,0,-2):
    print(cien)

#Ejercicio 7
'''7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
número entero positivo indicado por el usuario.'''