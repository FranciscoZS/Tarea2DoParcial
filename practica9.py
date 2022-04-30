'''
Practica 9
Generar un programa que simule la entrega de un a mano de cartas de la baraja inglesa (5 cartas en total) a dos jugadores 
(debe mostrarse las dos manos en la consola). Utilizar la programación orientada a objetos para resolver este programa
@utor: Francisco Zamora Saldaña
Programación avanzada 2MM3
'''

import random
class Carta:
           # atributos
           #cada carta tiene un digujo y un numero, hacemos su plantilla
           def __init__(self,dibujos,numeros):
             self.dibujos = dibujos
             self.numeros = numeros
           #funcion str
           def __str__(self):
               return self.numeros+' de '+self.dibujos
class Baraja:
     def __init__(self):
         #es para declarar la lista de dibujos y números
         self.dibujos = ['Espadas','Diamantes','treboles','corazones']
         self.numeros = ['As','2','3','4','5','6','7','8','9','10','Jack','Reina','Rey']

         #inicializando la baraja de cartas
         self.baraja = []
         for i in self.dibujos:
             for j in self.numeros:
                 #Añade cartas a la baraja
                 self.baraja.append(Carta(i,j))
     def deal(self):
         #elegir una carta al azar de la baraja
         cartaRandom = random.choice(self.baraja)
         #sacar la carta de la baraja y devolverla
         # para para que no se vuelva a repartir
         self.baraja.remove(cartaRandom)
         return cartaRandom
def main():
    #inicio de baraja
    baraja = Baraja()
    #manos de los 2 jugadores
    Jugador1 = []
    Jugador2 = []
    #se daran 5 cartas por jugador
    for i in range(5):
         Jugador1.append(baraja.deal())
         Jugador2.append(baraja.deal())
    #mostrando las manos de cada jugador
    print("Mano de jugador 1:")
    for i in Jugador1:
        print(i)
    print("\nMano de jugador 2:")
    for i in Jugador2:
        print(i)
# llamando al método principal
main()