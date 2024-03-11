def generar_patron(filas):
    for i in range(1, filas + 1):
        # Imprimir el número de la fila
        print(f"{i} #", end=" ")
        
        # Imprimir los símbolos de "#" con espacios según el patrón
        for j in range(1, i + 1):
            if j % 2 == 0:
                print("##", end=" ")
            else:
                print("#", end=" ")
        
        # Cambiar de línea para la siguiente fila
        print()

# Llamada a la función con el número de filas deseado (en este caso, 7)
generar_patron(7)
