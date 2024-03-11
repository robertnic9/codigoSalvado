def busqueda_dicotomica_recursiva(lista, elemento, inicio=0, fin=None):
    if fin is None:
        fin = len(lista) - 1

    if inicio > fin:
        return -1  # Elemento no encontrado

    medio = (inicio + fin) // 2

    if lista[medio] == elemento:
        return medio  # Elemento encontrado en la posición 'medio'
    elif lista[medio] < elemento:
        return busqueda_dicotomica_recursiva(lista, elemento, medio + 1, fin)
    else:
        return busqueda_dicotomica_recursiva(lista, elemento, inicio, medio - 1)

# Ejemplo de uso
mi_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
elemento_buscado = 10

resultado = busqueda_dicotomica_recursiva(mi_lista, elemento_buscado)

if resultado != -1:
    print(f"El elemento {elemento_buscado} se encuentra en la posición {resultado}.")
else:
    print(f"El elemento {elemento_buscado} no está en la lista.")
