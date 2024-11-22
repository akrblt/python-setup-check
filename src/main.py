operator=None
operand1=None
operand2=None
result = None
      #Get the operator from the user

def main():
    ask_user_input()
    global result
    result = calculate(operand1,operator,operand2)
    #print the result
    print("Result:", result)
    display_result(operand1,operator,operand2,result)

def ask_user_input():
        global operand1, operator, operand2
        # Get first operand from the user
        operand1 = float(input("Enter the first operand: "))

        # Get the operator from the user
        operator = input("Enter an operator (+, -, *, /): ")

        # Get second operand from the user
        operand2 = float(input("Enter the second operand: "))
def calculate(ope1,oper,ope2):
    #Perform the operation based on the operator
    res =None
    match oper:
        case '+':
            res = ope1 + ope2
        case '-':
            res = ope1 - ope2
        case '*':
            res = ope1 * ope2
        case '/':
            if ope2 == 0:
                print("Error: Division by zero is undefined.")
                return
            res = ope1 / ope2
        case _:
            print("Invalid operator.")
    return res

def display_result(op1,ope,op2,res):
    print(f" {op1} {ope} {op2} = {res}")





# Call the main function to run the program
main()