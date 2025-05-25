# Create some example frozensets
frozen_set1: frozenset = frozenset([1, 2, 3, 4])
frozen_set2: frozenset = frozenset([3, 4, 5, 6])
frozen_set3: frozenset = frozenset([1, 2])

print(f"frozen_set1: {frozen_set1}")
print(f"frozen_set2: {frozen_set2}")
print(f"frozen_set3: {frozen_set3}")
print("\n----------\n")
# Methods that work with frozensets (since they are immutable)
# These methods return a new frozenset or a boolean value

# 1. difference(): Returns a new frozenset with elements present in the first frozenset but not in the second.
difference_set: frozenset = frozen_set1.difference(frozen_set2)
print(f"difference(): {difference_set}")  # Output: frozenset({1, 2})

# 2. intersection(): Returns a new frozenset containing only elements common to both frozensets.
intersection_set: frozenset = frozen_set1.intersection(frozen_set2)
print(f"intersection(): {intersection_set}")  # Output: frozenset({3, 4})

# 3. union(): Returns a new frozenset containing all unique elements from both frozensets.
union_set: frozenset = frozen_set1.union(frozen_set2)
print(f"union(): {union_set}")  # Output: frozenset({1, 2, 3, 4, 5, 6})

# 4. symmetric_difference(): Returns a new frozenset with elements that are in either of the sets but not in both.
symmetric_difference_set: frozenset = frozen_set1.symmetric_difference(frozen_set2)
print(f"symmetric_difference(): {symmetric_difference_set}")  # Output: frozenset({1, 2, 5, 6})

# 5. isdisjoint(): Returns True if the two frozensets have no elements in common; otherwise, False.
print(f"isdisjoint(): {frozen_set1.isdisjoint(frozen_set2)}")  # Output: False
print(f"isdisjoint(): {frozen_set1.isdisjoint(frozenset([7, 8]))}")  # Output: True

# 6. issubset(): Returns True if all elements of the first frozenset are present in the second frozenset.
print(f"issubset(): {frozen_set3.issubset(frozen_set1)}")  # Output: True
print(f"issubset(): {frozen_set1.issubset(frozen_set3)}")  # Output: False

# 7. issuperset(): Returns True if all elements of the second frozenset are present in the first frozenset.
print(f"issuperset(): {frozen_set1.issuperset(frozen_set3)}")  # Output: True
print(f"issuperset(): {frozen_set3.issuperset(frozen_set1)}")  # Output: False

# 8. copy(): Returns a new frozenset that is a shallow copy of the original.
copy_set: frozenset = frozen_set1.copy()
print(f"copy(): {copy_set}")  # Output: frozenset({1, 2, 3, 4})
print(f"copy() is same object?: {copy_set is frozen_set1}") # Output: True because frozensets are immutable
