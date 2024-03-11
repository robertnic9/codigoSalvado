# Expressions regulars.
import re

regexp = r'\d{8}[A-Z]'
string = '09345687C'
string2 = 'hola que tal'
string3 = ' 09345687C'
string4 = '02314568B  01234569D hola que tal 45231245V, 21365479c'
lista = [string, string2, string3, string4]

# 1 re.match(expresion regular, string, flags=0)
# Busca una coincidencia solo al principio del texto, es decir, en su inicio.
# Devuelve el string coincidente con la expresión regular o, si no coincide,
# devuelve None.

for cadena in lista:
    if re.match(regexp, cadena):
        print(f'la cadena "{cadena}" coincide con la expresión regular {regexp}')
    else:
        print(f'la cadena "{cadena}" NO coincide con la expresión regular {regexp}')

# 2. El  método re.search(expresion regular, string, flags=0)
# Escanea el string buscando la PRIMERA ubicación donde coincide un patrón
#  con la expresión regular. Devuelve el string coincidente si lo encuentra
# en caso contrario, devuelve None.

print()
for cadena in lista:
    if re.search(regexp, cadena):
        print(f'la cadena "{cadena}" coincide con la expresión regular {regexp}')
    else:
        print(f'la cadena "{cadena}" NO coincide con la expresión regular {regexp}')

# 3. El método findall(expresion regular, string, flags=0)
# Encuentra todas las coincidencias de la expresión regular en el string
# y las devuelve en una lista, en caso contrario, devuelve una lista vacía.

print()
for cadena in lista:
    listaCoincid = re.findall(regexp, cadena)
    if listaCoincid:
        print(f'la cadena "{cadena}" coincide con la expresión regular {regexp}')
        print(f'Y la función re.findall() me ha devuelto {listaCoincid}')
    else:
        print(f'la cadena "{cadena}" NO coincide con la expresión regular {regexp}')

# 4. El método finditer(expresion regular, string, flags=0)
# Igual que el findall pero devuelve un iterador que proporciona información 
# sobre las coincidencias. Se usa con un for, cada coincidencia del iterador
# devuelto tiene = coincidencia.group() = es el string que coincide con la
# expresión regular, coincidencia.start() = devuelve la posición de inicion
# de la coincidencia en el string y coincidencia.end() que me devuelve la 
# posición final de dicha coincidencia dentro del string.

print()
print()
for coincidencia in re.finditer(regexp, string4):
    print(f'La coincidencia {coincidencia.group()} ha empezado en', end='')
    print(f' la posición {coincidencia.start()} y ha finalizado en', end='')
    print(f' la posición {coincidencia.end()} del string {string4}')

# 5. Método re.sub(exp. regular, string reemplazo, string, count=0, flags=0)
# Reemplaza las coincidencias de la expresión regular en el 'string'
# por el 'string reemplazo'. Devuelve el string con las modificaciones
# realizadas por el reemplazo.
# count = 0 implica reemplazar a todas las coincidencias.
print()
print()
print(f'El texto original sin reemplazos es: {string4}')
print(f'El texto original reemplazado es: ', end='')
print(re.sub(regexp, 'mariposon', string4))

# 6. El método re.split(exp. reg., string, maxsplit=0, flags=0)
# Devuelve una lista de cadenas resultante de dividir el 'string' por todas
# las coincidencias de la expresión regular. El parámetro maxspit és el
# número máximo de divisiones donde 0 implica sin límite de divisiones.

print('Hola que , tal   ,Pascual'.split())
print(re.split(r'[\W]+', 'Hola que , tal   ,Pascual'))

# 7. El método re.complie(exp. reg., flags=0)
# Compila una expresión regular r'...' y la convierte en un objeto
# del tipo re a partir del cual se podrá invocar a todas las funciones 
# anteriores sin necesidad de usar el argumento 'exp. reg.'

print()
print()
expregDni = re.compile(r'\d{8}[A-Z]')
print(expregDni.search(string4))
print(re.search(r'\d{8}[A-Z]', string4))
