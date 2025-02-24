# Add
def add(n1, n2):
    return n1 + n2

# Subtract
def subtract(n1, n2):
    return n1 - n2

# Multiply
def multiply(n1, n2):
    return n1 * n2

# Divide
def divide(n1, n2):
    return n1 / n2

operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}
def calculator():
    loop_continue = 'y'
    num1 = float(input("What's the first number?: ")) 
    for operand in operations:
        print(operand)
        
    while loop_continue == 'y': 
        
        operation_symbol = input("Pick an operation: ")

        num2 = float(input("What's the next number?: ")) 

        calculation_function = operations[operation_symbol]
        answer = calculation_function(n1 = num1, n2 = num2) 
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        num1 = answer
        loop_continue = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation.: ")
        if loop_continue == 'n':
            loop_continue = 'n'
            calculator()
        
calculator()