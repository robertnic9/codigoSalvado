import re 

salbruto =4000 #float(input("Introduce tu sueldo bruto: "))

if salbruto < 10000:
    impuesto = salbruto*0.04 
    print(f"El teu salari neto {salbruto-impuesto} i impuesto apagar {impuesto} eur")
elif salbruto < 20000:
    impuesto = 400 + (salbruto-10000)*0.11
    print(f"El teu salari neto {salbruto-impuesto} i impuesto apagar {impuesto} eur")
elif salbruto < 30000:
    impuesto = 400 + 1100 + (salbruto-20000)*0.27
    print(f"El teu salari neto {salbruto-impuesto} i impuesto apagar {impuesto} eur")
elif salbruto < 40000:
    impuesto = 400 + 1100 + 2700 + (salbruto-30000)*0.33
    print(f"El teu salari neto {salbruto-impuesto} i impuesto apagar {impuesto} eur")
else:
    impuesto = 400 + 1100 + 2700 + 3300 +(salbruto-40000)*0.47
    print(f"El teu salari neto {salbruto-impuesto} i impuesto apagar {impuesto} eur")

#This fuction is for calculating the IRPF of your anual salary ---> EJ2
def irpfcaculator(salbruto:float):
    ''' This fuction calculates the percentages of your ananual salary using conditionals
    and it gives you back using print the real salary and the taxes to pay '''

    if salbruto < 10000:
        impuesto = salbruto*0.04 
        print(f"El teu salari neto {salbruto-impuesto} i impuesto apagar {impuesto} eur")
    elif salbruto < 20000:
        impuesto = 400 + (salbruto-10000)*0.11
        print(f"El teu salari neto {salbruto-impuesto} i impuesto apagar {impuesto} eur")
    elif salbruto < 30000:
        impuesto = 400 + 1100 + (salbruto-20000)*0.27
        print(f"El teu salari neto {salbruto-impuesto} i impuesto apagar {impuesto} eur")
    elif salbruto < 40000:
        impuesto = 400 + 1100 + 2700 + (salbruto-30000)*0.33
        print(f"El teu salari neto {salbruto-impuesto} i impuesto apagar {impuesto} eur")
    else:
        impuesto = 400 + 1100 + 2700 + 3300 +(salbruto-40000)*0.47
        print(f"El teu salari neto {salbruto-impuesto} i impuesto apagar {impuesto} eur")

#This fuction calculates the IMC using first the mass in kg and the height in cm ---> Ej3
def imccalculator(kg:float, heightcm:int):
    ''' This fuction calculates the IMC using the mass in kg
    and the height in cm and returns you your IMC and the range
    if is healty or you have obesity'''

    imc = kg/((cm/100)**2)
    if imc < 18.5:
        return f"El teu IMC és de {imc} tens baix pes "
    elif imc < 25:
        return f"El teu IMC és de {imc} tens saludable "
    elif imc < 30:
        return f"El teu IMC és de {imc} tens Sobrepès  "
    elif imc < 35:
        return f"El teu IMC és de {imc} Obesitat de classe I o moderada "
    elif imc < 40:
        return f"El teu IMC és de {imc} tens Obesitat de classe II o severa "
    else:
        return f"El teu IMC és de {imc} Obesitat de classe III o mòrbida (molt severa) "
        
salbruto =4000 #float(input("Introduce tu sueldo bruto: "))

menu = '''  1 - Calcula el teu IRPF en funció dels teus ingressos
    2 - Comprova si estàs saludable en funció del teu pes i estatura
    3 - Sortir del programa.''' 
while True:
    print(menu) 
    opcio = int(input("Elige una opcion: "))
    match opcio:
        case  1:
            sal = float(input("Introduce tu salario: "))
            irpfcaculator(sal)
        case 2:
            pes = float(input("Introduce tu peso en kg: "))
            altura = int(input("Introuce tu altura en cm: "))
            print(imccalculator(pes,altura))
        case 3:
            print("Saliendo del programa")
            break

n = 5
for i in range(0,n*2-1):
    dimen= n*2
    if i < n:
        pat= str(n-i)
        for j in range(1,n):
            if i % 2 == 0:
                print(pat+(n-j-i)*"%",end=pat)
            else:
                print(pat, end="")
                print((n-j-i)*"*",end="")
        print()
    else:
        pat = str(i-n+2)
        for k in range(2,n+1):
            if i % 2 == 0:
                print(pat, end="")
                print((k)*"*",end="")
            else:
                print(pat, end="")
                print((k)*"%",end="")
        print()

#This fuction comprobates a string and gives you back another string with modifications 
def comprovastring(cadena:str) -> str:
    ''' 1) This fuction comprovates with a patrons and gives you true or false'''

    comp1 = re.compile(r"^\s(^[A-Z][\w])\s$")
    comp2 = re.compile(r"(?=.{0,15})(?=[\+\*\-\_\/\\@\$\&\%#\<\>\.\;\^]{2})")
    comp3 = re.compile(r"((^[\d]{9}[A-Za-z]{1}$)|(^[a-zA-Z]{1}[\d]{9}[a-zA-Z]{1}$))")

    