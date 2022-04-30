'''
Practica 7
Utilizando recursividad, generar un programa que calcule la suma harmónica de un número entero positivo N ingresado por el usuario
@utor: Francisco Zamora Saldaña
Programación avanzada 2MM3
'''


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
                print("¡¡Debe ser entero y positivo!! \n")
    return n

def recurSum(nar):
    if nar <= 1:#por la recursividad la suma armonica 
        return nar
    return 1/nar + recurSum(nar - 1)
 

nar = "Ingrese hasta que numero quiere la suma armonica(Por recursividad): "
nar =  numeroentero(nar)
print(recurSum(nar))