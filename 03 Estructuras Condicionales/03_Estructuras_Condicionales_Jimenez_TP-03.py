#Trabajo Practico Estructuras concionales
#Alumno: Daniel Alberto Jimenez Valderrama
#Dni:95899862

# Actividades

# 1. 1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
# deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

# Solicitamos al usuario que proporcione su edad

#edad = int(input("Por favor proporcione su edad: "))

#Si la edad es mayor a 18 el programa imprime "Usted es mayor de edad"
#if edad > 18:
    #print("Usted es mayor de edad")

# Si el usuario ingresa un numeor menor a 18 el programa imprime " Usted es menor edad"
#else:
    #print("Usted es menor de edad")

#---------------------------------------------------------------------------------------------------------------

# 2.) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
# mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el mensaje “Desaprobado”

#Solicitamos al usuario que ingrese su nota
#nota = int(input("Proporcione su nota:"))

#Si la nota ingresada es mayor o igual a 6, el programa imprime "Aprobado"
#if nota >= 6:
    #print("Aprobado")

# Si el numero ingresado es menor a 6, programa imprime "Desaprobado"
#else:
    #print("Desaprobado")

#-----------------------------------------------------------------------------------------------------------------

# 3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
# número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
# contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
# operador de módulo (%) en Python para evaluar si un número es par o impar.

# Solcitamos al usuario que ingrese un numero 
#numero = int(input("Por favor ingresa un número: "))

#Verificamos si el numero es par
#if numero % 2 == 0:
    #print("Ha ingresado un número par")

# si el numero ingresado no es par el programa imprime "Por favor ingrese un número par"
#else:
    #print("Por favor, ingrese un número par")

#-------------------------------------------------------------------------------------------------------------------

# 4) ) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las siguientes categorías pertenece:
# A. Niño/a: menor de 12 años.
# B. Adolescente: mayor o igual que 12 años y menor que 18 años.
# C. Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
# D. Adulto/a: mayor o igual que 30 años.

#Solicitamos al usuario ingresar su edad
#edad = int(input("Por favor, ingresa tu edad: "))

#Si el usuario ingresa un numero menor a 12 el programa imprime "Niño/a: menor de 12 años."
#if edad < 12:
    #print("Niño/a")

#Si la edad ingresada es mayor o igual a 12 y menor de 18 el programa imprime "Adolecente"
#elif edad >= 12 and edad < 18:
    #print("Adolescente")

#Si la edad ingresada es mayor o igual a 18 y menor a 30, ep programa imprime "Adulto/joven"
#elif edad >= 18 and edad < 30:
    #print("Adulto / Joven")

#Si la edad ingresada es mayor o igual a 30años el programa imprime "Adulto"
#elif edad >= 30:
    #print("Adulto")

#-----------------------------------------------------------------------------------------------------------------------

# 5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
# pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
# de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal como una lista o un string.

# Solicitamos ingresar una contraseña al usuario:
#contrasena = input("Por favor, ingresa un acontraseña entra 8 y 14 caracteres: ")

#Verificamos la longitud de la contraseña es valida
#if 8 <= len(contrasena) <= 14:
    #print("Ha ingresado una contraseña correcta")

# Si la contraseña ingresa nocumple con los parametros el programa imprime "Por favor, ingrese una contraseña de entre 18 y 14 carcateres"
#else:
    #print("Por favor, ingrese una contraseña de entre 18 y 14 carcateres")

#---------------------------------------------------------------------------------------------------------------------------

# 6) escribir un programa que tome la lista numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si
# hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.

#Importamos el paquete ramdom:
#import random
#from statistics import mode, median, mean

# Con la variable num_aleatorios, generamos una lista de 50 números aleatorios entre 1 y 100
#num_aleatorios = [random.randint(1, 100) for i in range(50)]

# Calculamos los valores estadísticos
#media = mean(num_aleatorios)
#mediana = median(num_aleatorios)
#moda = mode(num_aleatorios)

# Imprimimos los valores calculados
#print("Números aleatorios:", num_aleatorios)
#print(f"Media: {media}")
#print(f"Mediana: {mediana}")
#print(f"Moda: {moda}")

# Determinamos el sesgo
#if media > mediana > moda:
    #print("La distribución tiene sesgo positivo (a la derecha).")
#elif media < mediana < moda:
    #print("La distribución tiene sesgo negativo (a la izquierda).")
