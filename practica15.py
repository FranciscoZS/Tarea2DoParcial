'''
Practica 15
Programa que permita calcular n números de la serie de Fibonacci, con valores de n en el intervalo [1, 10000]
@utor: Francisco Zamora Saldaña
Programación avanzada 2MM3
'''

def numeroentero(t):
    while True:
        user = input(t)
        try:
            n= int(user)
        except:
            print("¡¡Debe ser numero entero y positivo entre 1 y 10000!! \n")
        else:
            if n % 1 == 0 and n >0  and n<10001:
                break
            elif n == 0:
                print("el zero es la mitad de la recta no jala")
            else:
                print("¡¡Debe ser entero y positivo entre 1 y 10000!! \n")
    return n

n=numeroentero("hasta que valores de n quieres calcular de la serie de fibonacci recuerda que debe ser del 1 al 10000:\n")

cache ={}

def fib(n):
    if n in cache:
        return cache[n]
    result = 0
    
    if n  <= 1:
        return n
    else: 
        result= fib(n-1)+fib(n-2)
    cache[n] = result
    print(n, " - ", cache[n])
    return result


if n == 1:
    print(n, " - 1")    
else:
    a=1
    print(a," -  1")
    print(fib(n))