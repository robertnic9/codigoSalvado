lista = [0,1, 2, 3, 4,9, 10, 11, 12, 13, 14]
ini = 0
fin = len(lista) - 1
i = 0

valor = int(input("Introduce un valor: "))

while ini <= fin:
    mitad = (ini + fin) // 2
    if valor == lista[mitad]:
        i = mitad
        print(f"El {valor} está en la posición {i}")
        break
    elif valor < lista[mitad]:
        fin = mitad - 1
    else:
        ini = mitad + 1
    i += 1

if ini > fin:
    print(f"El {valor} no está en la lista.")

