import copy

def merge_sort_rec(listaValor:list):
    #This fuction is for shorting 
    listaValor = copy.deepcopy(listaValor)
    if len(listaValor) > 1:
        
        mitad = len(listaValor)//2
        mitIzq = listaValor[:mitad]
        mitDer = listaValor[mitad:]
        mitIzq = merge_sort_rec(mitIzq)
        mitDer = merge_sort_rec(mitDer)

        
        i = 0
        d = 0
        x = 0
        while i < len(mitIzq) and d < len(mitDer):
            if mitIzq[i] < mitDer[d]:
                listaValor[x] = mitIzq[i]
                i += 1
            else:
                listaValor[x] = mitDer[d]
                d += 1
            x += 1

        while i < len(mitIzq):
            listaValor[x] = mitIzq[i]
            i += 1
            x += 1
        while d < len(mitDer):
            listaValor[x] = mitDer[d]
            d += 1
            x += 1
    return listaValor

def fact_rec(num:int):
    #This fuction is for calculating the factorial number with recursion
    if num <= 1:
         return num
    else:
        return num*fact_rec(num-1)

def fib_rec(num):
    #This fuction calculates the Fibonacci Numbers with recursion
    if n <= 1:
        return
    else:
        return fib_rec(n-1)+ fib_rec(n-2)

def sum_rec(lista):
    #This fuction is for adding all numbers in a list with recursion
    if not lista:
        return 0 
    else:
        return lista[0] + sum_rec[(lista[1:])]

def bus_binaria_rec(lista:list, valor:int, ini=0, fin= None):
    #This fuction is for the Binari Search in a List using recursion 
    if fin is None:
        fin= len(lista)-1
    if ini > fin:
        return f"El {valor} no está en la lista."
    mitad= (ini+fin)//2 
    if valor == lista[mitad]:
        pos = mitad
        return f"El {valor } encontrado en la posicion {mitad} "
    elif valor < lista[mitad]:
        return bus_binaria_rec(lista, valor, ini, mitad-1)
    else:
        return bus_binaria_rec(lista, valor, mitad+1, fin )

def inv_cad_rec(cadena:str, ini=0):
    # This function is for reversing a character string with recursion
    if len(cadena) <= 1: 
        return cadena
    else:
       return cadena[-1]+ inv_cad_rec(cadena[1:-1])+ cadena[0]

def alg_euclides_rec(num1:int, num2:int):
        if num2 == 0: 
            return num1
        else:
            return alg_euclides_rec(num2, num1 % num2)

def torres_hanoi(num, origen="1", auxiliar="2", final="3"):
    if num == 1:
        print(f"Se mueve de {origen} a {final} la pieza {num} ")
    else:
        torres_hanoi(num-1,origen,auxiliar,final)

        print(f"Se mueve de {origen} a {auxiliar} la pieza {num}")

        torres_hanoi(num-1,auxiliar,final,origen)

def sum_dig_nom(num, posicion=0):
    num=str(num)

    if  posicion == len(num):
        return 0
    else:
        return  int(num[posicion]) + sum_dig_nom(num,posicion+1)
    
def comp_digit_rec(num):
    num=str(num)
    if len(num) == 1:
        return 1
    else:
        return 1+comp_digit_rec(num[1:])

def pot_num_rec(x,n):
    if n < 1:
        return 1
    else:
        return x * pot_num_rec(x, n-1)

def com_palindrom(palb:str):
    if  palb == inv_cad_rec(palb):
        return f"{palb} es un palindrom"
    else:
        return f"{palb} no es un palindrom"

def pri_mult(n, x):
    if n ==0:
        return n
    else:
        print(x*n)
        return pri_mult(n-1,x) 

