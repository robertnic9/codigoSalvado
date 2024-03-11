import os 
import time

simbolo = "#"
remplazo = "x"
string1 = simbolo*20
string2 = simbolo + " "*18 + simbolo
j = 2

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
        time.sleep(0.1)
    else:
        if k != 19:
            rest = -1-k
        else:
            rest = -k
        string3 =  string1[:(rest)+19] + 'x' + string1[(-k+1)+19:]
        print(string1)
        print(string2)
        print(string2)
        print(string2)
        print(string3)
        time.sleep(0.5)
    k += 1    
