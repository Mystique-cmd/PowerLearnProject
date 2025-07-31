#This is a basic calculator
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y  
  
def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    return x / y 
   
def calculator(x, y, operation):
    if operation == '+':
        return add(x, y)
    elif operation == '-':
        return subtract(x, y)
    elif operation == '*':
        return multiply(x, y)
    elif operation == '/':
        return divide(x, y)
    else:
        raise ValueError("Invalid operation. Choose from: +, -, /, *.")
        
input_x = float(input("Enter first number: "))
input_y = float(input("Enter second number: "))
input_operation = input("Enter operation (+, -, /, *): ")
result = calculator(input_x, input_y, input_operation)
print(f"{input_x} {input_operation} {input_y} = {result}")
# End of basic_calculator.py