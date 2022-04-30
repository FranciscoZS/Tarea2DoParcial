'''
Practica 6
Resolver el problema de que se impriman los N números de la Serie de Padovan , 
donde N es un número entero positivo que el usuario debe ingresar para obtener los valores de la serie, 
utilizando el paradigma de Programación Funcional (no debe utilizarse ningún otro paradigma)
@utor: Francisco Zamora Saldaña
Programación avanzada 2MM3
'''

def numeroentero(t):
    while True:
        user = input(t)
        try:
            n= int(user)
        except:
            print("¡¡Debe ser numero entero y positivo!! \n")
        else:
            if n % 1 == 0 and n >0:
                break
            elif n == 0:
                print("el zero es la mitad de la recta no jala")
            else:
                print("¡¡Debe ser entero y positivo!! \n")
    return n

padovans = "Ingrese hasta que numero quiere la serie de Padovan:"
padovans = numeroentero(padovans)

def pad(n): 
  
    # para esta serie la posicion 0,1,2 son 1 en la serie, de ahi los valores iniciales
    PrevPrev, Prev, act, sig = 1, 1, 1, 1
  #previo,previo del previo,siguiente,el actual
     
    # se escribe la formula 
    for i in range(3, n+1): 
        sig = PrevPrev + Prev 
        PrevPrev = Prev 
        Prev = act
        act = sig 
  
    return (sig)
for x in range (padovans):
 print(pad(x))
 