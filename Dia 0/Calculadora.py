#lybrarys
import os
#definition of variables
opcion = True
operacion = 0
numero1, numero2 = 0,0
continuar = 'S'

#function to calculate the operation
def calculo(operacion, numero1, numero2):
        match operacion:
            case 1:
                return numero1+numero2
            case 2:
                return numero1-numero2
            case 3: 
                return numero1*numero2
            case 4:
                if(numero2 != 0):
                    return numero1/numero2
                else:
                    return print("No es posible dividir entre 0")
            case _:
                    return print("Ni idea como llegaste aqui, pero XD")     
                    
#function to clean the console after each operation
def limpiarConsola():
    os.system("cls")

#while opcion is true, the calculator will continue running
while(opcion == True):
    print("Calculadora \n")
    print("1-Suma")
    print("2-Resta")
    print("3-Multiplicacion")
    print("4-Division")
    operacion =  int(input("Digite la operacion que desea realizar: "))
    numero1 = int(input("Ingrese el primer numero: "))
    numero2 = int(input("Ingrese el segundo numero: "))
    print(calculo(operacion, numero1, numero2))
    
  #Ask if the user wantas continue
    continuar = input(("Desea continuar? [S/N]")).capitalize()
    
    if(continuar == 'S'): #if the user wants to continue
        opcion = True
        limpiarConsola()
    elif continuar == 'N': #if the user wants to finish
        opcion = False
    elif continuar != 'S' and continuar != 'N':
        print("Opcion no valida")
        opcion = False    
