import re
''' Crea una funció que converteixi a majúscula la primera lletra de cada paraula d’un string. 
També, aquesta funció, haurà de comptar el nombre de paraules y eliminar l’existència de més d’un espai entre paraules. 
Pots fer servir expressions regulars per crear aquesta funció.'''



'''Crea una funció que comprovi si un password és correcte, és a dir,
si té almenys 2 majúscules i 2 caràcters especials (‘%$·”!ª=)(/\_-^[]{}<>*€#~¬). A més, aquests caràcters
no han d’estar seguits un de l’altre, és a dir, que entre les majúscules i els caràcters especials hi ha d’haver 
al menys 1 caràcter estàndard (les majúscules i els caràcters especials poden ser alterns, no tens perquè trobar
primer les majúscules i després els caràcters especials ni viceversa). També s’haurà de comprovar que la contrasenya
tingui entre 10 y 14 caràcters.'''

import re

def comprovar_password(password):
    # Verificar longitud entre 10 y 14 caracteres y que no haya secuencias no deseadas
    if not re.match(r"^(?!.*(?:[A-Z]%[A-Z]|%[A-Z]|[A-Z]%|[A-Z]{2}|%{2}))[a-zA-Z\d%$·\"!ª=)(/\\_\-^[\]{}<>*€#~¬]{10,14}$", password):
        return False

    return True

# Ejemplo de uso:
password1 = "AbCdEfG%H#1"
password2 = "Aa$Bb%CcDdEe"

print(comprovar_password(password1))  # Output: True
print(comprovar_password(password2))  # Output: False
