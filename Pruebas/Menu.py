def sucessiofibo(num):
        Fibonacci=[]
        cont=0
        a, b = 0, 1
        for i in range(num+1):
             a, b = b, b + a 
        if num in Fibonacci:
             print(f"{num} forma parte de la sucessio de Fibonacci")
        else:
           return  "No forma part"         
def multiplos(num):
    if num % 5 == 0 and num % 2 == 0:
        print (f"{num} es un múltiplo de 2 y de 5")
    elif num % 5 == 0:
        print( f"{num} es un múltiplo de 5")
    elif num % 2 == 0:
        print(f"{num} es un múltiplo de 2")
    else:
        print (f"{num} no es múltiplo de 2 ni de 5")
menu = ''' 1)  Comprovar si un nombre és múltiple de 5 o de 2
    2) Comprovar si un nombre forma part de la sèrie de Fibonacci.
    3) Comprovar si un nombre és senar
    4)Transformar una temperatura de graus Celsius en graus Fahrenheit 
    5) Sortir del programa
     '''

while True: 
    print(menu)
    num = int(input("Introduce un numero "))
    n = input("Elige una opción: ")

    match n:
        case "1":
            multiplos(num)
           
        case "2":
           sucessiofibo(num)     
        case "3":
            if num % 2 != 0:
                print(f"{num} es senar")
            else:
                print(f"{num} no es senar")
        case "4": 
            Fahrenheit= num*(9/5)+32
            print("La tempera en Fahrenheit es",Fahrenheit)
            
        case "5":
            print("Has selecionado salir del programa")
            break