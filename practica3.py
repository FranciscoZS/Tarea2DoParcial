'''
Practica 3
Programa que permita ingresar una función f(x) polinomial cualquiera y mediante el Método de Lin-Bairstow 
obtener todas las ráices de la función polinomial una de las raíces de la función, 
por lo que en primer lugar se deben introducir los valores r0 y s0 que debe ingresarse. 
El programa también debe mostrar y guardar en un archivo de texto (.txt) la tabla con los siguientes valores: |i ri si εr εs|, 
donde i es el número de iteración, factores ri y si y los errores de los factores εr εs
@utor: Francisco Zamora Saldaña
Programación avanzada 2MM3
'''

def numeroenteropositivo(t):
    while True:
        user = input(t)
        try:
            n= int(user)
        except:
            print("¡¡Debe ser numero entero y positivo!! \n")
        else:
            if n % 1 == 0 and n >0 and n<5:
                break
            elif n == 0:
                print("el zero es la mitad de la recta no jala")
            else:
                print("¡¡Debe ser entero y positivo menor que 5!!")
    return n


lbarm=open("archivo de ejercicio numerico 3 lbarlistow.txt","w")
grad=[]
constantes=[]
suma=[]
eqr=[]
eqs=[]
suma2=[]


grado="Ingresa el grado del polinomio (menor a 5) : "

grado=numeroenteropositivo(grado)


for k in range(grado+1):
    grad.append(grado-k+1)

for k in range(grado+1):
    constantes.append(float(input("Ingrese el coeficiente la variable de grado {:1d} : ".format(grado-k))))
    
r=float(input("Ingresa el valor de ro: "))
s=float(input("Ingresa el valor de So: "))
lbarm.write("r=%s\n"%r)
lbarm.write("s=%s\n"%s)

def Solucion(r,s):
    
    b1=1
    b0=1
    i=0
    delta_r=0
    delta_s=0

    while (b0!=0 and b1!=0):
        r=r+delta_r
        s=s+delta_s
        suma.clear()
        suma2.clear()
    
        suma.append(constantes[0])
        for k in range(1,grado+1):
            if k==1:
                valor=(suma[k-1]*r+constantes[k])
                suma.append(round(valor,10))
            else:
                valor=(suma[k-1]*r+suma[k-2]*s+constantes[k])
                suma.append(round(valor,10))
            
        suma2.append(suma[0])
        for k in range(1,grado+1):
            if k==1:
                valor=suma2[k-1]*r+suma[k]
                suma2.append(round(valor,10))
            else:
                valor=suma2[k-1]*r+suma2[k-2]*s+suma[k]
                suma2.append(round(valor,10))
        i+=1
        lbarm.write("i=%s\n"%i)
        b0=suma[grado]
        b1=suma[grado-1]
        c1=suma2[grado-1]
        c2=suma2[grado-2]
        c3=suma2[grado-3]
    
        delta_s=((b1*c1)-(b0*c2))/((c2**2)-(c1*c3))
        delta_r=((b0*c3)-(b1*c2))/((c2**2)-(c1*c3))
        lbarm.write("delta_s=%s\n"%delta_s)
        lbarm.write("delta_r=%s\n"%delta_r)
    
    x1=(r+(r**2+4*s)**(1/2))/2
    x2=(r-(r**2+4*s)**(1/2))/2 
    
 
    print("Una raiz del polinomio es = "+str(x1))   
    print("Una raiz del polinomio es = "+str(x2))
    x2=(-suma[1]+((suma[1]**2)-(4*suma[0]*suma[2]))**(1/2))/(2*suma[0])
    print("Una raiz del polinomio es = "+str(x2))
    x2=(-suma[1]-((suma[1]**2)-(4*suma[0]*suma[2]))**(1/2))/(2*suma[0])
    print("Una raiz del polinomio es = "+str(x2))
    
Solucion(r,s)   
lbarm.close()