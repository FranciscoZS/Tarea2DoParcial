'''
Practica 5
Programa que permita realizar la simulación del Camino o Paseo Aleatorio (Random Walk) o caminata del borracho (su profesor de programación) 
solicitando cuántos pasos (n) se efectuarán y de que longitud (L(), mostrando al finalizar la gráfica en 2D tras efectuar los n pasos
@utor: Francisco Zamora Saldaña
Programación avanzada 2MM3
'''

#importamos las librerias
import numpy as np
import pylab
import random
  
def numeroenteropositivo(t):
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
                print("¡¡Debe ser entero y positivo!!")
    return n


# como requisito necesitamos definir el numero de pasos
n = "Ingrese el numero de pasos que usted dese que haga: "
n=numeroenteropositivo(n)


#se crean dos matrices para contener las coordenadas x y y
#de tamaño es igual al número de tamaño y se completa con ceros
x = np.zeros(n)
y = np.zeros(n)
  



# aqui se llenan las coordenadas con variables aleatorias
for i in range(1, n):
    val = random.randint(1, 4)#inicio de varibles aleatorias
    if val == 1:
        x[i] = x[i - 1] + 1
        y[i] = y[i - 1]
    elif val == 2:
        x[i] = x[i - 1] - 1
        y[i] = y[i - 1]
    elif val == 3:
        x[i] = x[i - 1]
        y[i] = y[i - 1] + 1
    else:
        x[i] = x[i - 1]
        y[i] = y[i - 1] - 1
      
  


# para graficar , usamos numpy y pylab
pylab.title("paseo aleatorio ($n = " + str(n) + "$ pasos)")
pylab.plot(x, y)#graficacion
pylab.savefig("paseo_aleatorio"+str(n)+".png",bbox_inches="tight",dpi=600)
pylab.show()