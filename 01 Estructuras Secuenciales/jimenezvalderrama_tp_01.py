# Actividad 1. Crear un programa que imprima por pantalla el mensaje: "Hola Mundo"
#print("Hola Mundo")

#-----------------------------------------------------------------------------------------
# Actividad 2. crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando el nombre ingresado.
#Solicitamos al usuario que ingrese su nombre
#nombre = input("Ingresa un tu nombre: ")
#Imprimimos la variable nombre
#print(f"Hola, {nombre}")

#-------------------------------------------------------------------------------------------
# Actividad 3. Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia,
# e imprima por pnatalla una oracion con todos los datos ingresados.
#Solcitamos al usuario nos proporcione, nombre, apellido, edad, residencia
#nombre = input("Indica tu nombre: ")
#apellido = input("Indica tu apellido: ")
#edad = input("Indica tu edad: ")
#residencia = input("Indica en que tu lugar de residencia:")
# Imprimimos las variables, nombre, apellido, edad, residencia.
#print(f"Soy, {nombre} {apellido}, Tengo: {edad} años y vivo en {residencia}")

#-------------------------------------------------------------------------------------------------
# Actividad 4.Crear un programa que pida al usuario el radio de un circuloe imprima por pantalla su área y su perimetro.

#import math

#radio_circulo = float(input("Indica el radio de un circulo: "))
#area = math.pi * radio_circulo**2
#perimetro = 2 * math.pi * radio_circulo

#print(f"El área del circulo es: {area:.2f}")
#print(f"El perímetro del circulo es: {perimetro:.2f}")

#--------------------------------------------------------------------------------------------------

# Actividad 5. Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a cuantas hora equivalen.
# Solicitamos al usuario ingrese los segundos 
#segundos = int(input("Ingresa los segundos, para saber cuantas horas equivalen: "))
#Convertimos los segundos a hora
#hora = segundos / 3600
# Imprimimos el resultado
#print(f"{segundos} segundos, equivalen a {hora:.2f} Horas")

#--------------------------------------------------------------------------------------------------

# Actividad 6. Crear un programa que pida al usuario un numero e imprima por pantalla la tabla de multiplicar de dicho número.

#Solicitamos al usuario qu eingrese el numero
#numero = int(input("Ingresa un número y sabremos la tabla de multiplicar: "))
#Imprimimos el el titulo
#print(f"La tabla de multiplicar del número {numero}, es:")
# Creamos un ciclo for en un rando del 1 al 11:
#for i in range(1 , 11):
#    print(f"{numero} x {i} = {numero * i}")

#---------------------------------------------------------------------------------------------------

# Actividad 7. Crae un programa que pida al usuario dos numeros enteros distintos del 0 y muestre por pantalla 
# el residuo de sumarlos, dividirlos, multiplicarlos y restarlos.

#Solicitamos al usuario ingresar el primer numero
#num1 = int(input("Ingresar el primer numero entero (distinto de 0):  "))
#num2 = int(input("Ingresar el segundo numero entero (distinto de 0):  "))
#Utilizamos el condional para asegurarnos que los numero ingresado son distintos de 0
#if num1 == 0 or num2 == 0:
    #print("Los numeros deben ser distintos de 0")

#else:
    #Cakculamos el residuo de la operacion:
    #residuo_suma = (num1 + num2) % num2
    #residuo_resta = (num1 - num2) % num2
    #residuo_multiplicacion = (num1 * num2) % num2
    #residuo_division = (num1 / num2) % num2

#Imprimimos los resultados:
#print(f"Residuo de la suma: {residuo_suma}")
#print(f"Residuo de la resta: {residuo_resta}")
#print(f"Residuo de la multiplicacion: {residuo_multiplicacion}")
#print(f"Residuo de la division: {residuo_division:.2f}")

#---------------------------------------------------------------------------------------------------------------

# Actividad 8. Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice de masa corporal. 
# Tener en cuenta que el indice de masa coporal se calcula: IMC = Peso en KG / Altura en MTS **2

# Declaramos variables Altura, Peso
#altura = float(input("Ingresa tu altura expresada em MTS: "))
#peso = float(input("Ingresa tu peso expresado en KG: "))
# Declaramos la variable IMC con la formula.
#imc = peso / altura ** 2

#Imprimimos el indice de masa corporal
#print(f" Su altura es:{altura}mts y su Peso {peso} kg, su indice de masa corporal es: {imc:.2f} ")

#--------------------------------------------------------------------------------------------------------------

# Actividad 9. Crear un programa que pida al usuario una tempreratura en grados celsius 
# e imprima por pantalla su equivalente en grados Fahrenheit.

#print("convertidor de temperatura de Celsius a Fahrenheit")
# Declaramos variables
#cels = float(input("Ingresa los G° Celsius: "))
# Creamos la variable de Fahrenheit y aplicamos la formula.
#fah = (cels * 9/5) + 32

# Imprimimos la conversión.
#print(f"{cels} G° Celsius equivalen a {fah} G° Fahrenheit")

#------------------------------------------------------------------------------------------------------------------

# Actividad 10. Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de dichos números

# Solcitamos al usuario que ingrese 3 numeros, declaramos 3 variables  para cada numero ingresado.

print("Promediando 3 valores diferentes.")
num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segúndo número: "))
num3 = int(input("Ingresa el tercer número: "))

# declaramos la variable promedio con la formula correspondiente.
promedio = (num1 + num2 + num3) / 3

#Imprimimos el resultado:
print(f"El promedio de los números: {num1}, {num2}, {num3}, es de: {promedio:.2f}")

#--------------------------------------------------------------------------------------------------------------2