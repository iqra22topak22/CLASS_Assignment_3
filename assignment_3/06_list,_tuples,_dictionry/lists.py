# # fruits_name : str = ["apple", "banana","orange"]
# # print(fruits_name)
# # print(fruits_name[1])    #output banana

# # numbers :int = [1,2,3,4,5]
# # print(numbers)
# # print[numbers[-2]]  #output 4

# # mixed : list = [1, " dua" , "sky"]
# # print(mixed)

# # fruits_name : str = ["apple", "banana","orange", "mango", "kiwi"]

# # print(fruits_name[1:3])


# # Common List Methods
 
# # last me 1 element add krna (append) 
 
# fruits_name : str = ["apple", "banana","orange", "mango", "kiwi"]
# fruits_name.append("watermelon")
# print(fruits_name)
# # +++++++++++++++++++++++++++++++++++++++++++++++++

# # list me 1 sy zad element add krna   (extend)
# fruits_name : str = ["apple", "banana","orange", "mango"]

# fruits_name.extend(["grape", "kiwi"]) 
# print(fruits_name) 

# # ===================================/
# #  1 element remove krna (remove)

# fruits_name : str = ["apple", "banana","orange", "mango", "kiwi"]
# fruits_name.remove("banana")
# print(fruits_name)

# # -------------------------------

# # pop([index]) – Item ko index se remove karta hai (default last item)

# fruits_name : str = ["apple", "banana","orange", "mango", "kiwi"]
# fruits_name.pop(2)
# print(fruits_name)

# # --------------------------------------------

# # clear() – Puri list ko empty kar deta hai

# fruits_name : str = ["apple", "banana","orange", "mango", "kiwi"]
# fruits_name.clear()
# print(fruits_name)

# # ------------------------------------------------
# # index(item) – Item ka index return karta hai (first occurrence)

# fruits_name : str = ["apple", "banana","orange", "mango", "kiwi"]
# print(fruits_name.index("mango"))

# # ----------------------------------------------
# # count(item) – Item kitni baar aya hai, ye batata hai

# fruits_name : str = ["mango","apple", "banana","mango","orange", "mango", "kiwi", "mango"]
# print(fruits_name.count("mango"))


# # sort() – List ko sort karta hai (ascending by default)

# fruits_name : str = ["apple", "banana","orange", "mango", "kiwi"]
# fruits_name.sort()
# print(fruits_name)

# # ==============================================
# # reverse() – List ko ulta kar deta hai 

# fruits_name : str = ["apple", "banana","orange", "mango", "kiwi"]
# fruits_name.reverse()
# print(fruits_name)

# # ============================================
# # copy() – List ka shallow copy banata hai

# fruits_name : str = ["apple", "banana","orange", "mango", "kiwi"]
# fruits_name.copy()
# print(fruits_name)

# # ==================================== sort key len
# # ya items ki leangth se sort karta hai
# fruits_name : str = ["apple", "banana","orange", "mango", "kiwi"]
# fruits_name.sort(key=len)
# print(fruits_name)


#  Iterating Over Lists

# fruits_name: list[str] = ["apple", "banana", "orange", "mango", "kiwi"]

# for fruit in fruits_name:
#     print(f"{fruit} ({len(fruit)} letters)")


# =================================================

# Using list comprehension
# Python mein list comprehension ek shortcut hota hai nayi list banane ka.
# Yeh tareeqa asaan aur readable hota hai — yani chhoti line mein kaam ho jaata hai.

# # new_list = [expression for element in iterable if condition]

# new_list = [number **2 for number in [1,2,3,4,5,6] if number % 2 == 0]
# print(new_list)

# # odd
# new_list_oddnum = [num for num in [1,2,3,4,5,6,]if num % 2!=0]
# print(new_list_oddnum)
    
# squre = [ num ** 2 for num in [1,2,3,4,5,6,7] if num > 4]
# print(squre)


vowels = [ch for ch in "programming" if ch in "aeiou"]
print(vowels)
# Output: ['o', 'a', 'i'

name = [name1 for name1 in "iqramushtaq" if name1 not in "iqra"]
print(name)

