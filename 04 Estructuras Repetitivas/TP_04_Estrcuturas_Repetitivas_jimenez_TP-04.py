# Alumno: Daniel Alberto Jimenez Valderrama
# Dni:95899862
# Comision: 12

#04 Ejercicios de Estructuras Repetitivas

# Actividades:
# 1) Crear un programa que imprima en pantalla todos los numeros enteros desde 0 al 100 (incluyendo ambos extremos)
# en orden creciente, mostrando un numero por linea:

# Imprimimos los nímeros del 0 al 100, uno por linea utilizando un ciclo for, 
# utilizo un ciclo for por que el ejercicio me indica la cantidad de veces que se va arrepetir, en este caso hasta el 100.

#for i in range(101):
    #print(i)

#------------------------------------------------------------------------------------------------------------------

# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de digitos que contiene.

# Solicitamos al usuario que ingrese un numero entero
#numero = input("Ingresa un número entero: ")

#Inicializamos el contador que llamaremos "i" en 0
#i = 0
# Utilizaremos el ciclo while por que sabremos segun el numero ingresado la cantidad de digitos a contar
#while i < len(numero):
    #i += 1 #Aumentamos a 1 nuestro contador de digitos

#Imprimimos la cantidad de digitos ingresados:
#print("Cantidad de digitos: ",numero, ", Corresponde a :", i, "Números ingresados")

#---------------------------------------------------------------------------------------------------------------------

# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores dados por el usurio,
# Excluyendo esos dos valores.

#Solicitamos al usuario ingrese dos numeros enteros;
#num_1 = int(input("Ingresa el primer número entero: "))
#num_2 = int(input("Ingresa el segundo número entero: "))

# Podemos asegurarnos que el numero inical sea menor, asi el programa recorrera de menor a mayor;
#if num_1 > num_2:
    #num_1,num_2 = num_2, num_1

# Inicializamos la variable suma en 0
#suma = 0

#Utilizamos un ciclo for, con la funcion range excluimos los valores extremos;
#a la variable num_1 le agregamos un +1 para que inicie el conteo con el numero que sigue del numero ingresado.
#for i in range(num_1 + 1, num_2):
    #suma += i #Sumamos cada número intermedio

#Imprimimos la sumatoria de los numero que se encuentran dentro del gango ingresado.
#print("La suma de los números entre: ",num_1, "y", num_2, "es: ", suma)

#-----------------------------------------------------------------------------------------------------------------------

# 4) Elabora un programa que permita al usuario ingresar números enteros y lo sume en secuencia.
# El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0

#Iniciamos creando una variable con el valor de True para detener el programa
#detener_programa = True

# Inicializamos la variable suma en 0
#suma = 0

#Utilizamos un ciclo while, que indique la sumatoria de todos los numeros enteros, hasta tanto el usuario ingrece 0 para detener
#while detener_programa:
    #Solcitamos al usuario ingresar los numeros enteros
    #numero = int(input("Ingresa un número entero (0 para terminar): ")) 
    # Iindicamos la condicion if, donde numeor es igual a 0 entonces la variable detener_programa pasa a False, y detiene el ciclo.
    #if numero == 0:
        #detener_programa = False
    #Indicamos la condicion else donde se encuentra la sumatoria de los numero enteros ingresados por el usuario.
    #else:
        #suma += numero

#print("La suma total de los números enteros ingresesados es de: ", suma)
        
#------------------------------------------------------------------------------------------------------

# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

# Definimos un numero manualmente en la variable numero_secreto para identificar el numero que debe adivinar el usuario
#numero_secreto = 5

#Creamos la variable intentos y la inicializamos en cero para llevar un conteo
#intentos = 0
#Creamos una variable que llamaremos num_acertado y le daremos el valor de False, su funcion sera cuando el usuario marque 5 pasara a True y detener el ciclo parar el juego
#acertado = False

#Utilizamos ciclo while 
#while not acertado:
    #Solcitamos al usuario ingresar un numero
    #intento = int(input("Adivina el número secreto (Debes seleccionar del 0 a 9): "))
    #hacemos la sumatoria de los intentos
    #intentos += 1

    # Condcionamos si la variable intento es igual a numero secreto, entonces:
    #if intento == numero_secreto:
        # La variable acertado pasa a True
        #acertado = True

    # Sino, imprimimimos numero incorrecto, intentetalo de nuevo
    #else:
        #print("Número incorrecto, intenta de nuevo!!")

#S i el usuario ingresa el numero correcto imprimos la canntidad de intentos.
#print("Correcto, adivinaste el número en: ", intentos, "Intentos.")

#---------------------------------------------------------------------------------------------------------------

# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos entre 0 y 100, en orden decreciente.

#Utilizamos un ciclo for con la funcion range, le indicamos al programa que son 100 numeros de los cuales deben ser impresos de forma decreciente -1, y indicamos que solo los pares -2

#for  numero in range(100, -1, -2):
    #print(numero)

#---------------------------------------------------------------------------------------------------------------

# 7) ) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un número entero positivo indicado por el usuario.

#Inicialiamos la variable llamada num_ingresado,solicitamos al usuario ingresar un numero entero positivo
#num_ingresado = int(input("Ingresa un número entero positivo: "))
# Inicializamosuna variable llamada suma que sera nuestro contador
#suma = 0

#Generamos nuestro ciclo for
#for i in range(num_ingresado + 1):
    #suma += i

#print("La suma de los números de 0 a",num_ingresado,"es: ",suma)

#-----------------------------------------------------------------------------------------------------------------

# 8) ) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad menor, pero debe estar preparado para procesar 100 números con un solo cambio).

# Inicializamos los contadores:
#pares = 0
#impares = 0
#positivos = 0
#negativos = 0

# cramos nuestro ciclo for y pedimos al usuario que ingrese los 100 numeros
#for i in range(1, 101):
    #numero = int(input("Ingrese el numero: "))

    #Creamos los contadores de pares e impares:
    #if numero % 2 == 0:
        #pares += 1
    #else:
        #impares += 1

    #Creamos los contadores positivo y negativo:
    #if numero > 0:
        #positivos += 1

    #elif numero < 0:
        #negativos += 1

#Imprimimos los resultados 
#print("Números pares: ", pares)
#print("Numeros impares: ",impares)
#print("Numeros positivos: ",positivos)
#print("Numeros negativo: ",negativos)

#---------------------------------------------------------------------------------------------------------------------------

# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
#poder procesar 100 números cambiando solo un valor).

#Inicializamos un variable indicando el total de numeros a ingresar
#total_numeros = 100
# Inicializamos una variable suma en 0
#suma = 0

#Creamos un ciclo for con la funcion range:
#for i in range(1, total_numeros + 1):
    #numero = int(input("Ingrese un numero: "))
    #suma += numero

#media = suma / total_numeros
#print("La media es: ",media)

#---------------------------------------------------------------------------------------------------------------------------

# 10) ) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

# Solicitamos al usuario ingresar un numero
#numero = int(input("Ingresa un número: "))
#numero_invertido = 0

#Creamos un ciclo while 
#while numero > 0: 
    #ultimo_digito = numero % 10
    #numero_invertido = numero_invertido * 10 + ultimo_digito
    #numero //= 10

#Imprimimos los numeros invertidos.
#print("Número invertido: ",numero_invertido)
