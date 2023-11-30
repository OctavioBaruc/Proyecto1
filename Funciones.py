# Prueba

def Capital() :
    #Inicializamos las variables en para que, si el usuario desea hacer otra vez la misma operación, los valores de la operación anterior no se guarden
    Cap=0
    Act=0
    Pas=0
    try :
        Act = float(input("Ingresa el activo: "))
        Pas = float(input("ingresa el Pasivo: "))
        Cap = Act - Pas
        print("Tu Capital vale : $", Cap)
        Enter = input("Presione Enter para continuar.")
    except :
        print("Ingresa valores numéricos válidos")
        Enter = input("Presione Enter para continuar.")

#Definimos ahora la parte para sacar el Pasivo
def Pasivo () :
    #Inicializamos las variables en para que, si el usuario desea hacer otra vez la misma operación, los valores de la operación anterior no se guarden
    Cap=0
    Act=0
    Pas=0
    try :
        Act = float (input("Ingresa el Activo: "))
        Cap = float (input("Ingresa el Capital: "))
        Pas = Act - Cap
        print("Tu pasivo vale: $", Pas)
        Enter = input("Presione Enter para continuar.")
    except :
        print("Ingresa valores numéricos válidos")
        Enter = input("Presione Enter para continuar.")
#Sigue definir la parte de com sacar el Activo
def Activo () :
        #Inicializamos las variables en para que, si el usuario desea hacer otra vez la misma operación, los valores de la operación anterior no se guarden
    Cap=0
    Act=0
    Pas=0
    try :
        Pas = float(input("Ingresa el Pasivo: "))
        Cap = float(input("Ingresa el Capital: "))
        Act = Pas + Cap
        print("Tu Activo vale: $", Act)
        Enter = input("Presione Enter para continuar.")
    except:
        print("Ingresa valores numéricos válidos")
        Enter = input("Presione Enter para continuar.")

#Definiremos la parte del código donde sacaremos la velocidad de un objeto del apartado de Física
def Velocidad ():
    distan=0
    tiemp=0
    Veloc=0
    try :
        distan = float(input("Ingresa la distancia en la que se encuentra el objeto (Metros): "))
        tiemp = float(input("Ingresa el timepo que tarda el objeto (Segundos): "))
        Veloc =  distan / tiemp 
        #Validamos que la distancia y el tiempo no sean negativos ya que tiempo y distancia negativos no existen
        if tiemp < 0 or distan < 0 :
            print("La velocidad o distancia no pueden ser negativas favor de verificarlos")
            Enter = input("Presione Enter para continuar.")
        else :
            print("La velocidad en la que se desplaza el objeto es de ", Veloc, " m/s")
            Enter = input("Presione Enter para continuar.")
    except:
        print("Ingresa valores numéricos válidos")
        Enter = input("Presione Enter para continuar.")
#En seguida se muestra la parte de para sacar el Tiempo en el que un objeto se desplaza del apartado de física
def Tiempo() :
    distan = 0
    tiemp = 0
    Veloc = 0
    try :
        distan = float(input("Ingresa la distancia en la que se encuentar el objeto (Metros): "))
        Veloc = float(input("Ingresa la velocidad a la que va el objeto (m/s): "))
        tiemp = distan / Veloc
        #Hacemos lo mismo de validar
        if distan < 0 or Veloc < 0 :
            print("La velocidad o distancia no pueden ser negativas favor de verificarlos")
            Enter = input("Presione Enter para continuar.")
        else :
            print("El tiempo en el que se desplaza el objeto es de ", tiemp, " segundos")
            Enter = input("Presione Enter para continuar.")
    except :
        print("Ingresa valores numéricos válidos")
        Enter = input("Presione Enter para continuar.")
#Ahora sigue la fórmula para sacar la distancia de un objeto del apartado de física
def Distancia () :
    distan=0
    tiemp=0
    veloc=0
    try:
        tiemp = float(input("Ingrea el tiempo que tarda el objeto (Segundos): "))
        veloc = float(input("Ingresa la velocidad en la que se mueve el objeto (m/s): "))
        distan = tiemp * veloc
        if tiemp<0 or veloc<0 :
            print("Error el tiempo o la velocidad no pueden ser negativos favor de verificarlo")
            Enter = input("Presione Enter para continuar.")
        else : 
            print("La distancia en la que se encuentra el objeto es de ", distan," Metros" )
            Enter = input("Presione Enter para continuar.")
    except :
        print("Ingresa valores numéricos válidos")
        Enter = input("Presione Enter para continuar.")
#Funcion prueba###########################################################################################################################3