#elif media == mediana == moda:
    #print("La distribución no tiene sesgo.")
#else:
    #print("La distribución no cumple claramente con ninguno de los sesgos descritos.")

#-----------------------------------------------------------------------------------------------------------------------------------

# 7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
# pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla.

# Solicitamos al usuario ingresar una frase o palabra
#texto = input("Por favor, ingrese una frase o palabra: ")

# con la funcion endswith verificamos si la cadena ingresada termina en una vocal.
#if texto.endswith(('a', 'e', 'i', 'o', 'u',)):
    #Si termina en vocal sumamos el caracter "!"
    #texto += "!"
    #print(f"Resultado: {texto}")

#---------------------------------------------------------------------------------------------------------------------------------

# 8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 dependiendo de la opción que desee:
# 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO. 
# 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
# 3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
# El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(),
# lower() y title() de Python para convertir entre mayúsculas y minúsculas.

# Solcitamos al usuario que ingrese su nombre
#nombre = input("Ingrese su nombre: ")

#Mostramos un menú de opciones al usuario:
#print("¿Cómo desea ver su nombre?")
#print("1. En mayúsculas")
#print("2. En minúsculas")
#print("3. Con la primera letra en mayúscula")

# Le solicitamos al usuario que ingrese una opción (1,2 o 3)
#opcion = input("Ingresa la opción (1, 2 o 3)")

# Agregamos los condcionales para cada opción:

#if opcion == "1":
    #print("Resultado:", nombre.upper())
#elif opcion == "2":
    #print("Resultado:", nombre.lower())
#elif opcion == "3":
    #print("Resultado:", nombre.title())
#else:
    #print("Opción no válida. Por favor ingrese 1, 2 o 3.")

#-----------------------------------------------------------------------------------------------------------------------------------------

# 9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado por pantalla:
# A) Menor que 3: "Muy leve" (imperceptible).
# b) Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
# C) Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero generalmente no causa daños).
# D) Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras débiles).
# E) Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
# F) Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).

# Iniciamos solicitando la magnitud del terremoto al usuario
#magnitud = float(input("Ingrese la magnitud del terremoto (escala de Richter): "))

# segun el numero ingresado clasificamos la magnitud:
#if magnitud < 3:
    #print("Muy leve (imperceptible).")
#elif 3 <= magnitud < 4:
    #print("Leve (ligeramente perceptible).")
#elif 4 <= magnitud < 5:
    #print("Moderado (sentido por personas, pero generalmente no causa daños).")
#elif 5 <= magnitud < 6:
    #print("Fuerte (puede causar daños en estructuras débiles).")
#elif 6 <= magnitud < 7:
    #print("Muy Fuerte (puede causar daños significativos).")
#elif magnitud >= 7:
    #print("Extremo (puede causar graves daños a gran escala).")

#--------------------------------------------------------------------------------------------------------------------------------------------

# 10) Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
# si el usuario se encuentra en otoño, invierno, primavera o verano.

# Iniciamos solicitando los datos al usuario:
#hemisferio = input("¿En qué hemisferio estás? (N/S): ")
#mes = int(input("Ingrese el número del mes (1 a 12): "))
#dia = int(input("Ingrese el día del mes: "))

# Validar si el día y mes son correctos
#if mes < 1 or mes > 12 or dia < 1 or dia > 31:
    #print("Fecha inválida.")
#else:
    # Convertir mes y día en un número para facilitar comparaciones (MMDD)
    #fecha = mes * 100 + dia

# Definir estaciones según hemisferio
#if hemisferio == "N":
    #if 1221 <= fecha or fecha <= 320:
        #estacion = "Invierno"
    #elif 321 <= fecha <= 620:
        #estacion = "Primavera"
    #elif 621 <= fecha <= 920:
        #estacion = "Verano"
    #elif 921 <= fecha <= 1220:
        #estacion = "Otoño"
    
#elif hemisferio == "S":
    #if 1221 <= fecha or fecha <= 320:
        #estacion = "Verano"
    #elif 321 <= fecha <= 620:
        #estacion = "Otoño"   
    #elif 621 <= fecha <= 920:
        #estacion = "Invierno"
    #elif 921 <= fecha <= 1220:
        #estacion = "Primavera"

# Imprimir resultado
#print(f"Te encuentras en la estación: {estacion}")




