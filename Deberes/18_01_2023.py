import re 
'''' 
Para mañana buscar un patron curioso 

Formato de todo tipo de telefono
Incluyendo las extensiones del pais 

+88 888 88 88
555 55 55 55
0055 555 55 55 (Los espacios pueden ser guiones "-")

Contraseñas 
de 0 a 16 caracteres (incluidos)
2 caracteres especiales no consecutivos 2 como minimo 
2 caracteres numericos no ocnsecutivos 2 como minimo
'''

telefonos = ["+88 888 88 88", "555 55 55-55", "0055 555 55 55", "0055-555-55-55", "Patata"]

pat_telf = r"((\+|00)\d{2})?[\s\-]\d{3}[\s\-]\d{2}[\s\-]\d{2}"

for numero in telefonos:
    coincidencia = re.match(pat_telf, numero)
    if coincidencia:
        print(f"{numero} es un número de teléfono válido.")
    else:
        print(f"{numero} NO es un número de teléfono válido.")
print ()

contraseñas = ["AbA$mec*12", "AB**mecbistec","jakdijisjn53kdk17"]
ver_contra = r"((?=.{8,16})(?=(A-z.){2,})(?=^\w.{2,}))"

for contra in contraseñas:
    coincidencia = re.match(ver_contra, contra)
    if coincidencia:
        print(f"{contra} es una contraseña válida.")
    else:
        print(f"{contra} NO es una contraseña válida.")
print()

ver_email = r"[\d\w\.-_]+@[\d\w.]+\.[\d\w]+"

emails = ["pepito@@gmail.com", "pepito123@gmail.com","pepito123@usario.gmail.com"]
for email in emails:
    coincidencia = re.match(ver_email, email)
    if coincidencia:
        print(f"{email} es un email válido.")
    else:
        print(f"{email} NO es un email válido.")
