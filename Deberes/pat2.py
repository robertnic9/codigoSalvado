import os
import time

# Configuración de la tasa de fotogramas por segundo (FPS)
fps = 24

# Configurar la duración deseada del bucle en segundos
duracion_deseada = 7

# Calcular la duración de cada fotograma
frame_duration = 1 / fps

# Obtener el tiempo actual
tiempo_inicial = time.time()

# Definir el patrón de líneas (este es solo un ejemplo, ajusta según tus necesidades)
palabra = "pinocho"
n = 5
ancho = n * 2 - 1

if len(palabra) % 2 == 0:
    altura = n * 2 + 2
else:
    altura = n * 2 + 3

simbolo = "# "
spacio = 1
i = 1

# Iniciar el bucle
while (time.time() - tiempo_inicial) < duracion_deseada:
    os.system('cls' if os.name == 'nt' else 'clear')  # Limpiar la pantalla en cada fotograma

    j = 1
    linAImpr = ""
    NumIMPR = 1
    if i == 1 or i == altura:
        linAImpr += simbolo * (2 * n - 1)
    else:
        if i <= n:
            while j <= ancho:
                relleno = (n + 2 - i) * 2 - 1
                if j < spacio:
                    linAImpr += "  "
                elif j < spacio + relleno:
                    if NumIMPR == 1:
                        linAImpr += simbolo
                        NumIMPR += 1
                    elif j < (n - i + 1) + spacio:
                        linAImpr += str(NumIMPR) + " "
                        NumIMPR += 1
                    else:
                        linAImpr += str(NumIMPR) + " "
                        NumIMPR -= 1
                else:
                    linAImpr += "  "
                j += 1
            spacio += 1
        else:
            if i <= n + 2:
                linAImpr += "  " * (spacio - 1) + simbolo + "  " * (spacio - 1)

    if i == 1 or i == altura:
        print(linAImpr + simbolo + linAImpr)
    else:
        print(linAImpr + "  " + linAImpr)

    i += 1

    # Pausar para mantener la tasa de fotogramas
    time.sleep(frame_duration)

print("El bucle ha terminado después de aproximadamente 7 segundos.")
