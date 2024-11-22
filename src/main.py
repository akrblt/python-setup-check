operator=None
operand1=None
operand2=None
      #Get the operator from the user

def main():
    ask_user_input();

    #Perform the operation based on the operator
    # Perform the operation based on the operator
    if operator == '+':
        result = operand1 + operand2
    elif operator == '-':
        result = operand1 - operand2
    elif operator == '*':
        result = operand1 * operand2
    elif operator == '/':
        if operand2 == 0:
            print("Error: Division by zero is undefined.")
            return
        result = operand1 / operand2
    else:
        print("Invalid operator.")
        return
    print("Result:", result)





def ask_user_input():
    global operand1,operator,operand2
    # Get first operand from the user
    operand1 = float(input("Enter the first operand: "))

    # Get the operator from the user
    operator = input("Enter an operator (+, -, *, /): ")

    # Get second operand from the user
    operand2 = float(input("Enter the second operand: "))





# Call the main function to run the program
main()