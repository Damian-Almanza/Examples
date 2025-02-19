operation = input("Enter your operation (+ - * /) ")
num1= float(input("Enter your first number: "))
num2 = float(input("Enter your second number: "))

if operation == "+":
    print(round((num1 + num2) ,2))

elif operation == "-":
    print(round((num1 - num2), 2))

elif operation == "*":
    print(round((num1 * num2),2))

elif operation == "/":
    print(round((num1 / num2),2))
else:    
    print("Invalid operation")  