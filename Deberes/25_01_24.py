import re
'''
dni = input("Introduce tu DNI: ")
dni = dni.upper()  

if re.match(r"\d{8}[A-HJ-NP-Z]", dni):
    num = list(dni[:-1])  
    letra_usuario = dni[-1]

    residuo = num % 23
    print(residuo)
    letras_dni = "TRWAGMYFPDXBNJZSQVHLCKE"
    letra_calculada = letras_dni[residuo]
    print(letra_calculada)

    if letra_calculada == letra_usuario:
        print("DNI válido.")
    else:
        print("DNI inválido. La letra no coincide.")
else:
    print("Formato de DNI incorrecto.")

dni = input("Introduce tu DNI: ")
dni = dni.upper()  

if re.match(r"\d{8}[A-HJ-NP-Z]", dni):
    num = list(dni[:-1])  
    letra_usuario = dni[-1]

    residuo = sum(int(numero) for numero in num)
    residuo = residuo % 23
    print(residuo)
    letras_dni = "TRWAGMYFPDXBNJZSQVHLCKE"
    letra_calculada = letras_dni[residuo]
    print(letra_calculada)

    if letra_calculada == letra_usuario:
        print("DNI válido.")
    else:
        print("DNI inválido. La letra no coincide.")
else:
    print("Formato de DNI incorrecto.")

nie = input("Introduce tu NIE: ")
nie = nie.upper()


if re.match(r"[XYZ]\d{7}[A-HJ-NP-Z]", nie):
    letra_usuario = nie[-1]
    num = int(nie[1:-1])  
    residuo = num % 23
    letras_nie = "TRWAGMYFPDXBNJZSQVHLCKE"
    letra_calculada = letras_nie[residuo]

    if letra_calculada == letra_usuario:
        print("NIE válido.")
    else:
        print("NIE inválido. La letra no coincide.")
else:
    print("Formato de NIE incorrecto.")

'''
'''
Particulares (Nueva)	1234 ABC	Cuatro números seguidos por tres letras.
Particulares (Antigua)	M-1234-AB	Prefijo con la letra de la provincia y guiones.
Motocicletas	M-1234-AB	Similar al formato antiguo para automóviles.
Diplomáticas	CD-1234-AB	Prefijo con las letras "CD" seguido por el formato común o CC vehículos del Cuerpo Consular.
Vehículos Especiales	E-1234-AB	Prefijo con la letra "E" seguido por el formato común.
------
Matricula provisionales letra P seguida de numeros y tres letras
Taxis, VTC Y matrículas de vehículos históricos, formadas por la letra H, un número de cuatro cifras y tres letras
Al ejército, puedes ver las siglas ET (Ejército de Tierra); EA (Ejército de Aire); y FN (Fuerzas Navales)
Vehículos de la Guardia Civil encontrarás las siglas PGC (Parque Guardia Civil) 
y para los de la Policía Nacional verás las letras CNP (Cuerpo Nacional de Policía)
Técnicos Administrativos TA
Organismos Internacionales OI
Organismos como la Ertzaintza con una E
Policía Canaria, con las siglas CGPC (Cuerpo General de la Policía Canaria)

---------- Despues de las letras 4 numeros y una letra extra 
'''

