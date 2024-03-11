
#Funciones anónimas o funciones lambda
a = lambda x: x**2
print(a(2))

# Lambda se utiliza habitualmente como una función que no deba usar más de
# una vez y como clave de ordenación u otros filtros en otras funciones
# ya existentes.

funcListaPrimos = lambda n: [x for x in range(n+1) if is_prime(x) and x > 1]
print(f'La lista de primos hasta el 200 es {funcListaPrimos(200)}')

# Una de las funciones principales de la función lambda es de filtro
# de otras funciones.
# Por ejemplo: como las funciones max(), min(), filter(), sort(), sorted()
# **sort() es el método de objetos iterables y sorted() método general

lista = [223, 5, 12, 34, 67, 456, 23, 45, 123]
print(max(lista))
print(max(lista, key=lambda x: x % 2 != 0))

listaCad = ['Hola', 'Que', 'Adios', 'feo', 'Feo', 'adios', 'zip', 'zop']
print(max(listaCad))
print(max(listaCad, key=len))

# Una de las funciones principales de la función lambda es de filtro
# de otras funciones.
# Por ejemplo: como las funciones max(), min(), filter(), sort(), sorted()
# **sort() es el método de objetos iterables y sorted() método general

lista = [223, 5, 12, 34, 67, 456, 23, 45, 123]
print(max(lista))
print(max(lista, key=lambda x: x % 2 != 0))

listaCad = ['Hola', 'Que', 'Adios', 'feo', 'Feo', 'adios', 'zip', 'zop']
print(max(listaCad))
print(max(listaCad, key=len))

listaEj = [425,3921,1,2,34,45,23,25,56,100]
print(min(listaEj))
print(min(listaEj, key=lambda x: x < 30))

print(sorted(listaEj, key=lambda x : len(str(x))))

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

# Una de las funciones principales de la función lambda es de filtro
# de otras funciones.
# Por ejemplo: como las funciones max(), min(), filter(), sort(), sorted()
# **sort() es el método de objetos iterables y sorted() método general

lista = [223, 5, 12, 34, 67, 456, 23, 45, 123]
print(max(lista))
print(max(lista, key=lambda x: x % 2 != 0))

listaCad = ['Hola', 'Que', 'Adios', 'feo', 'Feo', 'adios', 'zip', 'zop']
print(max(listaCad))
print(max(listaCad, key=len))

listaEj = [425,3921,1,2,34,45,23,25,56,100]
print(min(listaEj))
print(min(listaEj, key=lambda x: x < 30))

print(sorted(listaEj, key=lambda x : len(str(x))))