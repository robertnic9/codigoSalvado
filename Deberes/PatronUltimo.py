n = int(input("Introduce un numero:  "))
palabra = str(input("Introduce una sola palabra:  "))
nCharPal = len(palabra)

NumIteraciones = 2 * n - 3
AnchoChar = 4 * n - 8 + nCharPal
memo= []
i = 1
while i <= NumIteraciones:
    NumRelleno = i + 1
    NumImpri = 1
    linAimpri = ""
    NumChrelleno = AnchoChar - (4*i)
    NumNoRellenos = AnchoChar - NumChrelleno
    FinNUMRellons = NumChrelleno + (NumNoRellenos/2)
    j=1
    
    if i > n-1:
        print(memo[NumIteraciones-i],end="")
    else:
        while j <= AnchoChar:
            if i == n-1 and j == (n-2)*2+1:
                if AnchoChar % 2 == 0:
                    linAimpri += palabra
                    j += nCharPal - 2
                else:
                    linAimpri += palabra + " "
                    j += nCharPal
            else:
                if j % 2 == 0:
                    if AnchoChar % 2 == 0 and j == AnchoChar/2:
                        linAimpri += "  "
                    else:   
                        linAimpri += " "
                else:
                    if j > FinNUMRellons:
                        NumImpri -= 1
                        linAimpri += str(NumImpri)
                    else:
                        linAimpri += str(NumImpri)
                        if NumImpri != NumRelleno:
                            NumImpri += 1            
            j += 1
    memo.append(linAimpri)
    print(linAimpri)
    
    i += 1
