# fruits : str = ["apple", "banana", "cherry", "date", "elderberry"]

# for fruit in fruits:
#     print(fruits[fruits.index(fruit)])


# numbers = [1, 2, 3, 4, 5]

# for num in numbers:
#     if num == 10:
#         print("Number mil gaya!")
#         break
# else:
#     print("Number nahi mila.")


# numbers = [1,2,3,4,5,6,7]

# for num in numbers :
#     if num == 7:
#         print("number is found")
#         break
# else:
#     print("number is not found")


# for i in range(10):
#     print(i)

# for i in range(1, 10):
#     print(i)

# for i in range(1, 10, 2):
#     print(i)

#     thorwaway variable

# for _ in range(5):
#     print("good work")

# for i in range(5):
#     print(f"{i + 1} good work")

# for i in range(10):
#     if i  == 5:
#         continue
#     print(i)


# for i in range(10):
#     if i == 5:
#         break
#     print(i)

# for i in range(1, 3):          # Outer loop
#     for j in range(1, 4):      # Inner loop
#         print(i, j)



# for i in range(1,4):
#     for j in range(1 ,5):
#         print(i , j)


for outer in range(1, 6): # outer loop
    print(f"Multiplication table for {outer}:")
    for inner in range(1, 6): # nested inner loop
        print(f"{outer} * {inner} = {outer * inner}")
    print()  # Add a blank line after each row