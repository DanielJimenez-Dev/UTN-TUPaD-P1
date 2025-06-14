# Alumno: Daniel Alberto Jimenez Valderrama
# Dni: 95899862
# Comisión: 12

# Ejercicios:

# 1. Datos en diccionario precio frutas:
# Precio_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melon': 3000, 'Uva': 1450}

# Añadir las siguientes frutas con su respectivos precios:
# Naranja = 1200
# Manzana = 1500
# Pera = 2300

#Precio_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melon': 3000, 'Uva': 1450}

#Agregamos las frutas con respectivos precios.
#Precio_frutas['Naranja'] = 1200
#Precio_frutas['Manzana'] = 1500
#Precio_frutas['Pera'] = 2300
#print(Precio_frutas)

#--------------------------------------------------------------------------------------------------------------------------------

# 2. Siguiendo con el diccionario precio_frutas que resuelta luego de ejecutar el codigo desarrollado en el punto anterior,
# Actualizar los precios de la siguientes frutas:
# Banana = 1330
# Manzana = 1700
# Melon = 2800

#Actualizamos los precios de Banana, Manzana, Melon.
#Precio_frutas['Banana'] = 1330
#Precio_frutas['Manzana'] = 1700
#Precio_frutas['Melon'] = 2800

#print(Precio_frutas)

#----------------------------------------------------------------------------------------------------------------------------

# 3. Siguiendo el diccionario precio_frutas que sulta luego de ejecutar el codigo desarrollado en el punto anterior, crear una lista que contenga unicamente 
# las frutas sin los precios.

# diciconario
#Precio_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melon': 3000, 'Uva': 1450}

# Utilizamos list y le indicamos el parametro a sustarer en este caso utilizamos keys.
#lista_frutas = list(Precio_frutas.keys())
#print(lista_frutas)

#-------------------------------------------------------------------------------------------------------------------------------

# 4. Escribir un programa que permita almacenar y consultar numeros telefonicos.
# Permitir al usuario cargar 5 contactos con su nombre como clave y numero como valor.
# Luego, pedi unnombre y mouestrale el nmero asociado, si existe.

#Creamos una diccionario vacio, para agregar los contactos
#agenda = {}

# Cargamos los contactos
# Utilizamos siclo for con un rango de 5 segun la solicitud del ejercicio:
#for i in range(5):
    #Solicitamos al usuario ingresar el nombre
    #nombre = input(f"Ingresa el nombre del contacto {i+1}: ")
    #Solicitamos el numero de telefono:
    #numero = input(f"Ingresa el numero de telefono de {nombre}: ")
    #Ingresamos los nombre y nuemros a la variable agenda ya creada.
    #agenda[nombre] = numero

# Consultamos un numero 
#print("Consulta el numero de telefono ")
#consultar = input("Ingresa el nombre de contacto: ")

#Utiliamos codncional If / else para verificar si el contacto ingresao existe:

#if consultar in agenda:
    #print(f"El numero de {consultar} es: {agenda[consultar]}")
#else:
    #print(f"No se encuentra el contacto {consultar}. ")

#-------------------------------------------------------------------------------------------------------------------------

# 5. Solicita al usuario un afrase e imprime:
# Las palabras Unicas(usando set).
# UN diccionario con las cantidades de veces que aparece cada palabra

# SOlicitamos al usuario una frase
#frase = input("Ingresa una frase: ")

#Separamos la frase en palabras (por espacio)
#palabras = frase.split()

#Obtener palabras unicas usando set
#palabras_unicas = set(palabras)

#Contar la cantidad de veces que aparece cad apalabra
#frecuencia_palabras = {}

#for palabra in palabras:
    #if palabra in frecuencia_palabras:
        #frecuencia_palabras[palabra] += 1
    #else:
        #frecuencia_palabras[palabra]= 1

#Mostrar resultados
#print("Palabra unicas: ")
#print(palabras_unicas)

#print("Frecuencia de cada palabra: ")
#for palabra, cantidad in frecuencia_palabras.items():
    #print(f"{palabra}: {cantidad}")

#------------------------------------------------------------------------------------------------------------------------

# 6. Permite ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
# Luego, mostrar el promedio de cada alumno.

# Creamso un diccionario vacio para guardar los alumnos y las notas:

#alumnos = {}

# solicitamos al usuario cargar los dados de 3 alumnos
#for i in range(3):
    #nombre = input(f"Ingresa el nombre del alumno {i+1}: ")
    #Solicitamos al usuario ingresar 3 notas.
    #print(f"Ingresa 3 notas para {nombre}: ")
    #nota1 = float(input("Nota 1: "))
    #nota2 = float(input("Nota 2: "))
    #nota3 = float(input("Nota 3: "))

    #Guardamos las notas como tuplas en el diccionario:
    #alumnos[nombre] = (nota1, nota2, nota3)

#Calculamos el promedioo cada alumno:
#print("Promedio de los alumnos: ")
#for nombre, notas in alumnos.items():
    #promedio = nota1 + nota2 + nota3 / 3
    #print(f"{nombre}: su promedio de notas es: {promedio:.2f}")

#-------------------------------------------------------------------------------------------------------------------

# 7. Dado 2 sets de numeros, reprentando dos listas de estudiantes que aprobaron parcial 1 y parcial 2:
# Mostrar los que aprobaron ambos parciales
# mostrar los que aprobraron solo uno de los dos.
# Mostrar la lista total de estudiante que aprobaron almenos un parcial(sin repetir)

