'''
Practica 1
Programa que permita ingresar una función f(x) cualquiera y mediante el Método de bisección obtener una de las raíces de la función, 
por lo que en primer lugar se debe mostrar al usuario una gráfica que permita inducir el intervalo de valores [a, b] 
que debe ingresarse. El programa también debe mostrar y guardar en un archivo de texto (.txt) la tabla con los siguientes valores: |i a b xi ε|, 
donde i es el número de iteración, a y b son los valores del intervalo, xi es el valor de la raíz calculado y ε el error. 
Finalmente se debe mostrar el valor de la raíz y la gráfica de la vecindad donde se localiza la raíz
@utor: Francisco Zamora Saldaña
Programación avanzada 2MM3
'''

import numpy as np
import matplotlib.pyplot as plt
import math
from io import open


cala=open("archivo de jercicio numerico 1del metodo de biseccion.txt","w")
def f(x):
    return math.cos(x)-pow(x,6)+pow(x,4)#ecuacion dada
def biseccion (a,b,errorr):#inicia el metodo de biseccion
    
    m1=a
    m=b
    k=0
    if (f(a)*f(b)>0):
        print("la funcion no tiene cambio de signo")
        
    while(abs(m1-m)>errorr):#empieza a correr el metodo
        m1=m
        m=(a+b)/2
        if (f(a)*f(m)<0):
            b=m
        if (f(m)*f(b)<0):
            a=m  
                
        print("el intervalo es [ ",a,",",b,"]")    
        k=k+1
        cala.write("ciclo=%s\n"%k)#para guardar los datos en el archivo .txt
        cala.write("m=%s\n"%m)
        cala.write("k=%s\n"%k)
        cala.write("a=%s\n"%a)
        cala.write("b=%s\n"%b)
        cala.write("errorr=%s\n"%errorr)
       
        
       
    x=np.linspace(0,m,k)  #sera de o hasta los valores de m con k elemnetos en el intervalo  
    plt.plot(x,".")
    plt.show()
        
        
    print("\n\n\nx",k,"=",m,"es una aproximacion optima")  
    
   
biseccion(0,5,10**(-3))#ponemos los valores optimos
cala.close() 
