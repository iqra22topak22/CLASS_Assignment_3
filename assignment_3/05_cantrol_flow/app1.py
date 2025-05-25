def grade_system(marks):
  if marks>= 90:
    grade = "A+"
  elif marks >=80:
    grade = "A"
  elif marks >= 70:
    grade = "B"
  elif marks >= 60:
    grade = "C"
  elif marks >= 50:
    grade = "D"
  else:
    grade = "F"
 
  return grade
  
while True:
  try:
    marks = float(input("Enter the marks:"))
    if 0 <= marks <=100:
      break
    else:
      print("marks must be bewteen 0 and 100.")
  except ValueError:
      print("Invalid input. Please enter a number.")

grade = grade_system(marks)
print(f"the grade for {marks} marks is : {grade}")

# # #    ================================================================ 
# def grading_system(marks):
#   """
#   This function takes marks as input and returns the corresponding grade.

#   Args:
#     marks: The marks obtained by the student.

#   Returns:
#     The grade corresponding to the marks.
#   """
#   if marks >= 90:
#     grade = "A+"
#   elif marks >= 80:
#     grade = "A"
#   elif marks >= 70:
#     grade = "B"
#   elif marks >= 60:
#     grade = "C"
#   elif marks >= 50:
#     grade = "D"
#   else:
#     grade = "F"
#   return grade

# # Get marks as input from the user
# while True:
#   try:
#     marks = float(input("Enter the marks: "))
#     if 0 <= marks <= 100:
#       break
#     else:
#       print("Marks must be between 0 and 100.")
#   except ValueError:
#     print("Invalid input. Please enter a number.")

# # Determine the grade
# grade = grading_system(marks)

# # Print the grade
# print(f"The grade for {marks} marks is: {grade}")

# # ********************************************


# Python match-case Statement

def check_status(code):
    match code:
        case 200:
            print("OK")
        case 400:
            print("Bad Request")
        case 404:
            print("Not Found")
        case _:
            print("Unknown Status")

check_status(200)  # Output: OK
check_status(404)  # Output: Not Found
check_status(500)  # Output: Unknown Status

