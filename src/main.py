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

def ask_user_input():
        global operand1, operator, operand2
        # Get first operand from the user
        operand1 = float(input("Enter the first operand: "))

        # Get the operator from the user
        operator = input("Enter an operator (+, -, *, /): ")

        # Get second operand from the user
        operand2 = float(input("Enter the second operand: "))
def calculate(op1,ope,op2):
    #Perform the operation based on the operator
    global result
    match operator:
        case '+':
            result = operand1 + operand2
        case '-':
            result = operand1 - operand2
        case '*':
            result = operand1 * operand2
        case '/':
            if operand2 == 0:
                print("Error: Division by zero is undefined.")
                return
            result = operand1 / operand2
        case _:
            print("Invalid operator.")
            return result





# Call the main function to run the program
main()