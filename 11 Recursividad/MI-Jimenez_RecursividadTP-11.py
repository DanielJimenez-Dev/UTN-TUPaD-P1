#Alumno: Daniel Alberto Jimenez Valderrama
#Dni: 95899862
#Comision: 12

# Trabajo practico, ejercicos de recursividad:
#-----------------------------------------------------------------------------------------------------------------------------------------------------
# 1. Crea una función recursiva que calcule el factorial de un número.
#  Luego, utiliza esa función para calcular y mostrar en pantalla el factorial de todos los números enteros entre 1 y el número que indique el usuario.

#Creamos una funcion factorial:
#def factorial(n):
    #if n == 0 or n == 1:
        #return 1
    #else:
        #return n * factorial(n - 1)
    
#Creamos funcion para mostra factorial
#def mostrar_factoriales(n, actual=1):
    #if actual <= n:
        #print(f"{actual}! = {factorial(actual)}")
        #mostrar_factoriales(n, actual + 1)

# Solicitamos al usuario queingrese un numero:
#numero = int(input("Ingresá un número entero positivo: "))
#mostrar_factoriales(numero)

#-----------------------------------------------------------------------------------------------------------------------------------------

# 2. crear una funcion recursiva que calcule el valor de la serie de fibonacci en la posicion indicada.
# Posteriormente, muestra la serie completa hasta la posción que el usuario especifique.

# Creamos una funcijn recursiva para el valor de Fibonacci:
#def fibonacci(n):
    #if n == 0:
        #return 0
    #elif n == 1:
        #return 1
    #else:
        #return fibonacci(n - 1) + fibonacci(n - 2)
    
#Creamos una funcion para mostrar la serie hasta posicion indicada:
#def mostar_serie(posicion, actual=0):
    #if actual <= posicion:
        #print(f"Fibonacci({actual}) = {fibonacci(actual)}")
        #mostar_serie(posicion, actual + 1)

#Solicitamos al usuario hatsa donde quiere ver la serie de Fibonacci:
#num = int(input("Ingresa la posicion hasta donde queires ver la serie de Fibonacci: "))
#mostar_serie(num)

#-------------------------------------------------------------------------------------------------------------------------------------

# 3. Crear una fncion recursiva que calcule la potencia de un numero base elevado a un exponente, utilizando la formula 𝑛**𝑚= 𝑛*𝑛**(𝑚−1).
# Prueba esta funcion en un algoritmo general.

#Definimos una funcion para calcular l apotencia:

#def potencia(base, exponente):
    #if exponente == 0:
        #return 1 
    #else:
        #return base * potencia(base, exponente - 1)

#Solcitamos al usuario que ingrese los datos (base, exponente):
#base = int(input("Ingresa la base: "))
#exponente = int( input("Ingresa el exponente: "))

# Calculamos la potencia:
#resultado = potencia(base, exponente)

#Mostramos resultado:
#print(f"{base} elevado a la {exponente} es: {resultado}")

#----------------------------------------------------------------------------------------------

#4. Crear una función recursiva en Python que reciba un numero entero prositivo en base deciaml y devuelva su representancion en binario como una cadena de texto:

#Creamos la funcion recursiva que pase de decimal a binario:
#def decimal_a_binario(n):
    #if n == 0:
        #return " "
    #else:
        #return decimal_a_binario(n // 2 ) + str(n % 2)
    
# Solicitamos al usuari qu eingrese un numero entero positivo:
#numero = int(input("Ingresa un numero entero positivo: "))

#Colocamos un condicional por si el numero ingresa es 0
#if numero == 0:
    #print("0")
#Si no es 0 pasamos de decimal a binario llamando a la funcion.
#else:
    #binario = decimal_a_binario(numero)
    #print(f"El numero {numero} en binario es: {binario}")

#---------------------------------------------------------------------------------------------------

# 5. Implementa una fucnion recursiva llamada es_palindromo(palabra) que reciba una cadena de texto sin espacios ni tildes, y devuelva True si es un palindromo o False si no los es.

# Creamos la funcion es_palindormo:
#def es_palindromo(palabra):
    #if len(palabra) <= 1:
        #return True
    #if palabra[0] != palabra[-1]:
        #return False
    #return es_palindromo(palabra[1:-1])

#Progarama principal
#solicitamos al usuario ingresa un apalabra:

#palabra = input("Ingresa una palabra sin espacios ni tildes: ").lower()

#if es_palindromo(palabra):
    #print(f"{palabra} es un palindromo")
#else:
    #print(f"{palabra} no es palindromo ")

#------------------------------------------------------------------------------------------------------

# 6. Escribir una funcion en python llamada suma_digitos(n), que reciba un numero entero positivo y devuelva la suma de todos sus digitos.

# creamos funcion
#def suma_digitos(numero):
    #if numero < 10:
       #return numero
    #else:
        #return (numero % 10) + suma_digitos(numero // 10)
    
#progra principal
#Solcitamos al usuario ingresar un numero entero posituvo
#numero = int(input("Ingresa un numero entero positivo: "))

#Verificamos que el numeor sea valido
#if numero < 0:
    #print("El numero debe ser postivo")
#else:
    #resultado = suma_digitos(numero)
    #print(f"El numero {numero}, tiene una sunatoria de: {suma_digitos(resultado)}")

#----------------------------------------------------------------------------------------------------------------

# 7. Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n bloques, 
# en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al último nivel con un solo bloque
# Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el nivel más bajo 
# y devuelva el total de bloques que necesita para construir toda la pirámide.

# creamos la funcion recursiva
#def contar_bloques(n):
    #if n == 1:
        #return 1
    #else:
        #return n + contar_bloques(n - 1)
    
#Porgrama principal
#Solcitamos al usuario ingresar el nmero de bloques del nivel mas bajo

#nivel = int(input("Ingresa l acantidad de bloques en el nivel mas bajo: "))

#utilizamos condicionales para validar que sea posituvo:
#if nivel <= 0:
    #print("Debes ingresar un numero entero positivo")
#else:
    #total = contar_bloques(nivel)
    #print(f"Para construir la piramide se necesita {total} bloques.")

#-----------------------------------------------------------------------------------------------

# 8. Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un número entero positivo (numero) 
# y un dígito (entre 0 y 9), y devuelva cuántas veces aparece ese dígito dentro del número.

#Creamos la funcion recursiva:
#def contar_digito(numero, digito):
    #if numero == 0:
        #return 0
    #else:
        #ultimo = numero % 10
        #if ultimo == digito:
            #return 1 + contar_digito(numero // 10, digito)
        #else:
            #return contar_digito(numero // 10, digito)
        
# Programa principal
#Solicitamos al usuario ingresar los datos
#numero = int(input("Ingresa un numero entero positivo: "))
#digito = int(input("Ingresa un digito (0-9): "))

#Utilizamso un condicional para validar la entrada:
#if numero < 0 or not ( 0 <= digito <= 9):
    #print("Entrada invalida, el numero ingresado no corresponde")
#else:
    #resultado = contar_digito(numero, digito)
    #print(f"EL digito {digito} aparece {resultado} veces en el numero {numero}.")


























