
#Expresiones generadoras en Python
lista = [2,3,5,6,7]

#generamos una lista
listagenerada = [x**2 for x in lista]
print(listagenerada)

listagenerada = [x**2 for x in lista if x > 5]
print(listagenerada)

#Generamos un diccionario con una lista
listanom = ['Marta', 'Pepe', 'Manuel', 'Esteban', 'Pedro', 'Jesus', 'Maria', 'Adrian', 'Luis']

dicNombres = {i:nombre.upper() for i,nombre in enumerate(listanom)}

#Generamos un diccionario con una lista de nombres, pero no pueden haber nombres que empiecen por p
dictNomNoP = {i:nombre for i,nombre in enumerate(listanom) if nombre[0].lower() != 'p'}

print(dictNomNoP)

#Combinando cadenas
cadena1 = 'Hola'
cadena2 = 'Como'

listcadenas = [f'{letra1}{letra2}' for letra1 in cadena1 for letra2 in cadena2]
print(listcadenas)

#Combinando cadenas pero sin repetir los caracteres

listcadenas = [f'{letra1}{letra2}' for letra1 in cadena1 for letra2 in cadena2 if letra1 != letra2]
print(listcadenas)

#Espresiones generadoras ejemplos
# 1 Crea a través de una expresión generadora una lista a través de otra
# en la que se almacenen sin modificar los números mayores a 5, y si son
# menores, se les asigne el valor de 5.
def round5ifless5 (num:int):
    if num >= 5:
        return num
    else:
        return 5

listaOrg = [23,1,2,3,67,10,6,4,7,89,12,11,23,45]
listaGen = [round5ifless5(x) for x in listaOrg]

print(listaGen)

# 2 Crea con ayuda de una/s función o funciones, una lista de solo primos
# de tamaño hasta el número pasado por argumento de la función.
# Utiliza una expresión generadora para crear la lista.
# La función o funciones te puede o pueden ayudar a 
# filtrar pero no a crear directemente la lista.

def is_prime(num:int):
    if num > 3:
        i = 2
        while i <= num//2:
            if not num % i:
                return False
            i += 1
            
    return True

listaPrimos = [x for x in range(100) if is_prime(x) and x > 1]
print(listaPrimos)


