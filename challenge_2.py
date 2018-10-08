# Challenge #2 Taller de Python en el ITP (10-Octubre-2018)

#Recibir una frase y realizar lo siguiente:
# - Contar cuentas palabras hay
# - Mostrar la primera palabra
# - Mostrar la frase a partir de la tercera palabra ("Si tiene menos, mostrar mensaje de que es menor a 3 letras")
# - Añadir la palabra "ITPTICS" al final de la frase
# - Invertir la frase
# - Quitar la última palabra (Antes de agregar ITPTICS)
# - Obtener la longitud de la última palabra (Antes de agregar ITPTICS)

#Recibimos la frase desde el teclado con "input", como no haremos operaciones matemáticas con ella
#No es necesario parsear a int o a otro tipo de dato
frase = input("Escribe la frase para este challenge #2: ")

#Creamos una lista la cual contiene cada una de las palabras de la frase, separándolas con split
lista_frase = frase.split(" ")

#Una vez teniendo la lista, utilicemos "len" para contar el numero de elementos que tiene la lista
#Que vendrían siendo el número de palabras en la frase
no_palabras = len(lista_frase)

#Recordemos que las listas tienen indices, lo cuales van de 0 a n, por lo que, si queremos visualizar
#La primer palabra, tendríamos qu acceder al primer elemento de la lista, que tiene un indice 0
primer_palabra = lista_frase[0]



