'''
Practica 11
Programa que pemita obtener el RFC con homoclave de una persona, 
solicitando los datos necesarios (Nombre, Apellidos, Fecha de Nacimiento), 
siguiendo para ello las instrucciones proporcionadas por la SHCP ¿Cómo generar el RFC? utilizar, 
de ser posible, el paradigma de programación orientado a objetos
@utor: Francisco Zamora Saldaña
Programación avanzada 2MM3
'''


def nep(message = " "):
            while True:
                user = input(message)
                try:
                    n= int(user)
                except:
                    print("¡¡Debe ser numero entero y positivo!! \n")
                else:
                    if n % 1 == 0 and n >0 :
                        break
                    elif n == 0:
                        print("el zero es la mitad de la recta no jala")
                    else:
                        print("¡¡Debe ser entero y positivo!!")
            return n

def mes():
    while True:
        mes = input("Dame tu mes de nacimiento:\n")
        mes = mes.upper()
        if mes == "ENERO" or mes == "FEBRERO" or mes == "MARZO" or mes == "ABRIL" or mes == "MAYO" or mes == "JUNIO"  or mes == "JULIO" or mes == "AGOSTO" or mes == "SEPTIEMBRE" or mes == "OCTUBRE" or mes == "NOVIEMBRE" or mes == "DICIEMBRE":
            m = mes
            break
        else:
            print("Mes invalido vuelve a introducir")
    return m

def dia(mes,año):
    while True:
                user = input("Dame el dia de nacimiento:\n")
                if año % 4 == 0 and año % 100 != 0 or año % 400 == 0:
                    b="b"
                else:
                    b="nb"
                try:
                    n= int(user)
                except:
                    print("¡¡Debe ser numero entero y positivo!! \n")
                else:
                    if n % 1 == 0 and n >0 :
                        if (n<=31 and n>=1) and (mes == "ENERO" or mes == "MARZO" or mes == "MAYO" or mes == "JULIO" or mes == "AGOSTO" or mes == "OCTUBRE" or mes == "DICIEMBRE"):
                            break
                        elif (n<=30 and n>=1) and (mes == "ABRIL" or mes == "JUNIO" or mes == "SEPTIEMBRE" or mes == "NOVIEMBRE"):
                            break
                        elif b == "b" and (n<=29 and n>=1) and mes == "FEBRERO":
                            break
                        elif b == "nb" and (n<=28 and n>=1) and mes == "FEBRERO":
                            break
                    elif n == 0:
                        print("el zero es la mitad de la recta no jala")
                    else:
                        print("¡¡Debe ser entero y positivo!!")
    return n

class persona:
    def __init__(self,nombre,apellidopa,apellidoma,dia,mes,año):
        self.name=nombre
        self.surnamepa=apellidopa
        self.surnamema=apellidoma
        self.day=dia
        self.month=mes
        self.year=año
    
    def rfc(self):
        def cp_month(month):
            month = month.upper()
            mes={"ENERO":"01",
                   "FEBRERO":"2",
                   "MARZO":"03",
                   "ABRIL":"04",
                   "MAYO":"05",
                   "JUNIO":"06",
                   "JULIO":"07",
                   "AGOSTO":"08",
                   "SEPTIEMBRE":"09",
                   "OCTUBRE":"10",
                    "NOVIEMBRE":"11",
                    "DICIEMBRE":"12"}
            digito=mes.get(month)
            return digito

        def cp_name(name,surnamepa):
            name=name.upper()
            if len(surnamepa)<=2:
                name=name[0]+name[1]
            else:
                name=name[0]
            return name
        
        def cp_surnamepa(surnamepa):
            surnamepa=surnamepa.upper()
            if len(surnamepa)<=2:
                surnamepa = surnamepa[0]
            else:
                if surnamepa[1] =="A" or surnamepa[1] == "E" or surnamepa[1] =="I" or surnamepa[1] == "O" or surnamepa[1] == "U":
                    surnamepa = surnamepa[0]+surnamepa[1]
                elif surnamepa[2] =="A" or surnamepa[2] == "E" or surnamepa[2] =="I" or surnamepa[2] == "O" or surnamepa[2] == "U":
                    surnamepa = surnamepa[0]+surnamepa[2]
                else:
                    surnamepa = surnamepa[0]+surnamepa[3]
            return surnamepa

        def cp_surnamema(surnamema):
            surnamema=surnamema.upper()
            surnamema = surnamema[0]
            return surnamema

        def cp_year(year):
            year=str(year)
            if len(year) == 1:
                year = "0"+year
            elif len(year)==2:
                year = year
            else:
                year =year[-2]+year[-1]
            return year

        def cp_day(day):
            day =str(day)
            if len(day)==1:
                day="0"+day
            return day

        c_name=cp_name(self.name,self.surnamepa)
        c_surnamepa=cp_surnamepa(self.surnamepa)
        c_surnamema=cp_surnamema(self.surnamema)
        c_year=cp_year(self.year)
        c_month=cp_month(self.month)
        c_day=cp_day(self.day)

        print("Tu RFC es:")
        print(c_surnamepa+c_surnamema+c_name+c_year+c_month+c_day)




