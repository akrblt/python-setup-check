# calculatrice.py
# autour: ahmet krblt
# date : 07.11.2024
# version : 0.1
# calculatrice base , 4 operation


def addition (x,y):
    return x+y

def subtraction(x,y):
    return x-y

def multiplication(x,y):
    return x*y

def division(x,y):
    if y==0:
        print("division by zero set impossible. Vous pouvez saisir different numéro." )
    else:
        return x/y




print("List operation : \n 1: Addition  \n 2: Divise \n 3:multiple \n 4:soustraction  \n pour QUITTER : Q ")

while True:
    operation=input("Saisir operation. Vous pouvez trouver le list d'operation en haut: ")
    num1=int(input("saisir le numero 1 : "))
    num2=int(input("Saisir le numero 2 : "))

    match operation:
        case "1":
            addition(num1,num2)
            print(f" operation: Addition  {num1} + {num2} = {addition(num1,num2)} ")
        case "2":
            print(f" operation: Divise  {num1} / {num2} = {division(num1,num2)} ")
        case "3":
            print(f" operation: Multiple  {num1} * {num2} = {subtraction(num1,num2)} ")
        case "4":
            print(f" operation: Soustraction  {num1} - {num2} = {subtraction(num1,num2)} ")
        case "Q" :
            print(" -------------------QUITTER -------------------")
            quit()


print("------------------------------------")

main()