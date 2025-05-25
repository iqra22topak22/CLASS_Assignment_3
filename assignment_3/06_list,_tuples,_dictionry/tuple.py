# 4. Tuples in Python 

# A tuple is a collection which is ordered and unchangeable.

tuples : tuple = ("apple", "banana", "cherry")
print(tuples)
num : tuple = (1,2,3,4)
print(num)

# Comparison | Kya check kar raha hai? | Result
# tuple_1 == tuple_2 | Kya values same hain? | ✅ True
# tuple_1 is tuple_2 | Kya memory location same hai? | ❌ False

tuple_1 = (1, 2, 3, 4, 5)
tuple_2 = (1, 2, 3, 4, 5)

print("tuple_1 id is " ,id(tuple_1))
print("tuple_1 id is " ,id(tuple_2))

# ---------------------------------------------------------------
#  Tuples in Python

# A tuple is an `ordered`, `immutable` (unchangeable) sequence of elements.
# Tuples are useful for fixed data collections.

# Creating a Tuple
tuple1: tuple      = tuple(["apple", "banana", "cherry"])  # cast a list into tuple
tuple2: tuple      = (10, 20, 30)  # tuple
mixed_tuple: tuple = ("hello", 42, 3.14, True)  # tuple

print("tuple1      =", tuple1)
print("tuple2      =", tuple2)
print("mixed_tuple =", mixed_tuple)

# Accessing elements in a tuple
print("tuple1[0] =", tuple1[0])  # Accessing first element

# # Tuple slicing
print("tuple2[1:] =", tuple2[1:])  # Slicing from index 1

# # Tuple length
print("Length of tuple1:", len(tuple1))

# # Iterating through a tuple
print("Iterating through tuple2:")
for item in tuple2:
  print(item)

# # Checking if an item exists in a tuple
print("Is 20 in tuple2?", 50 in tuple2)

# # Concatenating tuples
tuple3: tuple = tuple1 + tuple2
print("tuple1 + tuple2 =", tuple3)

# # Repeating tuples
tuple4: tuple = tuple2 * 2
print("tuple2 * 2 =", tuple4)

# # Nested tuples
nested_tuple = (tuple1, tuple2)
print("nested_tuple =", nested_tuple)

# Unpacking tuples
# "Unpacking" ka matlab hota hai ke tuple ke andar jo values hain, unko alag alag variables mein ek saath assign karna.


a, b, c = tuple1
print("Unpacking tuple1:", a, b, c)

# Using tuples as keys in dictionaries (because they are immutable)
my_dict = {tuple1: "This is a tuple key", tuple2: "Another tuple key"}
print("Dictionary with tuple keys:", my_dict)
