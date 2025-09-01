import math

def calculator():
    print("Welcome to a mini Scientific Calculator!")
    print("Type 'q' to quit.\n")

    while True:
        operation = input("Enter operation (+, -, *, /, ^, sqrt, sin, cos, tan, log, !, abs): ").strip()

        if operation == 'q':
            print("Goodbye!")
            break

        # Double-number operations
        if operation in ['+', '-', '*', '/', '^']:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter valid numbers.\n")
                continue

            if operation == '+':
                result = num1 + num2
            elif operation == '-':
                result = num1 - num2
            elif operation == '*':
                result = num1 * num2
            elif operation == '/':
                if num2 == 0:
                    print("Error: Division by zero.\n")
                    continue
                result = num1 / num2
            elif operation == '^':
                result = num1 ** num2

            print("Result:", result, "\n")
            continue

        # Single-number operations
        single_ops = ['sqrt', 'sin', 'cos', 'tan', 'log', '!', 'abs']

        if operation in single_ops:
            try:
                num = float(input("Enter number: "))
            except ValueError:
                print("Invalid input. Please enter a valid number.\n")
                continue

            if operation == 'sqrt':
                if num < 0:
                    print("Error: Cannot compute square root of a negative number.\n")
                    continue
                result = math.sqrt(num)
            elif operation == 'sin':
                result = math.sin(math.radians(num))
            elif operation == 'cos':
                result = math.cos(math.radians(num))
            elif operation == 'tan':
                result = math.tan(math.radians(num))
            elif operation == 'log':
                if num <= 0:
                    print("Error: Logarithm undefined for non-positive numbers.\n")
                    continue
                result = math.log10(num)
            elif operation == '!':
                if num < 0 or int(num) != num:
                    print("Error: Factorial only defined for non-negative integers.\n")
                    continue
                result = math.factorial(int(num))
            elif operation == 'abs':
                result = abs(num)

            print("Result:", result, "\n")
            continue

        print("Invalid operation. Please try again.\n")

calculator()
# Scientific Calculatr