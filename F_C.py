f_c = input("Are you in F or C? ")

if f_c == "F":
    f = float(input("What is the temperature in Fahrenheit? "))
    print(f"The temperature in Celsius is: {(f - 32) * 5/9:.2f}°C")
elif f_c == "C":
    c = float(input("What is the temperature in Celsius? "))
    print(f"The temperature in Fahrenheit is: {c * 9/5 + 32:.2f}°F")
else:
    print("Invalid input. Please enter 'F' for Fahrenheit or 'C' for Celsius.")