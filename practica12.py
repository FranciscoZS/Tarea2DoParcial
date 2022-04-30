'''
Practica 12
Programa que permita obtener el CURP completo de una persona, solicitando los datos necesarios (Nombre, Apellidos, Fecha de Nacimiento, 
lugar de nacimiento), siguiendo para ello las instrucciones proporcionadas en el DOF Normativa para generar el CURP, DOF utilizar, 
de ser posible, el paradigma de programación orientado a objetos. Omitir los dos últimos dígitos asignados por el RENAPO
@utor: Francisco Zamora Saldaña
Programación avanzada 2MM3
'''

#para esta practiva reutilizare la parte inicial que es la del rfc

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

def genero():
    while True:
        a=input("Cual es tu genero:\n")
        a=a.upper()
        if a=="HOMBRE" or a=="MUJER" or a=="NO BINARIO":
            break
        else:
            print("Genero no incluido perdon no te queremos discriminar pero seguimos trabajando en favor de la inclusion\n")
        
    return a

def estado():
    while True:
        estado=["AGUASCALIENTES",
                       "BAJA CALIFORNIA SUR",
                       "BAJA CALIFORNIA",
                       "COAHUILA",
                       "CAMPECHE",
                       "COLIMA",
                       "CHIHUAHUA",
                       "CHIAPAS",
                       "CIUDAD DE MEXICO",
                       "DURANGO",
                       "GUANAJUATO",
                       "GUERRERO",
                       "HIDALGO",
                       "JALISCO",
                       "MEXICO",
                       "MICHOACAN",
                       "MORELOS",
                       "NAYARIT",
                       "NUEVO LEON",
                       "OAXACA",
                       "PUEBLA",
                       "QUERETARO",
                       "QUINTANA ROO",
                       "SAN LUIS POTOSI",
                       "SINALOA",
                       "SONORA",
                       "TABASCO",
                       "TAMAULIPAS",
                       "TLAXCALA",
                       "VERACRUZ",
                       "YUCATAN",
                       "ZACATECAS",
                       "NACIDO EN EL EXTRANJERO"]
        
        a=input("En que estado naciste. (Notas si fue en el estado de mexico escribir solo Mexico y si naciste en el extranjero poner Nacido en el extranjero):\n")
        a=a.upper()
        if a in estado:
            break
        else:
            print("Estado invalido vuelve a intentarlo\n")
        
    return a

class persona:
    def __init__(self,nombre,apellidopa,apellidoma,dia,mes,año,genero,estado):
        self.name=nombre
        self.surnamepa=apellidopa
        self.surnamema=apellidoma
        self.day=dia
        self.month=mes
        self.year=año
        self.gender=genero
        self.state=estado
    
    def curp(self):
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
        
        def cp_gender(gender):
            gender=gender.upper()
            genero={"HOMBRE":"H",
                           "MUJER":"M",
                            "NO BINARIO":"I"}
            gender=genero.get(gender)
            return gender
        
        def cp_state(state):
            state=state.upper()
            estado={"AGUASCALIENTES":"AS",
                       "BAJA CALIFORNIA SUR":"BS",
                       "BAJA CALIFORNIA":"BC",
                       "COAHUILA":"CL",
                       "CAMPECHE":"CC",
                       "COLIMA":"CM",
                       "CHIHUAHUA":"CH",
                       "CHIAPAS":"CS",
                       "CIUDAD DE MEXICO":"DF",
                       "DURANGO":"DG",
                       "GUANAJUATO":"GT",
                       "GUERRERO":"GR",
                       "HIDALGO":"HG",
                       "JALISCO":"JC",
                       "MEXICO":"MC",
                       "MICHOACAN":"MN",
                       "MORELOS":"MS",
                       "NAYARIT":"NT",
                       "NUEVO LEON":"NL",
                       "OAXACA":"OC",
                       "PUEBLA":"PL",
                       "QUERETARO":"QT",
                       "QUINTANA ROO":"QR",
                       "SAN LUIS POTOSI":"SP",
                       "SINALOA":"SL",
                       "SONORA":"SR",
                       "TABASCO":"TC",
                       "TAMAULIPAS":"TS",
                       "TLAXCALA":"TL",
                       "VERACRUZ":"VZ",
                       "YUCATAN":"YN",
                       "ZACATECAS":"ZS",
                       "NACIDO EN EL EXTRANJERO":"NE"}
        
            state=estado.get(state)
        
            return state 
        
        def ci(surnamepa,surnamema,name):
            surnamepa=surnamepa.upper()
            surnamema=surnamema.upper()
            name=name.upper()
            surnamepa=surnamepa[1:]
            surnamema=surnamema[1:]
            name=name[1:]
            vocals=['A','E','I','O','U']
            for letra in surnamepa:
                if letra in vocals:
                    pass
                else:
                    a = letra
                    break
                    
            for letra in surnamema:
                if letra in vocals:
                    pass
                else:
                    b = letra
                    break
                    
            for letra in name:
                if letra in vocals:
                    pass
                else:
                    c = letra
                    break
                    
            return a+b+c
            
        c_name=cp_name(self.name,self.surnamepa)
        c_surnamepa=cp_surnamepa(self.surnamepa)
        c_surnamema=cp_surnamema(self.surnamema)
        c_year=cp_year(self.year)
        c_month=cp_month(self.month)
        c_day=cp_day(self.day)
        c_gender=cp_gender(self.gender)
        c_state=cp_state(self.state)
        c_ci=ci(self.surnamepa,self.surnamema,self.name)
        

        print("Tu CURP es:")
        print(c_surnamepa+c_surnamema+c_name+c_year+c_month+c_day+c_gender+c_state+c_ci)




nombre = input("Dame tu nombre:\n")
apellidopa = input("Dame tu apellido paterno:\n")
apellidoma = input("Dame tu apellido materno:\n")
año = nep("Dame el año de tu nacimientos:\n")
mesna = mes()
diana = dia(mesna,año)
generod = genero()
estadod=estado()


ciudadano = persona(nombre,apellidopa,apellidoma,diana,mesna,año,generod,estadod)
ciudadano.curp()
