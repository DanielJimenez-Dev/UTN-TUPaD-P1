# Trabajo Practico de funciones
# ALumno: Daniel Alberto Jimenez Valderrama
# Comisión: 12

# Actividades:

# 1. Crear un afunción llamada imprimir_hola_mundo que imrpima por pantalla el mensaje: "Hola Mundo!", llamar a esta función desde programa principal.

# Definimos función
#def imprimir_hola_mundo():
    #print("Hola mundo!")

# Programa principal
#imprimir_hola_mundo()

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------

# 2. Crea una función llamada saludar_usuario(nombre) que reciba como parámetro un nombre y devuelva un saludo personalizado.
# Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: "Hola Marcos!". 
# Llamar a esta función desde el programa principal solicitado el nombre al usuario.

# Definimos Funcines
#def saludar_usuario(nombre):
    #return "Hola " + nombre + "!"

# Programa principal
#nombre = input("Ingresa tu nombre: ")
#print(saludar_usuario(nombre))

#----------------------------------------------------------------------------------------------------------------------------------------------------------------

# 3. Crear una función llamada informacon_personal(nombre, apellido, edad, residencia) que reciba cuatro parámetros e imprima: 
# "Soy [nombre] [apellido], tengo[edad] años y vivo en [residencia]"
# Pedir los datos al usuario y llamar a esta función con los valores ingresados.

#Definimos funciones

#def informacion_persona(nombre,apellido,edad,residencia):
    #print(f"soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

# programa principal 
# Solicitamos al usurio que ingrese sus datos:
#nombre = input("Ingresa tu nombre: ")
#apellido = input("Ingresa tu apellido: ")
#edad = input("Ingresa tu edad: ")
#residencia = input("Ingresa tu lugar de residencia: ")

#informacion_persona(nombre,apellido,edad,residencia)

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------

# 4. crear dos funciones: calcular_area_circulo(radio) que reciba el radio com parametro y vuelva el area del circulo. 
# calcular el perimetro_circulo(radio) que reciba el radio com parametro y devuelva el perimetro del circulo.
# solicitar radio al usuario y llamar ambas funciiones para mostrar los resultados.

# Definimos PI

#PI = 3.1416

#Definimos funciones

#def calcular_area_circulo(radio):
    #return PI * radio ** 2

#def Calcular_perimetro_circulo(radio):
    #return 2 * PI * radio

#Solicitamos al usuario que iungrese el radio:
#radio = float(input("Ingresa el radio del circulo: "))

#Programa principal

#area = calcular_area_circulo(radio)
#perimetro = Calcular_perimetro_circulo(radio)

#print(f"Área del circulo: {area:.2f}")
#print(f"Perimetro del circulo: {perimetro:.2f}")

#-------------------------------------------------------------------------------------------------------------------

# 5. Crea una funcion llamada segundos_a_horas(segundos) que reciba una cantidad de segundos como párametros y devuelva
# La cantidad de horas corespondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta funcion.

#Definimos la funcion:
#def segundos_a_horas(segundos):
    #return segundos / 3600

#Programa principal
#segundos = int(input("Ingrese la cantidad de segundos: "))
#horas = segundos_a_horas(segundos)
#print(f"{segundos} segundos, equivalen a {horas:.2f} horas")

#--------------------------------------------------------------------------------------------------------------------

# 6. Crear una funcion llamada tabla_multiplicar(numero) que reciba un numero como parametro y imprima la tabla de multiplicar
# de ese numero del 1 al 10. pedir al usuario el numero y llamar a la funcion.

# Definimos funcion
#def tabla_multiplicar(numero):
    #for i in range(1, 11):
        #print(f"{numero} x {i} = {numero * i}")

#Progama principal
#numero = int(input("Ingresa un numero: "))
#tabla_multiplicar(numero)

#-------------------------------------------------------------------------------------------------------------------------

# 7. Crea uan funcion llamada operacion_basica(a, b) que reciba dos numeros como parametros y devuelva una tupla con el resultado de sumarlos,
# restarlos, multiplicarlos y dividirlos. mostrar los resultados de forma clara

#Definimos funciones
#def operaciones_basicas(a, b):
    #return (a + b, a - b, a * b, a / b)

#Programa principal
#a = int(input("Ingresa el primer número: "))
#b = int(input("Ingresa el segundo numero: "))

#suma, resta, multiplicacion, division = operaciones_basicas(a, b)

#print(f"Suma: {suma}")
#print(f"Resta: {resta}")
#print(f"Multiplicacion: {multiplicacion}")
#print(f"Division: {division}")

#----------------------------------------------------------------------------------------------------------------------------

# 8. Crea una funcion llamada calcular_imc(peso, altura) que reciba el peso en kilogramos y la altura en metros y devuelva el indice
# de masa corporal (IMC). Solicitar al usuario los datos y llamar a la funcion para mostrar el resultado con  los dos decimales.

 #Definimos funcion
#def calcular_imc(peso, altura):
    #return peso / (altura ** 2)

#Porgrama principal
#peso = float(input("Ingresa tu peso en Kg: "))
#altura = float(input("Ingresa tu altura en Mts: "))

#imc = calcular_imc(peso, altura)

#print(f"{peso} Peso Kg y {altura} Altura Mts, equivalen a un indice de masa corporal de: {imc:.2f}")

#-------------------------------------------------------------------------------------------------------------------

# 9. Crear una funcion llamada celsius_a_fahrenheit(celsius) que reciba una temperatura en grados celsius y devuelva su equivalencia en Farenheit.
# Pedir al usuario la temperatura en celcius y mostrar el resultado usando la funcion.

#Definimos funcion:

#def celsius_a_fahrenheit(celsius):
    #return (celsius * 9/5) + 32

#Programa principal
#celsius = float(input("Ingresa la temperatura en grados celsius: "))
#farenheit = celsius_a_fahrenheit(celsius)

#print(f"{celsius} °C, equivalen a {farenheit:.2F}°f")

#---------------------------------------------------------------------------------------------------------------------

# 10. Calcular una funcion llamada calcular_promedio(a, b, c) que reciba tres numeros como parametros y devuelva el promedio de ellos
# Solicitar los numero sal usuario y mostrar el resultado mostrando esta funcion:

# Definimos Funcion:

#def calcular_promedio(a, b, c):
    #return (a + b + c) / 3

# Programa principal
#a = int(input("Ingresa el primer numero: "))
#b = int(input("Ingresa el segundo numero: "))
#c = int(input("Ingresa el tercer numero:"))

#promedio = calcular_promedio(a, b, c)
#print(f"El promedio de: {a}, {b}, {c}, corresponde a : {promedio:.2f}")