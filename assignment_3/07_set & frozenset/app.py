my_set: set = {123, 452, 5, 6}
my_set2: set = set([123, 452, 5, 6])
unknown: set = {} # set or dectionary
empty_set: set = set()

print("my_set            = ", my_set)
print("my_set2           = ", my_set2)
print("type(my_set)      = ", type(my_set))
print("type(my_set2)     = ", type(my_set2))
print("type(unknown)     = ", type(unknown))
print("type(empty_set)   = ", type(empty_set))
print("my_set == my_set2 = ", my_set == my_set2)


# --------------------------------------------------

my_set: set = {1, 2, 3, 4, 5, 'A', 'a'}
print(my_set)
# Remove an item
my_set.remove(3)
my_set.remove('A')
print(my_set) 

# -------------------------------------------------

my_set.add(6)
print(my_set)  # Output: {1, 2, 4, 5, 6}
# ------------------------------------------------

my_set: set = {1, 2, 3, 4, 5, 'A', 'a'}
print("my_set = ", my_set)

# discard() only removes a single element.
# {1, 2, 3} is a set itself, not an element within my_set.
# Therefore, discard does not find it and returns None, without modifying the set.
print(my_set.discard({1,2,3}))

print("After: my_set = ", my_set) # return None

# To remove multiple elements, iterate and discard each one individually:
for item in {1, 2, 3}:
    my_set.discard(item)

print("After removing multiple elements: my_set = ", my_set)