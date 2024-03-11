palabra = "nombre"#str(input("Introduce una palbra de como maximo 15 caracteres: "))
simbolo = "#" #str(input("Introduce un simbolo: "))
'''
     e n o m b r e n
    r ############# o
   b ############### m
  m ################# b
 o ################### r
n #### n o m b r e #### e
'''

altura  = len(palabra)
ancho = altura*4 +1
palabra = list(palabra)
relleno = altura*2 +3
i = 1
print(palabra[-1])
numInv = 1
while i <= altura :
    linAimpr = ""
    spacios = altura-i
    numNorm = 1
    j = 1 
    while j <= ancho:
        if j <= spacios:
            linAimpr +=  " "
        elif j <= (relleno + spacios):
            if i == 1:
                if j == spacios+1:
                    linAimpr = palabra[-numInv] +" "
                    numInv += 1
                    j += 2
                    continue
                elif j == (relleno + spacios):
                    linAimpr = palabra[numInv] +" "
                    numInv += 1
                    j += 2
                    continue
                else:
                    linAimpr = palabra[numNorm] + " "
                    numNorm += 1
                    j+= 2
                    continue
            elif i == altura:
                if j == spacios:
                    linAimpr = palabra[-numInv] +" "
                    j += 2
                    continue
        else:
            linAimpr += " "
        j += 1
    relleno += 2
    i += 1
    print(linAimpr)

