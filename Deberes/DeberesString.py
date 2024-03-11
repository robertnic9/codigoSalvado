import re 
"""
1 - Crear una expresion regular que compruebe si todas las palabras de un string empiezan por mayuscula

2 - Crea una expresion regular donde se sustituyan los multiples espacios entre palabras por uno solo
"""
#1
vermayus = r"\b[A-Z]\w*\b"

MayusPrueba = ["macaco","mono con Peluca"," Bebe Calvo  Con Bigote "]
for palabra in MayusPrueba:
    coincidencia = re.match(vermayus, palabra)
    if coincidencia:
        print(f"{palabra} es válido.")
    else:
        print(f"{palabra} NO es válido.")
print ()

# 2
textospacios = "Esto        tiene   muchos    espacios."
textosin = re.sub(r'\s+', ' ', textospacios)
print(f"Texto con espacio: {textospacios}")
print(textosin)
print()
# 3 
'''
3 - Crea un expresion regular comprueba si una contraseña tiene al menos 2 letras del abecedario en mayuscula,
 un caracter especial (ºª!¡|".#~$%&/()?¿'[]{}), tiene que haber al menos dos caracteres de otro tipo entre mayúsculas y caracteres especiales.
'''

verfcontras =  r"(?=.{8,})(?=(A-Z)[^\º\ª\!\¡\|\"\.\#\~\$\%\&\/\(\)\?\¿\'\[\]\{\}\]\)\)]{2,})(?=(A-Z){2,})(?=[\º\ª\!\¡\|\"\.\#\~\$\%\&\/\(\)\?\¿\'\[\]\{\}\]\)\)]+)"

#4
'''
4 - Formato coma flotante, formato telefono, formato email, formato contraseña
'''
comaflotante = r"^-?\d+(\.\d+)?$"
print(re.match(comaflotante, "-9.55"))
formatotelefono  =  r"((\+|00)\d{2})?[\s\-]\d{3}[\s\-]\d{2}[\s\-]\d{2}"
print(re.match(formatotelefono, "+34 642 47 18 80"))
formatoemail = r"[\d\w\.-_]+@[\d\w.]+\.[\d\w]+"
print(re.match(formatoemail, "sm23.rnicuta@iessantamariadeivissa.com"))
formatocontra = r"^(?=.*\w)(?=.*\d)(?=.*[!@#$%^&*]).{8,}$"
print(re.match(formatocontra, "#2MecOS2"))
print()

#5
'''
5 - Crea una expresion regular que compruebe que un string empiece por un caracter numerico y que a partir de alli haya minimo 3 combinaciones
    de un caracter de palabra + un caracter especial o de un caracter de palabra + un caracter numerico. 
'''
combi_completa = r"^\d(?=\w[\W\d]){3,}.*$"

combinaciones  = ["1m*2","3mm3","m32*"]
for combi in combinaciones:
    coincidencia = re.match(combi_completa, combi)
    if coincidencia:
        print(f"{combi} es válido.")
    else:
        print(f"{combi} NO es válido.")
