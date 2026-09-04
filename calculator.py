# create a calculator for addition, subtraction, multiplication, division, and exponentiation that takes two numbers as input and returns the result of the operation. The calculator should also handle invalid inputs and display an error message if the user enters a non-numeric value or tries to divide by zero.
# ask which operation the user wants to perform
inputoperation = input("Enter the operation you want to perform (add, sub, div, multiply, exp): ")
inputvariable1 = input("How many numbers do you want to input:")
# make a new code that takes in a list of numbers and performs the operation on all of them. The calculator should also handle invalid inputs and display an error message if the user enters a non-numeric value or tries to divide by zero.

if inputvariable1.isdigit():
    inputvariable1 = int(inputvariable1)
    if inputvariable1 < 2:
        print("You need to input at least two numbers.")
    else:
        numbers = []
        for i in range(inputvariable1):
            num = input(f"Enter number {i+1}: ")
            try:
                num = float(num)
                numbers.append(num)
            except ValueError:
                print("Invalid input, please enter a valid number.")
                break
        else:
            if inputoperation == "add":
                result = sum(numbers)
                print(f"The sum of the numbers is: {result}")
            elif inputoperation == "sub":
                result = numbers[0]
                for num in numbers[1:]:
                    result -= num
                print(f"The difference of the numbers is: {result}")
            elif inputoperation == "div":
                result = numbers[0]
                try:
                    for num in numbers[1:]:
                        result /= num
                    print(f"The quotient of the numbers is: {result}")
                except ZeroDivisionError:
                    print("Error: Division by zero is not allowed.")
            elif inputoperation == "multiply":
                result = 1
                for num in numbers:
                    result *= num
                print(f"The product of the numbers is: {result}")
            elif inputoperation == "exp":
                result = numbers[0]
                for num in numbers[1:]:
                    result **= num
                print(f"The result of the exponentiation is: {result}")
            else:
                print("Invalid operation. Please enter 'add', 'sub', 'div', 'multiply', or 'exp'.")