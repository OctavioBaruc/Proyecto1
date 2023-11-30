# Prueba

#Invocamos las funciones del archivo funciones
from Funciones import Capital,Pasivo,Activo,Velocidad,Tiempo,Distancia
#Definiciones de las funciones del menú (Contaduría,Física y más)
def Contaduria():
    from os import system 
    """
    Se usa un while True en todas las operaciones para que quede ciclado y en el momento en el que
    se quiera salir se seleccione la opción de Break (Opción 4)
    """
    while True :
        try :
        #Pedimos que escgoja la opción que quiera emplear
            system("cls")
            print("Ecoge que operación quieres emplear \n 1)Sacar Capital \n 2)Sacar Pasivo \n 3)Sacar Activo \n 4)Volver al menú")
            Opc_Conta = int(input("Selecciona una opción: "))
            match Opc_Conta:
                case 1 :
                #Usamos las funciones invocadas en el principio y usarlas para la operaación que el usuario quiere completar
                    system("cls")
                    Capital()
                case 2:
                #Aquí usamoa mas funciones invocada
                    system("cls")
                    Pasivo()
                case 3:
                #Otra función :)
                    system("cls")
                    Activo()
                case 4:
                    break
                case _ :
                    print("ingresa una opción válida")
                    Enter = input("Presiona enter para continuar.")
        except :
            print("Ingresa valores numéricos válidos")
            Enter = input("Presione enter para continuar")
###############################################################################################################################################3
#Definimos la función de física para usarla e el archivo principal
def Fisica () :
    from os import system
    while True :
        try :
            #Este apartado le pertenece a la materia de física donde se harán las operaciones para sacar velocidad,tiempo y distancia
            system("cls")
            print("Inserta la opción de lo que te interesa saber del objeto \n 1)Velocidad \n 2)Tiempo \n 3)Distancia \n 4)Salir al menú")
            Opc_Fis = float((input("")))
            #Despues de que el usuario escogió lo que le interesa conocer usaremos un funciones para representarlas
            match Opc_Fis:
                case 1:
                    #Una funcion para la velociad
                    system("cls")
                    Velocidad()
                case 2 :
                    #Otra función para Tiempo
                    system("cls")
                    Tiempo()
                case 3 :
                    #Otra función para Distancia :)
                    #<3
                    system("cls")
                    Distancia()
                case 4 :
                    #Usamos break para salir del while 
                    break
                case _:
                    print("ingresa una opción válida")
                    Enter = input("Presiona enter para continuar.")
        except :
            print("Ingresa valores numéricos válidos")
            Enter = input("Presione enter para continuar")