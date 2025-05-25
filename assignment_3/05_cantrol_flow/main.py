
# simple calculator

sum : str = input("enter the operator : , + ,- , * , / : " )
num1 = float(input("Enter the first number : "))
num2 = float(input("enter the second number :"))

if sum == "+":
    result = num1 + num2
elif sum == "-":
    result = num1 - num2
elif sum == "*":
    result = num1 * num2
elif sum == "/":
    if num2 != 0:
        result = num1 /  num2
else:
    result = "Error : division by zero"

print("Result : ", result)