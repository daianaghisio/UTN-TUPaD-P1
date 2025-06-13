#1
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

numero = int(input("Ingrese un número: "))
for i in range(1, numero + 1):
    print("Factorial de", i, "es", factorial(i))

#2
def fibonacci(posicion):
    if posicion == 0:
        return 0
    elif posicion == 1:
        return 1
    else:
        return fibonacci(posicion - 1) + fibonacci(posicion - 2)

hasta = int(input("Ingrese hasta qué posición quiere ver la serie de Fibonacci: "))
for i in range(hasta + 1):
    print(fibonacci(i))

#3
def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)

b = int(input("Ingrese la base: "))
e = int(input("Ingrese el exponente: "))
print("Resultado:", potencia(b, e))

#4
def decimal_a_binario(n):
    if n == 0:
        return ""
    else:
        return decimal_a_binario(n // 2) + str(n % 2)

numero = int(input("Ingrese un número decimal: "))
binario = decimal_a_binario(numero)
if binario == "":
    binario = "0"
print("En binario es:", binario)

#5
def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])

texto = input("Ingrese una palabra: ")
print(es_palindromo(texto))

#6
def suma_digitos(n):
    if n < 10:
        return n
    else:
        return (n % 10) + suma_digitos(n // 10)

numero = int(input("Ingrese un número para sumar sus dígitos: "))
print("Suma de los dígitos:", suma_digitos(numero))

#7
def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)

nivel = int(input("Ingrese el número de bloques en el nivel más bajo: "))
print("Total de bloques necesarios:", contar_bloques(nivel))

#8
def contar_digito(numero, digito):
    if numero == 0:
        return 0
    if numero % 10 == digito:
        return 1 + contar_digito(numero // 10, digito)
    else:
        return contar_digito(numero // 10, digito)

n = int(input("Ingrese un número: "))
d = int(input("Ingrese el dígito a contar: "))
print("Cantidad de veces que aparece:", contar_digito(n, d))
