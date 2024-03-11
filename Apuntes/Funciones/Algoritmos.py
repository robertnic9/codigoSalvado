import copy
def merge_sort_rec(listaValor:list):
    listaValor = copy.deepcopy(listaValor)
    if len(listaValor) > 1:
        #Separa la listaValor
        mitad = len(listaValor)//2
        mitIzq = listaValor[:mitad]
        mitDer = listaValor[mitad:]
        mitIzq = merge_sort_rec(mitIzq)
        mitDer = merge_sort_rec(mitDer)

        #Se atribuyen valores a las variables 'i, d y x'
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



lista2= [38,27,43,3,9,82,10]
print(merge_sort_rec(lista2))
print(lista2)