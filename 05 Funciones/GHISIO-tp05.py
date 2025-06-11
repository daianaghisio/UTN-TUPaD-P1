#1
def imprimir_hola_mundo():
    print("Hola Mundo!")

imprimir_hola_mundo()


#2
def saludar_usuario(nombre):
    return "Hola " + nombre + "!"

nombre = input("Ingrese su nombre: ")
print(saludar_usuario(nombre))


#3
def informacion_personal(nombre, apellido, edad, residencia):
    print("Soy", nombre, apellido + ", tengo", edad, "años y vivo en", residencia + ".")

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su lugar de residencia: ")
informacion_personal(nombre, apellido, edad, residencia)


#4
def calcular_area_circulo(radio):
    return 3.14 * radio * radio

def calcular_perimetro_circulo(radio):
    return 2 * 3.14 * radio

radio = float(input("Ingrese el radio del círculo: "))
print("Área del círculo:", calcular_area_circulo(radio))
print("Perímetro del círculo:", calcular_perimetro_circulo(radio))


#5
def segundos_a_horas(segundos):
    return segundos / 3600

segundos = int(input("Ingrese la cantidad de segundos: "))
print("Equivalente en horas:", segundos_a_horas(segundos))


#6
def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(numero, "x", i, "=", numero * i)

numero = int(input("Ingrese un número para ver su tabla de multiplicar: "))
tabla_multiplicar(numero)


#7
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    if b != 0:
        division = a / b
    else:
        division = "Indefinida (división por cero)"
    return (suma, resta, multiplicacion, division)

a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))
resultados = operaciones_basicas(a, b)
print("Suma:", resultados[0])
print("Resta:", resultados[1])
print("Multiplicación:", resultados[2])
print("División:", resultados[3])


#8
def calcular_imc(peso, altura):
    return peso / (altura * altura)

peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))
imc = calcular_imc(peso, altura)
print("Su IMC es:", round(imc, 2))


#9
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

celsius = float(input("Ingrese la temperatura en Celsius: "))
fahrenheit = celsius_a_fahrenheit(celsius)
print("Equivalente en Fahrenheit:", fahrenheit)


#10
def calcular_promedio(a, b, c):
    return (a + b + c) / 3

a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))
c = float(input("Ingrese el tercer número: "))
promedio = calcular_promedio(a, b, c)
print("El promedio es:", promedio)
