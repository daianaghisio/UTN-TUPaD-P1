#Ejercicio 1

edad = int(input("Ingrese su edad: "))

if edad > 18:
    print("Es mayor de edad")

#Ejercicio 2

nota = int(input("Ingrese su nota: "))

if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

#Ejercicio 3
numero = int(input("Ingrese un número: "))

if numero % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")

#Ejercicio 4
edad = int(input("Ingrese su edad: "))

if edad < 12:
    print("Niño/a")
elif edad >= 12 and edad < 18:
    print("Adolescente")
elif edad >= 18 and edad < 30:
    print("Adulto/a joven")
else:
    print("Adulto/a")

#Ejercicio 5
contrasena = input("Ingrese una contraseña: ")
longitud = len(contrasena)

if longitud >= 8 and longitud <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#Ejercicio 6
import random
from statistics import mean, median, mode

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
moda = mode(numeros_aleatorios)

if media > mediana and mediana > moda:
    print("Sesgo positivo o a la derecha")
elif media < mediana and mediana < moda:
    print("Sesgo negativo o a la izquierda")
elif media == mediana and mediana == moda:
    print("Sin sesgo")
else:
    print("No se puede determinar un sesgo claro")

#Ejercicio 7

texto = input("Ingrese una frase o palabra: ")
ultima_letra = texto[-1].lower()

if ultima_letra == 'a' or ultima_letra == 'e' or ultima_letra == 'i' or ultima_letra == 'o' or ultima_letra == 'u':
    print(texto + "!")
else:
    print(texto)

#Ejercicio 8

nombre = input("Ingrese su nombre: ")
opcion = input("Ingrese 1 para imprimir en mayúsculas, 2 para minúsculas, 3 para primera letra en mayúscula: ")

if opcion == "1":
    print(nombre.upper())
elif opcion == "2":
    print(nombre.lower())
elif opcion == "3":
    print(nombre.title())
else:
    print("Opción no válida")

#Ejercicio 9
magnitud = float(input("Ingrese la magnitud del terremoto: "))

if magnitud < 3:
    print("Muy leve (imperceptible)")
elif magnitud >= 3 and magnitud < 4:
    print("Leve (ligeramente perceptible)")
elif magnitud >= 4 and magnitud < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif magnitud >= 5 and magnitud < 6:
    print("Fuerte (puede causar daños en estructuras débiles)")
elif magnitud >= 6 and magnitud < 7:
    print("Muy Fuerte (puede causar daños significativos)")
else:
    print("Extremo (puede causar graves daños a gran escala)")

#Ejercicio 10
hemisferio = input("¿En qué hemisferio estás? (N/S): ").upper()
mes = input("¿Qué mes es? (escribilo en minúsculas, por ejemplo 'marzo'): ")
dia = int(input("¿Qué día es?: "))

meses = {
    'enero': 1, 'febrero': 2, 'marzo': 3,
    'abril': 4, 'mayo': 5, 'junio': 6,
    'julio': 7, 'agosto': 8, 'septiembre': 9,
    'octubre': 10, 'noviembre': 11, 'diciembre': 12
}
mes_num = meses[mes]

if (mes_num == 12 and dia >= 21) or (mes_num in [1, 2]) or (mes_num == 3 and dia <= 20):
    estacion_norte = "Invierno"
    estacion_sur = "Verano"
elif (mes_num == 3 and dia >= 21) or (mes_num in [4, 5]) or (mes_num == 6 and dia <= 20):
    estacion_norte = "Primavera"
    estacion_sur = "Otoño"
elif (mes_num == 6 and dia >= 21) or (mes_num in [7, 8]) or (mes_num == 9 and dia <= 20):
    estacion_norte = "Verano"
    estacion_sur = "Invierno"
elif (mes_num == 9 and dia >= 21) or (mes_num in [10, 11]) or (mes_num == 12 and dia <= 20):
    estacion_norte = "Otoño"
    estacion_sur = "Primavera"
else:
    estacion_norte = "Desconocida"
    estacion_sur = "Desconocida"

if hemisferio == "N":
    print("Estás en", estacion_norte)
elif hemisferio == "S":
    print("Estás en", estacion_sur)
else:
    print("Hemisferio no válido")

