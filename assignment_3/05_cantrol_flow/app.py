    # *****cantrol flow******

# if condition:
#         statement
# elif condition:
#         statement
# else:
#         statemen
# name = "iqra"
# is_student = True
# if name == "dua" and is_student:
#     print(" your qualify for a student discount")

# elif name =="iqra" and is_student:
#     print(" your qualify for a student discount")

# else:
#     print("you are not a student")

    # *****************************************************

    # Nested if and else
num: int = 10
if num > 0: 
    if num % 2 == 0: # Modulus operator, remainder 0 = even_number,
        print("The number is positive and even.")
    else: # remainder 1 = odd_number,
        print("The number is positive and odd.")
else:
    print("The number is negative.")


# # -------------------------------------------------
# simple calculator

operation: str = input("Enter the operation (+, -, *, /): ")
num1: float = float(input("Enter the first number: "))
num2: float = float(input("Enter the second number: "))

if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error: Division by zero."
else:
    result = "Invalid operation."

print("Result:", result)