# Prueba

from os import system
import statistics
#Funciones importadas del archivo de Funciones
from Funciones import Capital,Pasivo,Activo,Velocidad,Tiempo,Distancia
from FuncionesMenu import Contaduria,Fisica
# No le muevas de aqui hasta la linea 160

try:
    mainMenu=True
    while mainMenu==True:
        ## Orden y limpieza
        system("cls")
        ## Aquí asignamos las opciones del menú y se solicita la opción a elegir
        print("1) Calculo de intereses.\n"+
        "2) Probabilidad y estadistica.\n"+
        "3) Conversor de programador.\n"
        "4) Contaduría\n"+
        "5) Física\n"+
        "6) Salir")
        opMenuPrin=int(input("Selecciona una opción: "))
        try:
            match opMenuPrin:
#################################################################################################################3
                case 1:
                    def calcular_pago(saldo_inicial, tasa_interes_mensual, num_meses):
                        saldo_final = saldo_inicial * (1 + tasa_interes_mensual) ** num_meses
                        return saldo_final

                    saldo_inicial = float(input("Por favor, ingresa el saldo inicial: "))  # Saldo inicial
                    tasa_interes_mensual = float(input("Por favor, ingresa la tasa de interés mensual (como decimal, por ejemplo, 0.05 para 5%): "))  # Tasa de interés mensual
                    num_meses = float(input("Por favor, ingresa el número de meses: "))  # Número de meses

                    saldo_final = calcular_pago(saldo_inicial, tasa_interes_mensual, num_meses)
                    diferencia = saldo_final - saldo_inicial
                    print(f"El monto que tendrías que pagar después de {num_meses} meses es: {saldo_final}")
                    print("estarías pagando ", diferencia , " de intereses.")

                    Enter =input("Enter para continuar. ")

##########################################################################################################################################
                case 2:
                    try:
                        system("cls")
                        listaProb=[]
                        cicloWhileMenuProb=True
                        while cicloWhileMenuProb==True:
                            ## Variable para poder hacer todas las operaciones que el usuario quiera
                            ## y pueda volver al menú a voluntad gracias a un ciclo.
                            cicloWhileProbOps=True
                            # Usamos una lista para que el usuario pueda ingresar todos los datos que deseé
                            if len(listaProb)==0:
                                print("PROBABILIDAD Y ESTADISTICA")
                                print("Generemos una lista que contenga los datos a evaluar:")
                                valor=int(input("Ingrese el primer dato: "))
                                while valor !=0:
                                    listaProb.append(valor)
                                    valor=int(input("Ingrese otro dato (Presione 0 para terminar de agregar valores): "))
                                ## Imprimimos los valores
                                system("cls")
                                print("Su lista queda de la siguiente forma: ")
                                listaProb.sort()                                
                                print(listaProb)
                                longitud=int(len(listaProb))
                                print("Con una longitud de :",longitud ," valores")
                                Enter=input("Presione cualquier tecla para continuar")
                            else:
                                # Le damos un ciclo al menú para que el usuario pueda hacer las operaciones que deseé -
                                # con la misma lista, o pueda cambiarla                             
                                while cicloWhileProbOps==True:
                                    
                                    ## Aquí borramos la consola para darle orden y limpieza al programa, lo haremos en cada caso
                                    system("cls")
                                    print("PROBABILIDAD Y ESTADISTICA:")
                                    print("\n¿Qué operación te gustaría realizar?\n"+
                                    "1) Media.\n"+
                                    "2) Mediana.\n"+
                                    "3) Desviación estándar.\n"+
                                    "4) Cambiar de lista.\n"+
                                    "5) Salir al menú principal.")
                                    opProbBasi=int(input("Selecciona una opción: "))

                                    match opProbBasi:
                                        #Solicitar numeros y realizar operaciones
                                        case 1:
                                            # Media
                                            system("cls")                                    
                                            media = statistics.mean(listaProb)
                                            print("La media es: ", media)
                                            Enter=input("Presione enter para continuar: ")
                                            system("cls")
                                        case 2:
                                            # Mediana
                                            system("cls")
                                            mediana= statistics.median(listaProb)
                                            print("La mediana es: ", mediana)
                                            Enter=input("Presione Enter para continuar.")
                                            system("cls")                                    
                                        case 3:
                                            system("cls")
                                            Desviacion=statistics.stdev(listaProb)
                                            print("La desviación estandar es: ", Desviacion)
                                            Enter=input("Presione Enter para continuar.")
                                            system("cls")
                                        case 4:
                                            print("Volviendo a agregar nueva lista.")
                                            cicloWhileProbOps=False
                                            listaProb= []
                                        case 5:
                                            print("Volviendo al menú principal.")
                                            cicloWhileProbOps=False
                                            cicloWhileMenuProb=False
                                        case _:
                                            print("Selecciona una opción valida")
                    except:
                        print("Error lista Probabilidad")
###########################################################################################################################################
                case 3:
                    system("cls")
                    cicloWhileConvCant=True
                    while cicloWhileConvCant==True:
                        system("cls")
                        numOgConv=0
                        numConvertido=0
                        print("CONVERSOR DE CANTIDADES.\n"+
                        "1) Decimal a binario\n"+
                        "2) Decimal a Hexadecimal\n"+
                        "3) Decimal a Octal\n"+
                        "4) Salir\n"+
                        "(Más conversiones en camino :P)\n")
                        SelConvCant=int(input("Selecciona una opción: "))
                        match SelConvCant:
                            case 1:
                                system("cls")
                                print("DECIMAL --> BINARIO")
                                numOgConv=int(input("Ingresa la cantidad a convertir: "))
                                numConvertido=bin(numOgConv)
                                print("El número ", numOgConv , " en binario es: ", numConvertido,"\n")
                                Enter= input("Presione Enter para continuar.")
                            case 2:
                                system("cls")
                                print("DECIMAL --> HEXADECIMAL")
                                numOgConv=int(input("Ingresa la cantidad a convertir: "))
                                numConvertido=hex(numOgConv)
                                print("El número ", numOgConv , " en hexadecimal es: ", numConvertido,"\n")
                                Enter= input("Presione Enter para continuar.")
                            case 3:
                                system("cls")
                                print("DECIMAL --> OCTAL")
                                numOgConv=int(input("Ingresa la cantidad a convertir: "))
                                numConvertido=oct(numOgConv)
                                print("El número ", numOgConv , " en octal es: ", numConvertido,"\n")
                                Enter= input("Presione Enter para continuar.")
                            case 4:
                                print("Regresando al menú principal...")
                                cicloWhileConvCant=False
                            case _:
                                print("Selecciona una opción valida")
                                system("cls")

#######################################################################################################################################################################################
                case 4:
                    #En el caso 4 vamos a entra en el menú del apartado de Contaduría 
                    system ("cls")
                    """
                    Se usa un while True en todas las operaciones para que quede ciclado y en el momento en el que
                    se quiera salir se seleccione la opción de Break (Opción 4)
                    """
                    Contaduria()

############################################################################################################################################################################3#
                case 5:
                    #Aquí entramos en el apartado de física
                    system("cls")
                    Fisica()
################################################################################################################################################################################3
                case 6:
                    ## Aquí se cierra la "sesión" y saca del ciclo para cerrar el programa.
                    system("cls")
                    print("Adiós")
                    mainMenu=False
                case _:
                    print("¡Selecciona una opción valida! \n")
        except:
            print("Error try 2")
    ## Aquí cierra el ciclo del menú principal y lanza un mensaje de despedida.
    print("¡Hasta la proxima!")
except:
    print("Error Try 1")