nombre = input("Dame tu nombre:\n")
apellidopa = input("Dame tu apellido paterno:\n")
apellidoma = input("Dame tu apellido materno:\n")
año = nep("Dame el año de tu nacimientos:\n")
mesna = mes()
diana = dia(mesna,año)



ciudadano = persona(nombre,apellidopa,apellidoma,diana,mesna,año)

ciudadano.rfc()

nombre = ciudadano.name+' '+ciudadano.surnamepa+' '+ciudadano.surnamema
nombrecompleto=nombre.upper()



def generar_homoclave(nombre_completo):
    suma_numeros_nombre = 0
    numeros_nombre = '0'
    for letra in nombre_completo:
        if letra in tabla1:
            numeros_nombre += tabla1[letra]
    
    suma = 0
    for i in range(len(numeros_nombre) -1 ):
        suma += int(numeros_nombre[i] + numeros_nombre[i+1]) * int(numeros_nombre[i+1])
    
    suma_numeros_nombre = int(str(suma)[-3::])    # Tomamos los ultimos tres numeros

    digitos = [int(suma_numeros_nombre / 34), suma_numeros_nombre % 34]
    homoclave = ''
    if digitos[0] in tabla2:
        homoclave += tabla2[digitos[0]]
    if digitos[1] in tabla2:
        homoclave += tabla2[digitos[1]]
    
    return homoclave

tabla1 = {
    ' ' : '00', '0' : '00', '1' : '01', '2' : '02', '3' : '03', '4' : '04', 
    '5' : '05', '6' : '06', '7' : '07', '8' : '08', '9' : '09', '&' : '10',
    'A' : '11', 'B' : '12', 'C' : '13', 'D' : '14', 'E' : '15', 'F' : '16',
    'G' : '17', 'H' : '18', 'I' : '19', 'J' : '21', 'K' : '22', 'L' : '23',
    'M' : '24', 'N' : '25', 'O' : '26', 'P' : '27', 'Q' : '28', 'R' : '29',
    'S' : '32', 'T' : '33', 'U' : '34', 'V' : '35', 'W' : '36', 'X' : '37',
    'Y' : '38', 'Z' : '39', 'Ñ' : '40'
}

tabla2 = {
     0 : '1',  1 : '2',  2 : '3',  3 :  '4', 4 :  '5', 5 : '6',  6 : '7',  7 : '8', 8 : '9', 
     9 : 'A', 10 : 'B', 11 : 'C', 12 : 'D', 13 : 'E', 14 : 'F', 15 : 'G', 16 : 'H',
    17 : 'I', 18 : 'J', 19 : 'K', 20 : 'L', 21 : 'M', 22 : 'N', 23 : 'P', 24 : 'Q',
    25 : 'R', 26 : 'S', 27 : 'T', 28 : 'U', 29 : 'V', 30 : 'W', 31 : 'X', 32 : 'Y', 33 : 'Z'
}

homoclave=generar_homoclave(nombrecompleto)

print(f"Y tu homo clave es:\n{homoclave}")