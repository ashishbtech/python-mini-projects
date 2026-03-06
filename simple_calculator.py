operator = input("Enter or choose an operator (+ - * / %): ")
num1 = float(input("Enter the 1st number: "))
num2 = float(input("Enter the 2nd number: "))

if operator == "+":
    result = num1 + num2

elif operator == "-":
    result = num1 - num2

elif operator == "*":
    result = num1 * num2

elif operator == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        print("Error: Division by zero is not allowed.")
        exit()

elif operator == "%":
    result = num1 % num2

else:
    print("Invalid operator!")
    exit()

print("Result:", result)