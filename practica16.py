'''
Practica 16
Generar un programa que lea de la internet el siguiente texto: Romeo and Juliet by William Shakesperare y obtenga la estadítica, 
junto con su respectivo histograma, del número de letras que aprecen en el texto 
(esto es cuantas a's, cuántas b's, cuántas c's y así sucesivamente). (piden aprender a hackear, veamos con esto si pueden dar sus primeros pasos)
@utor: Francisco Zamora Saldaña
Programación avanzada 2MM3
'''

#importaos libreria para el archio de internet
import urllib.request
datos= urllib.request.urlopen('https://automatetheboringstuff.com/files/rj.txt').read().decode()
#ponemos la url de la pagina donde esta el texto
LETRAS=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
letras=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]
#generamos los diccionarios 
print("\nMayusculas\n")
for i in range(len(LETRAS)):
    print(f"La letra {LETRAS[i]} tiene: {datos.count(LETRAS[i])} caracteres")
    
print("\nMinusculas\n")
for x in range(len(letras)):
    print(f"La letra {letras[x]} tiene : {datos.count(letras[x])} caracteres")