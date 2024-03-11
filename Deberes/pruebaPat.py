import os
import time

duracion_deseada = 10
tiempo_inicial = time.time()

n = int(input("Introduce un numero del 1-9:  "))
palabra = str(input("Introduce una sola palbra:  "))


ancho = n * 2 - 1

if len(palabra) % 2 == 0:
    altura = n * 2 + 2
else:
    altura = n * 2 + 3

letras = list(palabra)

vacio = "  "*n
cont = 0
i = 1
NumFinal = n

if n > 5: 
    NumALlegar = round(n**0.5)
else:
    NumALlegar = n * 2

reverso = False

while (time.time() - tiempo_inicial) < duracion_deseada:
    simbolos = ["* ","# ","$ ","Є ","& "]
    spacio = 1
    patron = []
    NumDePAt = 1
    os.system('cls' if os.name == 'nt' else 'clear')
    i = 1  
    if len(palabra) % 2 == 0:
        altura = n * 2 + 2
    else:
        altura = n * 2 + 3
    letras = list(palabra)
    while i <= altura:
        j = 1
        linAImpr = ""
        NumIMPR = 1
        ancho = (2 * n - 1)
        if i == 1 or i == altura:
            linAImpr += simbolos[cont] * ancho
        else:
            if i <= n:
                while j <= ancho:
                    relleno = (n + 2 - i) * 2 - 1
                    if j < spacio:
                        linAImpr += "  "
                    elif j < spacio + relleno:
                        if NumIMPR == 1:
                            linAImpr += simbolos[cont]
                            NumIMPR += 1
                        elif j < (n-i+1) + spacio:
                            linAImpr += str(NumIMPR) + " "
                            NumIMPR += 1
                        else:
                            linAImpr += str(NumIMPR) + " "
                            NumIMPR -= 1
                    else: 
                        linAImpr += "  "
                    j += 1
                spacio += 1
                patron.append(linAImpr)
            else:
                if i <= (altura - n):
                    linAImpr += "  "*(spacio-1) + simbolos[cont] + "  "*(spacio-1)
        
        if i == 1 or i == altura:
            print(vacio + linAImpr + simbolos[cont] + linAImpr)
        else:
            if i <= (altura - n):
                print(vacio + linAImpr + "  " + linAImpr)
            else: 
                print(vacio + patron[-NumDePAt] + "  " + patron[-NumDePAt])
                NumDePAt += 1
        
        i += 1
    time.sleep(0.15)
    if reverso == True:
        if n != NumFinal: 
            n += 1
        else: 
            print( vacio + "Se ha acabado la animacion")
    else:
        if n == NumALlegar:
            if cont != 4:
                cont += 1
            else:
                reverso = True
        else:
            n -= 1


    CalcSigAncho = ancho - ((2 * (n-1) - 1))
    
    