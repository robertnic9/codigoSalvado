# Funciones de orden superior
# Son funciones que admiten otras funciones como parámetro
def operacion(a, b, func):
    return func(a,b)

valor = operacion(5,6,int.__add__)
print(valor)

def crea_diccionario(claves:list, valores:list):
    diccion = dict()
    if len(claves) != len(valores):
        return diccion
    else:
        for i, clave in enumerate(claves):
            diccion.update({clave:valores[i]})
        return diccion

print(operacion([1,2,3,4], ['Hola', 'Que', 'Tal', 'Pascual'], crea_diccionario))

#Funciones dentro de funciones
def telf_prefijo(prefijo):
    def telf_num(numeroTelf):
        return f'+{prefijo} {numeroTelf}'
    return telf_num
    
telf_espanol = telf_prefijo(34)
terl_frances = telf_prefijo(33)

print(telf_espanol(625789456))
print(terl_frances(752456123))

#Función de función que genera datos de carnets de identidad
#Usaremos ejemplos de 4 países: España, Italia, Alemania i Francia

def generador_carnets(nombrePais:str, strSexo:str, strNombre:str, 
                      strApellidos:str, strNumero:str):
    def datos_carnet(sexo:str, nombre:str, apellidos:str,
                     numero:str):
        datos =  f'{nombrePais} \n{strSexo}: {sexo} \n'
        datos += f'{strNombre}: {nombre} \n{strApellidos}: {apellidos}\n'
        datos += f'{strNumero}: {numero} \n'
        return datos
    return datos_carnet

carnet_aleman = generador_carnets('Deutsche Republik', 'Geschlecht',
                                  'Vorname', 'Familienname',
                                   'Identitätsnummer')
carnet_espanol = generador_carnets('España', 'Sexo', 'Nombre', 'Apellidos',
                                   'Numero DNI:')
print()
print(carnet_espanol('Mujer', 'Ana', 'Fernández Torres', '48253612Z'))
print(carnet_aleman('Mujeren', 'Ava', 'Brown', 'F123456789V'))

#Memoización
# Se basa en guardar en la memoria de la función 'padre' los resultados
# de ejecuciones de la función interna. Es especialmente útil en situaciones
# en las que para llegar a un resultado es necesario el cálculo de las
# anteriores.
# Aquí también veremos el uso de la función 'timeit' que nos permite
# calcular en segundos el tiempo de ejecución de cualquier código que le 
# pasemos como argumento
# timeit.timeit('nombrefunc(param1,...)', globals=globals(), 
#                number=nº de ejecuciones)

def fib_rec(n):
    if n <= 1:
        return n
    else:
        return fib_rec(n-1) + fib_rec(n-2)
    
def memoize(funcion):
    mem = dict()
    def mem_func(n):
        if n not in mem:
            mem[n] = funcion(n)
        return mem[n]
    return mem_func

mem_fibo_rec = memoize(fib_rec)

import timeit

print('Llamamos a fib_rec(32) 10 veces, tardamos:')
print(timeit.timeit('fib_rec(32)', globals=globals(), number=10))
print()
print('Llamamos a mem_fibo_rec(32) 10 veces, tardamos:')
print(timeit.timeit('mem_fibo_rec(32)', globals=globals(), number=10))
print()
print(timeit.timeit('mem_fibo_rec(33)', globals=globals(), number=10))
print()
print(timeit.timeit('mem_fibo_rec(32)', globals=globals(), number=10))

# Espacios de contextos y nombres
# Las variables de fuera de la función pueden ser accedidas por
# Contenido pero no pueden ser modificacas --> para modificar su contenido
# debemos definirlo con la palabra clave "global"

num = 10

def funcion_ejemplo(x):
    return x + num

print(f'Valor devuelto usando una variable declarada externa = {funcion_ejemplo(5)}')

def funcion_ejemplo2(x):
    global num
    num += x
    return num

print(funcion_ejemplo2(7))

# Espacios de contextos y nombres
# Las variables de fuera de la función pueden ser accedidas por
# Contenido pero no pueden ser modificacas --> para modificar su contenido
# debemos definirlo con la palabra clave "global"
import time

num = 10

def funcion_ejemplo(x):
    return x + num

print(f'Valor devuelto usando una variable declarada externa = {funcion_ejemplo(5)}')

def funcion_ejemplo2(x):
    global num #Recordamos que la variable num es Global definida en "main"
    num += x
    return num

print(funcion_ejemplo2(7))

# Existen diversos contextos, pero el del programa principal se llama "main"
# Si yo tengo que usar una variable definida en un contexto superior,
# pero no es global, usamos la palabra clave "nonlocal" para definir
# el nombre de esa variable e indicar que no pertenece a ese contexto
# sinó a uno superior.