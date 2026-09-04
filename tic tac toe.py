user_operation = str(input("Enter the operation you want to perform (add, sub, div, multiply, expo): "))

if user_operation == "add":
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = num1 + num2
    print(f"The result of adding {num1} and {num2} is: {result}")
elif user_operation == "sub":
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = num1 - num2
    print(f"The result of subtracting {num2} from {num1} is: {result}")
elif user_operation == "div":
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    if num2 == 0:
        print("Error: Division by zero is not allowed.")
    else:
        result = num1 / num2
        print(f"The result of dividing {num1} by {num2} is: {result}")
elif user_operation == "multiply":
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = num1 * num2
    print(f"The result of multiplying {num1} and {num2} is: {result}")
elif user_operation == "expo":
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = num1 ** num2
    print(f"The result of raising {num1} to the power of {num2} is: {result}")