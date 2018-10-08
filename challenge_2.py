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
print(lista_frase)
#Una vez teniendo la lista, utilicemos "len" para contar el numero de elementos que tiene la lista
#Que vendrían siendo el número de palabras en la frase
no_palabras = len(lista_frase)

#Recordemos que las listas tienen indices, lo cuales van de 0 a n, por lo que, si queremos visualizar
#La primer palabra, tendríamos qu acceder al primer elemento de la lista, que tiene un indice 0
primer_palabra = lista_frase[0]

#Ahora mostraremos la frase desde la tercer palabra
#método "join" permite poder pasar una lista en un string, utilizando el caracter puesto antes de escribir join
#Tambien recordemos que con los breads podemos cortar nuestros strings o listas desde un determinado punto
#En este caso colocaremos [2:] para omitir las 2 primera palabras, mostrando desde la 3ra hasta el fin de la frase
tercer_palabra = lista_frase[2:]
separador = " "
tercer_palabra_en_string = separador.join(tercer_palabra)
print(tercer_palabra_en_string)

#Para añadir la palabra ITPTICS, utilizaremos el método "append" que nos permite añadir nuevos elementos
#a una lista.
#Nuevamente utilizaremos el método "join" para mostrarlo en forma de texto y no de lista

lista_frase.append("ITPTICS")
print(separador.join(lista_frase))

#Invertir la frase es muy sencllo, sólo debemos utilizar el método "reverse" para las listas
lista_frase.reverse()
print(separador.join(lista_frase))

#Ahora quitaremos la última palabra de la lista original, es decir, sin contar la palabra ITPTICS
#Y sin haber invertido la frase, entonces... Pensemos.
#Con la frase invertida, en la lista la palabra ITPTICS pasó de ser el último elemento de la lista al primero
#Por lo tanto tiene un índice 0. Entonces la palabra que estaba antes de ITPTICS (la que nos interesa)
#Al invertir la frase quedó como segundo elemento de la lista, teniendo como índice 1
#Entonces, sabiendo ya en que lugar de la lista quedó la última palabra de la lista origina, basta con
#utilizar el método del
ultima_palabra_original = lista_frase[1]
print("La palabra que ya no debe aparecer abajo es: ", ultima_palabra_original)
del lista_frase[1]
print(lista_frase)
