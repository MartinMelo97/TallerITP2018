# Challenge #1 Taller de Python en el ITP (10-Octubre-2018)

#Recibir 2 numeros e imprimir:
#Suma ("La suma es:")
#Resta
#Multiplicacion
#División
#División Entera
#Suma de cuadrados

#CODE

#Recibimos los 2 números
#Recordemos que al utilizar "Input" lo que reciba del teclado será de tipo stringo
#Por lo que ese string que recibimos lo parseamos a tipo entero o flotante, en este caso, entero.

num1 = int(input("Escribe el primer número: "))
num2 = int(input("Escribe el segundo número "))

#Comenzamos a realizar las operaciones solicitadas, almacenando cada una en una variable diferente
suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2
division_entera = num1 //num2
modulo = num1 % num2
suma_cuadrados = num1**2 + num2**2

#Mostramos los resultados, concatenando la leyenda indicada en el challenge con el valor
#Recordemos que para concatenar, podemos usar "+" o ","
#La diferencia es que el operador "+" solo funciona con variables tipo string
#Mientras que el operador "," con cualquier tipo de dato, y agrega un espacio automáticamente
print("---------------------------------")
print()
print("La suma es: " + str(suma))
print("La resta es:", resta)
print("La multiplicación es:", multiplicacion)
print("La division es:", division)
print("La division entera es:", division_entera)
print("El módulo es:", modulo)
print("La suma de cuadrados es:", suma_cuadrados)