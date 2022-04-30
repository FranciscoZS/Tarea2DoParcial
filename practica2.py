'''
Practica 2
Programa que permita ingresar una función f(x) cualquiera y mediante el Método de Newton-Raphson obtener una de las raíces de la función, 
por lo que en primer lugar se debe mostrar al usuario una gráfica que permita inducir el valor incial x0 que debe ingresarse. 
El programa también debe mostrar y guardar en un archivo de texto (.txt) la tabla con los siguientes valores: |i xi ε|, 
donde i es el número de iteración, xi es el valor de la raíz calculado y ε el error. 
Finalmente se debe mostrar el valor de la raíz y la gráfica de la vecindad donde se localiza la raíz
@utor: Francisco Zamora Saldaña
Programación avanzada 2MM3
'''

import numpy as np#importamos librerias
import matplotlib.pyplot as plt
import math #se abrira primero el .txt con el open

NRMet=open("archivo de ejercicio numerico 2 de Newton R.txt","w")

def f(x):#ecuacion dada
    return math.cos(x)-pow(x,3)

def df(x):#su derivada de la ecuaciom
    return -(math.sin(x))-3*pow(x,2)

def nr(x0,errorr,n):
    
    for k in range(n):
        x1=x0-f(x0)/df(x0)
        if(abs(x1-x0)<errorr):
            x=np.linspace(0,x1,k)
            plt.plot(x,".")
            plt.show()
        
            print("x",k+1,"=",x1,end=" ")
            print("Es una buena aproximacion de la raiz")
            return
        x0=x1
        print("x",k+1,"=",x1)
        NRMet.write("ciclo=%s\n"%k)#datos para el .txt
        NRMet.write("x0=%s\n"%x0)
        NRMet.write("k=%s\n"%k)
        NRMet.write("errorr=%s\n"%errorr)  
       
nr(3,0.0000001,10) #graficacion   
NRMet.close()   #cerrar .txt 