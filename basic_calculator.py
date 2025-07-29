num1= int(input("Enter the first number : "))
num2 = int(input("Enter the second number : "))
operator = input("Choose an operation(+, -, *, /) : ")

if operator == "+":
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif operator == "-":
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif operator == "*":
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
elif operator == "/":
    if num2 != 0:
        result = num1 / num2
        print(f"{num1} - {num2} = {result}")
    else:
        print("Division by zero is not allowed.")
else:
    print("You entered invalid input. Please choose from the operation list.")
