 
import timeit 
'''  
* * * * * * * * * * * * * * * * * * * * * * *
* 2 3 4 5 6 5 4 3 2 *   * 2 3 4 5 6 5 4 3 2 *
  * 2 3 4 5 4 3 2 *       * 2 3 4 5 4 3 2 *
    * 2 3 4 3 2 *           * 2 3 4 3 2 *
      * 2 3 2 *               * 2 3 2 *
        * 2 *                   * 2 *
          *                       *
          *                       *
        * 2 *                   * 2 *
      * 2 3 4 *               * 2 3 2 *
    * 2 3 4 3 2 *           * 2 3 4 3 2 *
  * 2 3 4 5 4 3 2 *       * 2 3 4 5 4 3 2 *
* 2 3 4 5 6 5 4 3 2 *   * 2 3 4 5 6 5 4 3 2 *
* * * * * * * * * * * * * * * * * * * * * * * 
             '''

'''
* * * * * * * * * * * * * * * * * * *
* 2 3 4 5 4 3 2 *   * 2 3 4 5 4 3 2 *
  * 2 3 4 3 2 *   I   * 2 3 4 3 2 *
    * 2 3 2 *     P     * 2 3 2 *
      * 2 *       O       * 2 *
        *         T         *
        *         A         *
      * 2 *       M       * 2 *
    * 2 3 2 *     O     * 2 3 2 *
  * 2 3 4 3 2 *   J   * 2 3 4 3 2 *
* 2 3 4 5 4 3 2 *   * 2 3 4 5 4 3 2 *
* * * * * * * * * * * * * * * * * * * 

* * * * * * *
* 2 *   * 2 *
  *       *
  *       *
* 2 *   * 2 *
* * * * * * *

* * * * * * * * * * *
* 2 3 2 *   * 2 3 2 *
  * 2 *       * 2 * 
    *           *


'''
''' '''
# El ancho del patron es ((n*4)+1)*2+3
# El centro del patron es (n*4)+3 alli es donde se imprime la palabra en vertical
# La altura (n+2)*2 si la palbra es mas pequeña que el spacio vacio
# EL SPACIO vacio donde se puede escribir el texto es de (n+1)*2 = 2n+2
# Si la palbra es mas grande que la altura de vacios  se pueden añadir mas caracteres especiales en el centro 
# si la longitud de la palabra es impar el centro siempre tendra 3 carct esp como minimo 
# si es par siempre tendra 2 caract esp
# La palabra como maximo podra comenzar en i = 3, 
# El numero del centro de la base de las piramides es n+1
# Es decir que si es n= 1 se imprime * 2 * 
# si n es mayor se imprime una escalera en este (n= 3) * 2 3 2 * 
#  desde i = 2, se comienza a sustituir los numeros y caracteres por espacios Dando lugar a la forma triangular
# se sustituyen dos caracteres por espacios por cada nivel 
# Al llegar al centro la piramide se invierte aumentado en dos caracteres por piramide 
# Ya que la figura es simetrica menos en el centro se puede almacenar la linia a imprimir 
# y utilizarla en las dos siguientes piramides

# EXTRA : Poder hacer una animacion cambiando el exterior "*" por otros caracteres especiales creando una animacion
#Que en total  dure 10 s hasta que se haga un break 

i = 1
palabra = "pinoho"
n = 9
n = n +1 
ancho = n * 2 - 1

if len(palabra) % 2 == 0:
    altura = n * 2 + 2
else:
    altura = n * 2 + 3

letras = list(palabra)

simbolo = "# "
spacio = 1
patron = []
vacio = "  "*n
NumDePAt = 1
while i <= altura:
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
                    elif j < (n-i+1) + spacio:
                        linAImpr += str(NumIMPR) + " "
                        NumIMPR += 1
                    else:
                        linAImpr += str(NumIMPR) + " "
                        NumIMPR -= 1
                else: 
                    linAImpr += "  "
                j += 1
            spacio += 1
            patron.append(linAImpr)
        else:
            if i <= (altura - n):
                linAImpr += "  "*(spacio-1) + simbolo + "  "*(spacio-1)
    
    if i == 1 or i == altura:
        print(vacio + linAImpr +simbolo+linAImpr)
    else:
        if i <= (altura - n):
            print(vacio + linAImpr + "  " + linAImpr)
        else: 
            print(vacio + patron[-NumDePAt] + "  " + patron[-NumDePAt])
            NumDePAt += 1
    
    i += 1
    
