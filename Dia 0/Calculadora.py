import os
#Seccion para definiar las variables

opcion = True
operacion = 0
numero1, numero2 = 0,0
continuar = 'S'

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
                    
#Metodo para limpiar la consola
def limpiarConsola():
    os.system("cls")

#Seccion de las operaciones
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
    
  
    continuar = input(("Desea continuar? [S/N]")).capitalize()
    
    print(continuar)
    if(continuar == 'S'):
        opcion = True
        limpiarConsola()
    elif continuar == 'N':
        opcion = False
    elif continuar != 'S' and continuar != 'N':
        print("Opcion no valida")
        opcion = False    
