'''
Practica 8
Generar un programa que acepte una cadena de texto que representan una constraseña; el programa debe revisar que la contraseña sea válida, 
tomando en cuenta los siguientes criterios:
Debe contener al menos una letra minúscula [a-z]
Debe contener al menos un número [0-9]
Debe contener al menos una letra mayúscula [A-Z], no en la primera posición
Debe contener al menos un caracter especial [$, #, @, _]
Longitud mínima - máxima de la contraseña, 6-12 caracteres
Sólo hasta que se ingresa la contraseña correcta, el programa debe permitir continuar. Una vez que se ingrese una contraseña válida, 
el programa guardará la contraseña cifrada mediante el algoritmo César del grupo de ejercicios I (problema 26), 
seleccionando de manera aleatoria entre [0,20], el número de posiciones a mover, 
y guardando primero dicho número seguido de la contraseña en el archivo de texto (.txt). 
Este archivo debe irse actualizando con todas las contraseñas que se vayan ingresando en el programa
@utor: Francisco Zamora Saldaña
Programación avanzada 2MM3
'''

import random
import re
import os

while True:
  user = input("Ingresa la contraseña con los siguientes requerimientos: \nDebe contener al menos una letra minúscula [a-z] \nDebe contener al menos un número [0-9]\nDebe contener al menos una letra mayúscula [A-Z], no en la primera posición \nDebe contener al menos un caracter especial [$, #, @, _] \nLongitud mínima - máxima de la contraseña, 6-12 caracteres \n ")
  validar = False

  if (len(user)<6 or len(user)>12):
    print("¡No es válido! El total de caracteres debe estar entre 6 y 12")
    continue
  elif not re.search("[A-Z]",user):
    print("No es válido ! Debe contener una letra entre [A-Z]")
    continue
  elif not re.search("[a-z]",user):
    print("¡No es válido! Debe contener una letra entre [a-z]")
    continue
  elif not re.search("[1-9]",user):
    print("¡No válido! Debe contener una letra entre [1-9]")
    continue
  elif not re.search("[~!@#$%^&*]",user):
    print("¡No válido! Debe contener al menos una letra en [~! @ # $% ^ & *]")
    continue
  else:
    validar = True
    break

if(validar):
  print("contraseña aceptada ")

userstr=[str(a) for a in user]
index=len(userstr)
abc="abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
abcstr=[str(b) for b in abc]

print(f"Tu texto es: {user}")

n=random.randint(0,20)

abcstrc=abcstr.copy()
cifradoc=abcstr

for i in range(0,n):
    cifradoc.sort(key = abcstr[0] .__eq__)

textoc=[]
dic={}

for j in range(0,54):
    dic[abcstrc[j]]=cifradoc[j]

for k in range(0,index):
    value=userstr[k]
    try:
        textoc.append(dic[value])
    except:
        textoc.append(value)

print("Tu acordeon de cifraado es:\n")

for key in dic:
  print(key, ":", dic[key])


print(f"Tu texto cifrado con un desplazamiento de {n} espacios a la derecha es:\n", ''. join(textoc))
cnt = ''. join(textoc)

archivo = open("contraseñas.txt","a")
archivo.write(f"\n{n}\t {cnt}\n")
archivo.close()