prefijos_provincias = {
    'A-': 'Alava',
    'AB': 'Albacete',
    'AL': 'Almeria',
    'AV': 'Avila',
    'B-': 'Barcelona',
    'BA': 'Badajoz',
    'BI': 'Vizcaya',
    'BU': 'Burgos',
    'C-': 'A Coruña',
    'CA': 'Cadiz',
    'CC': 'Caceres',
    'CE': 'Ceuta',
    'CO': 'Cordoba',
    'CR': 'Ciudad Real',
    'CS': 'Castellon',
    'CU': 'Cuenca',
    'GC': 'Las Palmas (Gran Canaria)',
    'GI': 'Girona',
    'GR': 'Granada',
    'GU': 'Guadalajara',
    'H': 'Huelva',
    'HU': 'Huesca',
    'IB': 'Illes Balears',
    'J': 'Jaen',
    'L': 'Lleida',
    'LE': 'Leon',
    'LO': 'La Rioja',
    'LU': 'Lugo',
    'M': 'Madrid',
    'MA': 'Malaga',
    'MU': 'Murcia',
    'NA': 'Navarra',
    'O': 'Asturias',
    'OR': 'Ourense',
    'P': 'Palencia',
    'PM': 'Illes Balears (Palma de Mallorca)',
    'PO': 'Pontevedra',
    'S': 'Cantabria',
    'SA': 'Salamanca',
    'SE': 'Sevilla',
    'SG': 'Segovia',
    'SO': 'Soria',
    'SS': 'Gipuzkoa',
    'T': 'Tarragona',
    'TE': 'Teruel',
    'TF': 'Santa Cruz de Tenerife',
    'TO': 'Toledo',
    'V': 'Valencia',
    'VA': 'Valladolid',
    'BI': 'Vizcaya',
    'ZA': 'Zamora',
    'Z': 'Zaragoza',
    'CE': 'Ceuta',
    'ML': 'Melilla'
}
formatos_matriculas = {
    'Nuevas': re.compile(r"[\s*-]\d{4}[\s*-][A-HJ-NP-Z]{3}"),
    'Vehiculos Antiguos': re.compile(r"^\s*[A-Z]{1,2}[\s*-]\d{4}[\s*-][A-HJ-NP-Z]{2}\s*$"),
    'Motocicletas': re.compile(r'^\s*[A-Z]{1,2}-\d{4}-[A-HJ-NP-Z]{2}\s*$'),
    'Diplomáticas': re.compile(r'^\s*CD-\d{4}-[A-HJ-NP-Z]{2}\s*$'),
    'Vehículos Especiales': re.compile(r'^\s*E-\d{4}-[A-HJ-NP-Z]{2}\s*$'),
    'Matrículas provisionales': re.compile(r'^\s*P\d{3}[A-HJ-NP-Z]{3}\s*$'),
    'Taxis, VTC y matrículas históricas': re.compile(r'^\s*H\d{4}[A-HJ-NP-Z]{3}\s*$'),
    'Ejército': re.compile(r'^\s*(ET|EA|FN)\d{4}[A-HJ-NP-Z]{2}\s*$'),
    'Guardia Civil': re.compile(r'^\s*PGC\d{4}[A-HJ-NP-Z]{2}\s*$'),
    'Policía Nacional': re.compile(r'^\s*CNP\d{4}[A-HJ-NP-Z]{2}\s*$'),
    'Técnicos Administrativos': re.compile(r'^\s*TA\d{4}[A-HJ-NP-Z]{2}\s*$'),
    'Organismos Internacionales': re.compile(r'^\s*OI\d{4}[A-HJ-NP-Z]{2}\s*$'),
    'Ertzaintza': re.compile(r'^\s*E\d{4}[A-HJ-NP-Z]{2}\s*$'),
    'Policía Canaria': re.compile(r'^\s*CGPC\d{4}[A-HJ-NP-Z]{2}\s*$'), 
}
matricula_ejemplo = input("Introduce tu matricula para verificarla: ")
matricula_ejemplo.upper()
for tipo, patron in formatos_matriculas.items():
    if patron.match(matricula_ejemplo):
        if tipo == 'Motocicletas'or tipo == 'Vehiculos Antiguos':
            matriculasinspacio =  re.sub(r'\s', '', matricula_ejemplo)
            for provincia, LetraProv in prefijos_provincias.items():
                if LetraProv == matriculasinspacio[:2]:
                    print(f'La matricula {matriculasinspacio} es valida de {tipo} proviene de la pronvincia {provincia}')
                    break
                else:
                     print(f'La matricula {matriculasinspacio} es falsa')
                     break
        else:
            print(f'La matrícula "{matricula_ejemplo}" es valida es de tipo: {tipo}')
            break
else:
    print(f'La matrícula "{matricula_ejemplo}" es invalida')
    
'''
Código del país (2 caracteres):Utiliza la norma ISO 3166-1 alfa-2, que son dos letras representando el país.

Dígitos de control (2 caracteres):  verifican la validez del IBAN y se generan mediante un algoritmo específico.

Número de cuenta (variable): Este componente puede incluir tanto dígitos numéricos como letras. Su longitud y formato varían según el país y la entidad bancaria.
### Cálculo del IBAN:

1. **Convertir el número de cuenta a un formato estándar:** Eliminar espacios y guiones, y colocar los dígitos numéricos al principio de la cadena.

2. **Agregar el código del país y dígitos de control:** Agregar al inicio el código del país y los dígitos de control, que se obtienen a partir de un algoritmo específico.

DIGITOS  CONTROL-->

Eliminar caracteres no numéricos:

Quita los espacios y letras del IBAN, dejando solo los dígitos numéricos: 0012345678901234567890
Mover los primeros cuatro dígitos al final:

Toma los cuatro primeros dígitos y colócalos al final del número: 56789012345678900012
Asignar valores a las letras:

Si hay letras en el IBAN, asigna a cada letra su posición en el alfabeto
(A=10,B=11,C=12,D=13,E=14,F=15,G=16,H=17,I=18,J=19,K=20,L=21,M=22,N=23,O=24,P=25,Q=26,R=27,S=28,T=29,U=30,V=31,W=32,X=33,Y=34,Z=35)

Si solo hay números, continúa con el siguiente paso.
Concatenar y añadir ceros:

Añade dos ceros al final del número: 5678901234567890001200
Dividir y obtener el módulo:

Divide el número resultante por 97 y toma el residuo (módulo): 
5678901234567890001200

5678901234567890001200 % 97 = 1.
Restar el módulo a 98:

Resta el módulo obtenido a 98: 
98−1=97

97 es el numero de control 

3. **Dividir la cadena en bloques de 4 caracteres:** Dividir la cadena resultante en bloques de 4 caracteres, añadiendo ceros si es necesario.

4. **Calcular los dígitos de control finales:** Aplicar un algoritmo de cálculo específico para obtener los dígitos de control finales.

'''

