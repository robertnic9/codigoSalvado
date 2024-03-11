import re

#Exercicis expressions regulars
# Quines cadenes seríen vàlides per les expressions regulars següents?

expreg1 = r'^([^!@#$%^&*]*[!@#$%^&*]){3}[^!@#$%^&*]*$'
expreg2 = r'^([!@#$%^&*]){3}[^!@#$%^&*]*$'
listacadenas = ['@hola *que tal&', '!@$ amigo', 'hoy no se que hago @%&']

for cadena in listacadenas:
    if re.search(expreg1, cadena):
        print(f'La expresion regular {expreg1} valida la cadena {cadena}')
    if re.search(expreg2, cadena):
        print(f'La expresion regular {expreg2} valida la cadena {cadena}')

# Crea un codi que mitjançant una expressió regular
# validi una contrasenya que tingui entre 8
# i 12 caràcters però que al menys tingui una lletra majúscula, un caràcter
# especial i 3 xifres
# El lookahead (?=.*[A-Z]) nos busca si existe al menos una mayúscula, nos 
# devuelve cierto o faso si está o no respectivamente pero no consume caracteres

expregBernardo = r'(?=.*[A-Z][!@#$%^&*][\d]{3}){8,12}' #No tiene sentido
expreg = r'(?=.*[A-Z])(?=.*[!@#$%^&*])(?=(.*\d){3})(?=.{8,12}$)'

contrasenya = 'Ahola?3a5b6D'

if re.search(expregBernardo, contrasenya):
    print(f'La expresion {expregBernardo} funciona para la contraseña {contrasenya}')
else:
    print(f'Bernardo, to expresion regular {expregBernardo} no funciona')

listacontr = ['Ahola#3a5b6D', 'gatoPato123%', 'contrasenyainvalida', 
              'culito234$', '%mesa689Poya', 'Qlon@699', 'hola#que568',
              'A5B6C8#   ']

print()
for contrasena in listacontr:
    if re.search(expreg, contrasena):
        print(f'La contraseña {contrasena} es válida')
    else:
        print(f'La contraseña {contrasena} es inválida')