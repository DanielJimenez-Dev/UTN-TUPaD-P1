# Trabajo practico 05_Listas
# Alumno: Daniel Alberto Jimenez Valderrama
# Comisión: 12

# Actividades:

# 1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función range.

# en la variable list_mult_4 utilizamos la funcion de list, e indicamos os parametros que inicie del 1 al 101 en multiplos de 4.
#lis_mult_4 = list(range(1, 101, 4))

#Imprimimos la variable
#print(lis_mult_4)

#----------------------------------------------------------------------------------------------------------

# 2) ) Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el penúltimo. ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el
# indexing con números negativos!

#Inicializamos la variable elemento e incluimos 5 elementos de preferencia.
#elementos = ["UTN", "Comision:12", "Listas", "Programar", "San Nicolas"]

# Creamos un avariable llamada penuiltimo, que representa el penultimo elemento con valor 3
#penultimo = elementos[3]

# imprimimos la variable penultimo
#print(penultimo)

#-------------------------------------------------------------------------------------------------------------------------------------------------

# 3) Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por pantalla.

#Inicializamos una variable llamada lista_vacia con los corchetes []
#lista_vacia = []

# A la variable lista_vacia vamos a agregarle 3 palabras con la funcion append
#lista_vacia.append("Python")
#lista_vacia.append("vscode")
#lista_vacia.append("UTN")

#Renombramos la variable lista_vacia a nueva_lista.
#nueva_lista = lista_vacia

# Imprimimos la nueva lista con la palabras agregadas
#print(nueva_lista)

#-------------------------------------------------------------------------------------------------------------------------------------------------

# 4)  Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”, respectivamente. Imprimir la lista resultante por pantalla. 
# ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el indexing con números negativos! animales = ["perro", "gato", "conejo", "pez"]

# iniciamos tomando la referencia del ejercicio con la variable animales
#animales = ["perro", "gato", "conejo", "pez"]

# reescribiendo la varobale animales le indicamos entre corchetes la posicion que vamos a remplaza[1], y le damos le nuevo valor "loro"
#animales[1] = "loro"

# Hacemos el mismo procedimiento on el siguiente valor
#animales[-1] = "oso"

#Imprimos la lista con los nuevos valores.
#print(animales)

#-------------------------------------------------------------------------------------------------------------------------------------------------

# 5)  Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza

#numeros = [8, 15, 3, 22, 7]
#numeros.remove(max(numeros))
#print(numeros)

# Respuesta: 
# El programa comienza mostrando una lista con 4 elementos numéricos. Luego, utiliza la función remove(max(lista)) para eliminar el valor más alto presente en la lista. 
# Finalmente, imprime la lista actualizada, que ya no contiene ese valor máximo.

#-----------------------------------------------------------------------------------------------------------------------------------------------------

# 6) Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por pantalla los dos primeros.

# Utilizamos list y el gange par aindicar el rango del ejercicio
#num = list(range(10, 31, 5))

#Imprimimos la lista entera de 5 en cinco, iniciando porell valor 10 y finalizando en 30.
#print("Mostramos la lista entera: ",num)

# Mostramos por pantanlla los dos primeros digitos.
#print("Mostramos los dos primeros digitos como lo indica el ejercicio: ", num[:2])

#----------------------------------------------------------------------------------------------------------------------------------------------

# 7) ) Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores
# cualesquiera. autos = ["sedan", "polo", "suran", "gol"]

#autos = ["sedan", "polo", "suran", "gol"]

#autos[1] = "Amarok"
#autos[2] = "Taos"

#print("Lista actualizada: ", autos)

#-----------------------------------------------------------------------------------------------------------------------------------------------

# 8)  Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append directamente. Imprimir la lista resultante por pantalla.

#dobles = []

#dobles.append(5 * 2)
#dobles.append(10 * 2)
#dobles.append(15 * 2)

#print("Lista: [5, 10, 15], lista doble: ",dobles )

#-----------------------------------------------------------------------------------------------------------------------------------------------

# 9) Dada la lista “compras”, cuyos elementos representan los productos comprados por diferentes clientes:

# compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

# a) Agregar "jugo" a la lista del tercer cliente usando append.
# b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
# c) Eliminar "pan" de la lista del primer cliente.
# d) Imprimir la lista resultante por pantalla

#compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

#print("Lista inicial: ", compras)

#a) agregamos jugo a la lista del tercer cliente
#compras[2].append("jugo")

#b) Remplazamos fideos por tallarines en el segundo cliente
#indice_fideos = compras[1].index("fideos")
#compras[1][indice_fideos] = "tallarines"

#c) eliminamos pan de la lista dle primer cliente.
#compras[0].remove("pan")

# d) Imprimimos la listas actualizadas.
#print("Lista Actualizada: ", compras)

#-----------------------------------------------------------------------------------------------------------

# 10) Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos:
# ● Posición lista_anidada[0]: 15
# ● Posición lista_anidada[1]: True
# ● Posición lista_anidada[2][0]: 25.5
# ● Posición lista_anidada[2][1]: 57.9
# ● Posición lista_anidada[2][2]: 30.6
# ● Posición lista_anidada[3]: False
# Imprimir la lista resultante por pantalla.

#lista_anidada = [15, True, [25.5, 57.9, 30.6], False]

#print("Resultado de la lista: ", lista_anidada)

#------------------------------------------------------------------------------------------------------------





