'''
Practica 13
Generar un programa que mediante recursividad permita resolver el problema de las Torres de Hanoi, 
permitir que el usuario ingrese el número de discos que se deben de mover (cerrar el intervalo de 3 a 15 discos) y 
mostrar los movimientos que se deben de realizar (todo puede ser en texto, aunque, de ser posible, mostrar los discos y los movimientos)
@utor: Francisco Zamora Saldaña
Programación avanzada 2MM3
'''

def numeroentero(t):
    while True:
        user = input(t)
        try:
            n= int(user)
        except:
            print("¡¡Debe ser numero entero y positivo de 3 a 15!! \n")
        else:
            if n % 1 == 0 and n >= 3 and n <= 15:
                break
            elif n == 0:
                print("el zero es la mitad de la recta no jala")
            else:
                print("¡¡Debe ser entero y positivo de 3 a 15!! \n")
    return n

def Torredehanoi(n , fuente, destino, auxiliar):
     
      if n==1:
          print ("Mover el disco 1 de la fuente",fuente,"al destino",destino)
          return
      Torredehanoi(n-1, fuente, auxiliar, destino)
      print ("Mover el disco",n,"de la fuente",fuente,"al destino",destino)
      Torredehanoi(n-1, auxiliar, destino, fuente)

n=numeroentero("Ingrese hasta que numero de discos que queire mover(De 3 a 15 discos): ")

Torredehanoi(n,'A','B','C')