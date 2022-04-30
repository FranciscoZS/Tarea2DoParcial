'''
Practica 14
Programa que permita obtener diversas soluciones de el problema de las 8 reinas. 
El programa debe permitirle al usuario seleccionar la posición inicial de una de las reinas y de ahí mostrarle la(s) posible(s) solución(es)
@utor: Francisco Zamora Saldaña
Programación avanzada 2MM3
'''

pivote=True
while pivote:
 try:
     pass 
     print("¿Qué posicion inicial quieres dar? primero la fila y despues la columna")
     pos_x = int(input("Ingrese la cordenada de la fila: "))
     pos_y = int(input("Ingrese la cordenada de la columna: "))
     if -1<pos_y<8 and -1<pos_x<8:#condiciones para el tablero
         pivote=False
          
 except Exception:#se repite hasta que sea un tbalero optimo
     pass
     print("Ingresa un numero entero y positivo: ")  
print()

import random
random.choice([1,2,3])
def disponibles(y,n):
    columnas_disponibles = []
    for x in range(n):
        if pos_x!=x and pos_y!=y:
            if(columna[x] or diagonal_izquierda[x+y] or diagonal_derecha[x-y+n-1]): 
                #Aqui se usa la condicion cuando la reina es atacada 
                #si es asi debe iniciar de nuevo
                continue
            columnas_disponibles.append(x)
    return columnas_disponibles



if([]):
    print("y")
else:
    print("n")
    

n = 8
solucion = []

import numpy as np
tablero=np.zeros([8,8])

columna = [False]*n
diagonal_izquierda = [False]*(n*2)
diagonal_derecha = [False]*(n*2)

while(len(solucion)!=n and n>3):
#para un rango de(10):
    solucion = [(pos_x,pos_y)]
    columna = [False]*n
    diagonal_izquierda = [False]*(n*2)
    diagonal_derecha = [False]*(n*2)
    
    for y in range(n):
        if pos_y!=y:
            #se coloca a la reina en una columna aleatoria
            columnas_d = disponibles(y,n)
            #condicion que se cumple si solo hay columnas no atacadas
            if(columnas_d):
                x = random.choice(columnas_d)
            else:
                break
            
            columna[x] = diagonal_izquierda[x+y] = diagonal_derecha[x-y+n-1] = True
            solucion.append((x,y))
        
print("La solucion es:\n\n",solucion,"\n")

for i in range(len(solucion)):
    ejes=solucion[i]
    tablero[ejes[0],ejes[1]]=1
print("Las posiciones finales son:\n\n\n",tablero)