# # #  A dictionary is a collection of key-value pairs. It is:
# # #unorderd mutable and un-indexed

# person: dict = {
#     "name": "DUA",
#     "age": 25,
#     "city": "karachi"
# }
# print(person)

# # #  Accessing Values -------------------------
# # print(person.get("area" ,"abc"))
# # print(person["name"])  # Output: Alice
# # print(person.get("age", "99"))  # Output: 25, if not found it will return 99 (default value)

# # # Access a non-existent key
# # print(person.get("country", "my_default_vlaue_if_key_not_found"))  # Output: my_default_vlaue (default value)

# # # Modifying a Dictionary --------------

# # person["age"]= 20
# # print(person)

# # person["email"]="abcb@gamil.com"
# # print(person.keys())

# # #  Deleting Items -----------------------------
# # del person["age"]
# # print(person)


# age: int = person.pop("age", -1)
# print("Removed age:", age)
# print(person)


# name:str = person.pop("name", -1)
# print("remover name:", name)
# print(person)
# print("\n-----\n")
# # Again remove a key which is already removed to check the default value
# age: int = person.pop("age", -1)
# print("key 'age' not found in dict so returning default value: ", age)

# # --------------------------------------

# # Get all keys
# print("person.keys()         = ", person.keys()  )  # Output: dict_keys(['name', 'email', 'city', 'age'])

# # Get all values
# print("person.values()       = ", person.values())  # Output: dict_values(['Alice', 'alice@example.com', 'Los Angeles', 27])

# # Get all key-value pairs
# print("person.items()        = ", person.items())  # Output: dict_items([('name', 'Alice'),


# # Update the dictionary
# person.update({"city": "Los Angeles", "age": 27})
# print("After: person.update  = ", person)

# # Clear the dictionary
# person.clear()
# print("After: person.clear() = ", person)  # Output: {}
# -----------------------------------------------------------------------------
person :dict ={
    "name" : "iqra",
    "age" : 20,
    "city" : "karachi"
}
print(person)

person["age"] = 30
print(person)

del person["age"]
print(person)


# # . Dictionary Methods

print("person key " ,person.keys())
print("person value", person.values())
print("person items", person.items())
person.update({"name" : "sadaf", "city" : "lahore"})
print(person)
person.clear()
print(person)

for key, value in person.items():
    print(key," : ", value)



# Duplicate Key Not Allowed

thisdict: dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020 # this will overwrite the previous key:vlaue
}
print(thisdict)

#  Iterating Over a Dictionary

for key in thisdict:
    print(key)

for key , value in thisdict.items():
    print(key, " : " , value)