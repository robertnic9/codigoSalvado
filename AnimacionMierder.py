#Cambio 
import os 
import time

simbolo = str(input("Introudce un caracter: "))
remplazo = str(input("Introudce un caracter desplazamiento: "))
string1 = simbolo*20
string2 = simbolo + " "*18 + simbolo
j = 1
while j <= 9:
    os.system('cls' if os.name == 'nt' else 'clear')
    if j == 1 or j == 5:
        k=0
        while k <= 19:
            os.system('cls' if os.name == 'nt' else 'clear')
            if j == 1:
                string3 =  string1[:k] + remplazo + string1[1+k:]
                print(string3)
                print(string2)
                print(string2)
                print(string2)
                print(string1)
                time.sleep(0.25)
            else:
                if k != 19:
                    rest = -1-k
                else:
                    rest = -k
                string3 =  string1[:(rest)+19] + remplazo + string1[(-k)+19:]
                print(string1)
                print(string2)
                print(string2)
                print(string2)
                print(string3)
                time.sleep(0.25)
            k += 1
    elif j == 9:
        string3 = remplazo + simbolo*19
        print(string3)
        print(string2)
        print(string2)
        print(string2)
        print(string1)
    else:
        print(string1)
        if j == 2 or j == 8:
            if j == 2:
                string3 = simbolo + " "*18 + remplazo
            else:
                string3 = remplazo + " "*18 + simbolo
            print(string3)
            print(string2)
            print(string2)
        elif j == 3 or j == 7:
            if j == 3:
                string3 = simbolo + " "*18 + remplazo
            else:
                string3 = remplazo + " "*18 + simbolo
            print(string2)
            print(string3)
            print(string2)
        elif j == 4 or j == 6:
            if j == 4:
                string3 = simbolo + " "*18 + remplazo
            else:
                string3 = remplazo + " "*18 + simbolo
            print(string2)
            print(string2)
            print(string3)    
        print(string1)
        time.sleep(0.25)
    j += 1