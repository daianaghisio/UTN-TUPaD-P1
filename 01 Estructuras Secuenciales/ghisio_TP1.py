#Ejercicio 1
print("Hola mundo")

#Ejercicio 2
nombre = input("Ingrese su nombre: ")
print(f"Hola {nombre}!")

#Ejercicio 3
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
lugar = input("Ingrese su lugar de residencia: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {lugar}")

import math

#Ejercicio 4
radio = float(input("Ingrese el radio de un circulo: "))
area = (radio**2)*math.pi
perimetro = radio*2*math.pi
print(f"El area del circulo es: {area} y su perimetro es: {perimetro}")


#Ejercicio 5
segundos = int(input("Ingrese una cantidad de segundos: "))
horas = float(segundos/60/60)
print("La cantidad de horas a las que equivale es: "+ str(horas))


#Ejercicio 6
numero = int(input("Ingrese un numero: "))
print(f"La tabla de multiplicar de {numero} es: ")
print(f"1 x {numero} = " + str(numero))
print(f"2 x {numero} = " + str(numero*2))
print(f"3 x {numero} = " + str(numero*3))
print(f"4 x {numero} = " + str(numero*4))
print(f"5 x {numero} = " + str(numero*5))
print(f"6 x {numero} = " + str(numero*6))
print(f"7 x {numero} = " + str(numero*7))
print(f"8 x {numero} = " + str(numero*8))
print(f"9 x {numero} = " + str(numero*9))
print(f"10 x {numero} = " + str(numero*10))


#Ejercicio 7
print("Ingrese dos numeros distintos de cero: ")
numero = input()
numero2 = input()

suma = int(numero) + int(numero2)
division = float(int(numero) / int(numero2))
multiplicacion = int(numero) * int(numero2)
resta = int(numero) - int(numero2)

print(f"La suma de los numeros ingresados es: {suma}, la division da como resultado: {division}, el producto es: {multiplicacion} y la resta: {resta}")

#Ejercicio 8
altura = float(input("Ingrese su altura en metros: "))
peso = float(input("Ingrese su peso en kilos: "))

indice = peso / (altura**2)
print(f"Su indice de masa corporal es: {indice}")

#Ejercicio 9
celsius = float(input("Ingrese la temperatura en Celsius: "))
fahrenheit = (9/5)*celsius + 32

print(f"La temperatura en fahrenheit es: {fahrenheit}")

#Ejercicio 10
print("Ingrese tres numeros a continuacion: ")
num1 = float(input())
num2 = float(input())
num3 = float(input())
promedio = float((num1+num2+num3)/3)
print(f"El promedio de los mismos es: {promedio}")