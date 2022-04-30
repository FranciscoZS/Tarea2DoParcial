'''
Practica 10
Programa que permita cifrar un texto ingresado por medio del algoritmo RSA Así funciona el algoritmo RSA y Ejemplo algoritmo RSA, 
otro ejemplo, otro más. Para este programa se debe de generar una función de cifrado y otra de descifrado, 
en donde la primera reciba una cadena de texto y almacene un archivo (.txt) con la cadena cifrada y lo necesario para descifrar, 
mientras que la función de descifrado debe recibir el archivo cifrado y obtener la cadena original, 
de ser posible utilizar los paradigmas de programación orientada a objetos y funcional
@utor: Francisco Zamora Saldaña
Programación avanzada 2MM3
'''

def numeroentero(t):
    while True:
        user = input(t)
        try:
            n= int(user)
        except:
            print("¡¡Debe ser numero entero y positivo !! \n")
        else:
            if n % 1 == 0 and n >0:
                break
            elif n == 0:
                print("el zero es la mitad de la recta no jala")
            else:
                print("¡¡Debe ser entero y positivo!! \n")
    return n


cala8 =open("archivo de jercicio rsa .txt","w")
def cifrado(m1,e,n):
    cifrar=[None]*len(m1)
    for i in range(len(m1)):
        cifrar[i]=(m1[i]**e)%n
    return cifrar

def desifrado(frase,e,d):
    desifrar=[None]*len(frase)
    for i in range(len(frase)):
        desifrar[i]=(frase[i]**d)%n
    return desifrar
           
archivo=open("cifrado.txt","w")
p=numeroentero("ingrese P : ")
q=numeroentero("ingrese Q : ")

if p==q:
   print("P debe ser diferente a Q")
else:
    n=p*q
    o=(p-1)*(q-1)
    e=numeroentero("ingrese el valor de e :   ")
    clave_publica=[e,n]    
        
    
    k=numeroentero("ingrese el valor de k: ")
    d=(1+ k*o)//e                                                     
    clave_privada=[d,n]
        
    m=str(input("ingrese la frase a cifrar: "))
    m=m.lower()
    
    m1=[None]*len(m)
    for i in range(len(m)):                                     
       if(ord(m[i])==32):
          m1[i]=0
       else:
          m1[i]=ord(m[i])-97
    
    
    cifrar=cifrado(m1,e,n)
    desifrar=desifrado(cifrar,e,d)
    print("\nSU CIFRADO ES: " + str(cifrar))
    print("SU DESIFRADO ES: "+ str(desifrar))
    
    
    archivo=open("cifrado.txt","r")
    
    for i in range(len(cifrar)):
        cala8.write("cifrar=%s\n"%cifrar)
cala8.close()