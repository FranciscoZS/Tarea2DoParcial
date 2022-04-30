'''
Practica 18
Realizar la simulación y animación de un péndulo simple, pidiendo al usuario los siguientes datos: Masa del péndulo, 
aceleración de la gravedad, Longitud del péndulo, constante de fricción viscosa. Usar algo como lo que se muestra en esta página del Modelado y 
simulación del péndulo simple
@utor: Francisco Zamora Saldaña
Programación avanzada 2MM3
'''

pivote=True#hacemos un while hasta que se cumplan las condiciones de m,l,g,c_f_v
while pivote:
 try:
     pass 
     
     masa= int(input("Ingresa la masa del pendulo: "))
     
     gravedad=float(input("Ingresa la aceleracion de la gravedad: "))
     
     longitud=int(input("Ingresa la longitud del pendulo: "))
     
     Cv= int(input("Ingresa la constante de friccion viscola :"))
     #condicion hasta que se cum`pla
     if masa>0 and gravedad>0 and longitud>0 and Cv>0:
         pivote=False
          
 except Exception:
     pass
     print("INGRESA UN NUMERO ENTERO POSITIVO")  
print()

import numpy as np#importamos librerias para la graficacion
import matplotlib.pyplot as plt

#las condiciones iniciales
t=0.
thetainc=0
omegainc=0.5
u=np.array([thetainc,omegainc]) #cambio de variale

#campo de direcciones
def F(u,t):
    return np.array([u[1],-gravedad*np.sin(u[0])/1])

#solucion
tsol=[t]
thetasol=[u[0]]
omegasol=[u[1]]
dt=0.05
tfin=10.

#aplicamos el metodo de ouler
while t<tfin:
    u=u+F(u,t)*dt
    t=t+dt
    thetasol.append(u[0])
    omegasol.append(u[1])
    tsol.append(t)


import matplotlib.animation as animation

#thetasol=np.array(thetasol)
fig=plt.figure()
ax=fig.gca()

def actualizar(i):#se hace la graficacion del pendulo
    ax.clear()
    plt.plot([0,longitud*np.sin(thetasol[i])],[0,-longitud*np.cos(thetasol[i])],'b-')
    plt.plot(longitud*np.sin(thetasol[i]),-longitud*np.cos(thetasol[i]),'ro')
    plt.title(str(round(tsol[i],3)))
    plt.xlim(-longitud-1,longitud+1)
    plt.ylim(-longitud-1,1)

ani=animation.FuncAnimation(fig, actualizar, range(len(tsol)))
plt.show()