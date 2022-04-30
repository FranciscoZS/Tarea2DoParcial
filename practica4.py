'''
Practica 4
Programa que permita ingresra una función y mediante el Método de Trapecios o Trapezoidal obtener la integral definida en el intervalo [a, b]
El programa también debe mostrar y guardar en un archivo de texto (.txt) la tabla con los siguientes valores: |i h Valor_Integral ε|
@utor: Francisco Zamora Saldaña
Programación avanzada 2MM3
'''

import math
from io import open#importamos las librerias

def numeroentero(t):
    while True:
        user = input(t)
        try:
            n= int(user)
        except:
            print("¡¡Debe ser numero entero!! \n")
        else:
            if n % 1 == 0 and n >0:
                break
            elif n == 0:
                print("el zero es la mitad de la recta no jala")
            else:
                print("¡¡Debe ser entero")
    return n

def numero(t):
    while True:
        user = input(t)
        try:
            n= float(user)
        except:
            print("¡¡Debe ser numero!! \n")
        else:
            break
    return n


trm=open("archivo de ejercicio numerico 4.txt","w")#para archivo de texto
def f(x):
    return math.cos(x)-pow(x,2)#variables

a = "Ingresa el interbalo a: "#se ingresan los intervalos
a=numero(a)

b = "Ingresa el intervalo b: " 
b=numero(b)

n = "Ingresa el numero del intervalo: "
n = numeroentero(n)

trm.write("n=%s\n"%n)
h = (b-a)/n#se inicia el metodo del trapezio
trm.write("h=%s\n"%h)
sum=0.0
for i in range(1,n):
    x=a+i*h
    sum=sum+f(x)
    

trap=h*(f(a)+2*sum+f(b))/2#formula
trm.write("trap=%s\n"%trap)
print("valor integral",trap)
trm.close()#cierre del .txt