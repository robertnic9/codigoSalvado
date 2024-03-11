# Decoradores
def temporizar(func):
    def funcion_interna(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        intervalo = time.time() - inicio
        print(f'Funcion {func.__name__} tardó en ejecutarse',end='') 
        print(f' {intervalo} segundos usando los argumentos {args} y {kwargs}', end='')
        return resultado
    return funcion_interna

def convierte_formato(cadena:str):
    listaElems = list(cadena)
    lista_final = []
    for c in listaElems:
        elem = c.lower() if c.lower() > 'p' else c.upper()
        """
        if elem.lower() > 'p':
            elem = c.lower()
        else:
            elem = c.upper()    """
        lista_final.append(elem)
    return ''.join(lista_final)

tiempo_formato = temporizar(convierte_formato)
print(f' con resultado {tiempo_formato("Hola que tal Pascual, janders")}')

# Function suma realizes the addition of all elements of a list of integers
@temporizar
def suma_elementos(elems:list[int|float]) -> int|float:
    '''This function returns the sum of all integers in a list.'''
    suma = 0
    for elem in elems:
        suma += elem
    return suma

lista = [1,2,3,4,5,6,7,8,9,11,12,13,45,67,1000]
print(f' con resultado {suma_elementos(lista)}')

# Objetos equivalentes que evaluamos como True --> "truthy".
# Objetos equivalentes que evaluamos como False --> "falsy".

# ¿Qué es equivalente al booleano True pero no es de tipo Bool?
# 1 - Cualquier número diferente de 0. Ej -> 45, -123 serían ambos True
# 2 - Cualquier string NO vacío. Ej 'a' or 'hola' se evaluan como True
# No hacemos if formato('texto') != '', sino directamente if formato('texto')
# 3 - Cualquier contenedor de datos NO vacío. listas, tuplas, diccionarios,
# sets NO vacíos.
# 4 - Cualquier objeto personalizado que tenga uno o más métodos que devuelvan
# un booleano o otro elemento evaluable como booleano.

# ¿Qué es equivalente al booleano False pero no es de tipo Bool?
# Pues lo contrario que en los casos anteriores.
print(suma())