# Creamos 2 listas de estudiantes:
#parcial1 = ["Carlos", "Ana", "Diana", "Luis"]
#parcial2 = ["Luis", "Juan", "Carlos", "Miguel"]

# Combertimos listas a set
#set1 = set(parcial1)
#set2 = set(parcial2)

# Estudiantes que aprobaron ambos parciales
#ambos = set1 & set2
#print("Estudiantes que aprobaron ambos parciales: ", ambos)

# Estudiantes que aprobaron solo uno de los dos:
#solo_uno = set1 ^ set2
#print("Estudiantes que aprobaron solo uno parcial: ", solo_uno) 

# Estuadiantes que aprobaron al menos un parcial 
#al_menos_uno = set1 | set2
#print("Aprobaron al memos un parcial: ", al_menos_uno)

#-------------------------------------------------------------------------------------------------------------------

# 8. Arma un diccionario donde las claves sean nombres de productos
#  permite al usuario:
# Consultar el stock de un producto ingresado.
# Agregar unidades al stock si el producto ya existe
# Agrega un nuevo producto si no existe.

# Creamos un diccionario vacío para guardar los productos y su stock
#stock = {}

# Mostramos el menú en un bucle para que el usuario elija una opción
#while True:
    #print("\n----- MENÚ -----")
    #print("1. Consultar stock")
    #print("2. Agregar unidades a un producto existente")
    #print("3. Agregar un nuevo producto")
    #print("4. Salir")

    #opcion = input("Elegí una opción (1-4): ")

    # Opción 1: Consultar stock
    #if opcion == "1":
        #producto = input("Nombre del producto: ")
        #if producto in stock:
            #print(f"Stock de {producto}: {stock[producto]} unidades")
        #else:
            #print("Ese producto no existe.")

    # Opción 2: Agregar unidades si el producto ya existe
    #elif opcion == "2":
        #producto = input("Nombre del producto: ")
        #if producto in stock:
            #cantidad = int(input("¿Cuántas unidades querés agregar?: "))
            #stock[producto] += cantidad
            #print(f"Nuevo stock de {producto}: {stock[producto]}")
        #else:
            #print("El producto no existe. Usá la opción 3 para agregarlo.")

    # Opción 3: Agregar un nuevo producto
    #elif opcion == "3":
        #producto = input("Nombre del nuevo producto: ")
        #if producto in stock:
            #print("Ese producto ya existe.")
        #else:
            #cantidad = int(input("¿Cuántas unidades tiene?: "))
            #stock[producto] = cantidad
            #print(f"Producto {producto} agregado con {cantidad} unidades.")

    # Opción 4: Salir del programa
    #elif opcion == "4":
        #print("¡Chau! Gracias por usar el sistema.")
        #break

    # Si se elige otra opción no válida
    #else:
        #print("Opción no válida. Por favor elegí del 1 al 4.")

#---------------------------------------------------------------------------------------------------------

# 9. Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.

# Diccionario para guardar la agenda: clave = (día, hora), valor = evento
#agenda = {}

# Menú para el usuario
#while True:
    #print("--- MENÚ DE AGENDA ---")
    #print("1. Agregar evento")
    #print("2. Consultar evento por día y hora")
    #print("3. Ver toda la agenda")
    #print("4. Salir")

    #opcion = input("Elegí una opción (1-4): ")

    # Opción 1: Agregar un evento
    #if opcion == "1":
        #dia = input("Ingresá el día (ej: lunes): ")
        #hora = input("Ingresá la hora (ej: 14:00): ")
        #evento = input("¿Qué evento querés agendar?: ")
        #clave = (dia, hora)  # Creamos una tupla como clave
        #agenda[clave] = evento  # Guardamos el evento
        #print(f"Evento guardado para {dia} a las {hora}.")

    # Opción 2: Consultar qué hay en cierto día y hora
    #elif opcion == "2":
        #dia = input("Ingresá el día a consultar: ")
        #hora = input("Ingresá la hora a consultar: ")
        #clave = (dia, hora)

        #if clave in agenda:
            #print(f"En {dia} a las {hora} tenés: {agenda[clave]}")
        #else:
            #print("No hay ningún evento agendado en ese momento.")

    # Opción 3: Ver toda la agenda
    #elif opcion == "3":
        #if not agenda:
            #print("La agenda está vacía.")
        #else:
            #print("\n--- Agenda completa ---")
            #for (dia, hora), evento in agenda.items():
                #print(f"{dia} a las {hora}: {evento}")

    # Opción 4: Salir
    #elif opcion == "4":
        #print("¡Hasta la próxima!")
        #break

    #else:
        #print("Opción no válida. Elegí un número del 1 al 4.")

#---------------------------------------------------------------------------------------------------------------------------

# 10. Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo diccionario donde:
# Las capitales sean las claves
# Los paises sean los valores 

# Diccionario original: país → capital
#paises_a_capitales = { "Venezuela": "Caracas", "Argentina": "Buenos Aires", "Estados Unidos": "New York", "Chile": "Santiago de Chile", "Uruguay": "Monte Video"}

# Queremos crear uno nuevo: capital → país
#capitales_a_paises = {}

# Recorremos el diccionario original
#for pais, capital in paises_a_capitales.items():
    #capitales_a_paises[capital] = pais  # Invertimos el orden

# Mostramos el nuevo diccionario
#print("Diccionario invertido (capital → país):")
#for capital, pais in capitales_a_paises.items():
    #print(f"{capital}: {pais}")

