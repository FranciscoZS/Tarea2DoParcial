'''
Practica 20
Generar un programa que realice la simulación de un tiro parabólico para el cual se le ingresen los valores de la velocidad incial v0, 
el ángulo inicial θ0, la altura inicial de donde saldrá el proyectil h0 y la aceleración de la gravedad que afectará al proyectil, 
así como los pasos en el tiempo δt que se tomarán para realizar la simulación, 
la cual deberá detenerse cuando el proyectil llegue al suelo y = 0. Los datos de la simulación deben de guardarse a su vez en un archivo de texto 
(.txt) con formato de tabla |i x y t |, donde i es el paso, la posición en (x,y) y 
el tiempo t de vuelo del proyectil, considerar los siguientes casos:
Caso ideal, en donde el proyectil no se ve afectado por la fricción del aire, 
noni tampoco existen cambios en la densidad del aire o de la gravedad (caso estudiado por los libros de física)
Considerar que existe un componente de desaceleración debida a la fricción del proyectil con el aire, 
la cual esta dada por a_friccion = Coef_aer * 0.5 * rho * A * (vx^2 + vy^2)/masa*cos(angulo), donde:
Coef_aer -> coeficiente aerodinámico del proyectil
rho -> densidad del aire a nivel del mar
A -> Area transversal del proyectil
vx, vy -> velocidad en x,y del proyectil
masa -> masa del proyectil
angulo -> ángulo en el movimiento del proyectil
Tomar en cuenta estas cantidades que sean ingresadas por el usuario. Obtener la gráfica con este modelo
Considerar que existe un cambio en la densidad del aire en cuento el proyectil alcance alturas considerables. 
La densidad del aire cambia de acuerdo a la ecuación: rho = -0.0001031*y + 1.216, donde y es la altura del proyectil y rho la densidad del aire
Finalmente, para que el modelo sea aún más completo, la aceleración de la gravedad también se ve modificada de acuerdo con la altura 
(entre más alejado este un objeto, experimentará menor gravedad), lo cual está modelado mediante la ecuación g = g0 * (r/(r+y))^2, donde:
g0 -> gravedad a nivel del mar (9.80655 m/s^2)
r -> radio de la tierra
Comparar las gráficas de todos los casos. De ser posible, generar la animación de como se mueve el objeto en cada caso.
@utor: Francisco Zamora Saldaña
Programación avanzada 2MM3
'''

import numpy as np
import matplotlib.pyplot as plt

def limite(cad, a, b):
    val = 0
    while True:
        val = float(input("Ingresar " + cad))
        if (val > a) and (val < b):
            break
    return val

def simula(caso, v0, an0, h0, vx, vy, g, radT, C_air, rho, A, m, dt, text):
    i = 0
    x = [0]
    y = [h0]
    vx = vx
    vy = vy
    ax = 0
    ay = 0
    f = open( text + "_" + str(caso) + ".txt" ,"w")
    
    f.write("---Caso {}---\n". format(caso))
    f.write("Velocidad inicial        : {} m/s\n".format(v0))
    f.write("Ángulo inicial           : {} °\n".format(an0))
    f.write("Altura inicial           : {} m\n".format(h0))
    f.write("Masa proyectil           : {} kg\n".format(m))
    f.write("Área del proyectil       : {} m^2\n".format(A))
    f.write("Coeficiente aerodinámico : {} \n".format(C_air))
        
    print("{0} {1} {2} {3} {4} {5}".format('i'.rjust(6,' '), 'x'.rjust(12, ' '), 'y'.rjust(12, ' '), '\u0394t'.rjust(12, ' '), 'g [m/s\u00B2]'.rjust(12, ' '), '\u03C1 [kg/m\u00B3]'.rjust(12, ' ')))
    f.write( "{0} {1} {2} {3} {4} {5}\n".format('i'.rjust(6,' '), 'x'.rjust(12, ' '), 'y'.rjust(12, ' '), 'dt'.rjust(12, ' '), 'g [m/s^2]'.rjust(12, ' '), 'rho [kg/m^3]'.rjust(12, ' ')) )
    while True:
        if(caso == 1):
            rho = 0
            gc = g
        if(caso == 2):
            rho = rho
            gc = g
        if(caso == 3):
            rho = -0.0001031*y[i] + 1.216
            gc = g
        if(caso == 4):
            rho = -0.0001031*y[i] + 1.216
            gc = g*( ( radT/(radT+y[i]) )**2 )
        
        angle = np.tan( vy/vx )
        ax = -C_air*0.5*rho*A*(vx**2 + vy**2)/m*np.cos(angle)
        ay = -gc - C_air*0.5*rho*A*(vx**2 + vy**2)/m*np.sin(angle)
        
        print("{0:6d} {1:12.4f} {2:12.4f} {3:12.4f} {4:12.4f} {5:12.4f}".format(i, x[i], y[i], i*dt, gc, rho))
        f.write("{0:6d} {1:12.4f} {2:12.4f} {3:12.4f} {4:12.4f} {5:12.4f}\n".format(i, x[i], y[i], i*dt, gc, rho))
        vx = vx + ax * dt
        vy = vy + ay * dt
                
        if( y[i] < 0 ):
            break
        
        x.append( x[i] + vx*dt + (1/2)*ax*(dt**2) )
        y.append( y[i] + vy*dt + (1/2)*ay*(dt**2) )
        i += 1
    
    f.close()
    return x, y

v0 = float(input("Ingrese la velocidad inicial: "))
an0 = float(input("Ingrese el angulo inicial: "))
h0 = float(input("Ingrese la altura inicial: "))
m = float(input("Ingrese la masa del proyectil: "))
A = float(input("Ingrese el area del proyectil: "))
C_air = 0.25
g= 9.80665
rho = 1.2254
dt = 0.1
radT = 6371000
texto = "proyectil"

th0 = an0 * np.pi / 180
vx = v0 * np.cos(th0)
vy = v0 * np.sin(th0)

x, y = simula(1, v0, an0, h0, vx, vy, g, radT, C_air, rho, A, m, dt, texto)
x1, y1 = simula(2, v0, an0, h0, vx, vy, g, radT, C_air, rho, A, m, dt, texto)
x2, y2 = simula(3, v0, an0, h0, vx, vy, g, radT, C_air, rho, A, m, dt, texto)
x3, y3 = simula(4, v0, an0, h0, vx, vy, g, radT, C_air, rho, A, m, dt, texto)

plt.plot(x, y, color=(1,0,0))
plt.plot(x1, y1, color=(0,0,1))
plt.plot(x2, y2, color=(0,0,0))
plt.plot(x3, y3, color=(0,1,0))
plt.xlabel('x [m]')
plt.ylabel('y [m]')
plt.legend(['Ideal','Fricción',r'Fricción, $ \Delta\rho_{aire} $ ',r'Fricción, $ \Delta\rho_{aire}  \Delta g $ '], loc='upper right')
plt.grid()
plt.savefig(texto + '_fig.png', transparent = True, dpi = 300)
plt.show()