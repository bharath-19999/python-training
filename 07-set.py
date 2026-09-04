"""
=========================================================
PYTHON SETS - COMPLETE REVISION NOTES
=========================================================

1. SET BASICS
   - Set is an unordered collection of UNIQUE elements.
   - Duplicate values are automatically removed.
   - Created using {} or set().
   - Example:
       {10, 20, 30}

2. SET PROPERTIES
   - Unordered
   - Unindexed
   - Mutable
   - Does not allow duplicates
   - Can store heterogeneous elements

3. IMPORTANT
   - Set does NOT support indexing.
   - Set does NOT support slicing.
   - Order is not guaranteed.

4. CREATION
   - {10, 20, 30}
   - set()

5. EMPTY SET
   - {}      -> Empty Dictionary
   - set()   -> Empty Set

6. DUPLICATES
   - Automatically removed.
   - {10, 20, 10} -> {10, 20}

7. ADDING ELEMENTS
   - add()      -> Add one element
   - update()   -> Add multiple elements

8. REMOVING ELEMENTS
   - remove(x)  -> Removes element, ERROR if not found
   - discard(x) -> Removes element, NO ERROR if not found
   - pop()      -> Removes an arbitrary element
   - clear()    -> Removes all elements

9. SET OPERATIONS
   - union()                -> All elements
   - intersection()         -> Common elements
   - difference()           -> Elements in first but not second
   - symmetric_difference() -> Elements different in both sets

10. OPERATORS
   - | -> Union
   - & -> Intersection
   - - -> Difference
   - ^ -> Symmetric Difference

11. RELATIONSHIP METHODS
   - issubset()
   - issuperset()
   - isdisjoint()

12. MEMBERSHIP
   - in
   - not in

13. SET FUNCTIONS
   - len()

14. SET COMPREHENSION
   - {expression for element in iterable}

15. CONVERTING COLLECTIONS
   - set(list)
   - list(set)
   - tuple(set)

16. MAIN USE OF SET
   - Remove duplicates
   - Perform mathematical set operations
   - Fast membership checking

=========================================================
QUICK REMEMBER FORMULA

SET = Unordered + Unique + Mutable + Unindexed

Creation          -> {} / set()
Empty Set         -> set()
Duplicates        -> Automatically Removed

Add One           -> add()
Add Multiple      -> update()

Remove            -> remove()
Safe Remove       -> discard()
Remove Arbitrary  -> pop()
Remove All        -> clear()

Union             -> union() / |
Intersection      -> intersection() / &
Difference        -> difference() / -
Symmetric Diff    -> symmetric_difference() / ^

Subset            -> issubset() / <=
Superset          -> issuperset() / >=
Disjoint          -> isdisjoint()

Membership        -> in / not in

Comprehension     -> {expression for element in iterable}

=========================================================
COMPLETE CODE EXAMPLES
=========================================================
"""


# =========================================================
# 1. SET CREATION AND DUPLICATE REMOVAL
# =========================================================

s1 = {10, 20, 30, 10, 20}

print(s1)

# Explanation:
# Sets store only unique elements.
# Duplicate values 10 and 20 are automatically removed.


# =========================================================
# 2. SET IS CASE-SENSITIVE
# =========================================================

s1 = {"Ravi", "Ravi", "ravi"}

print(s1)

# Explanation:
# "Ravi" and "ravi" are different strings.
# Python strings are case-sensitive.


# =========================================================
# 3. REMOVE DUPLICATES FROM A LIST
# =========================================================

list1 = [10, 20, 30, 10, 20]

result = list(set(list1))

print(result)

# Explanation:
# set(list1) removes duplicate elements.
# list() converts the set back into a list.


# IMPORTANT:
# Order may change because sets are unordered.


# =========================================================
# 4. REMOVE DUPLICATES AND CONVERT TO TUPLE
# =========================================================

tuple1 = [10, 20, 30, 10, 20]

result = tuple(set(tuple1))

print(result)

# Explanation:
# set() removes duplicate elements.
# tuple() converts the unique elements into a tuple.


# NOTE:
# Variable name tuple1 should ideally contain a tuple.
# Here it contains a list, but set() works with both.


# =========================================================
# 5. EMPTY DICTIONARY VS EMPTY SET
# =========================================================

s1 = {}

print(type(s1))

s2 = set()

print(type(s2))

# Explanation:
# {} creates an empty dictionary.
# set() must be used to create an empty set.


# =========================================================
# 6. ADDING ONE ELEMENT USING add()
# =========================================================

s1 = {10, 20, 30}

s1.add(40)

print(s1)

# Explanation:
# add() adds one element to a set.
# If the element already exists, it is not duplicated.


# =========================================================
# 7. ADDING MULTIPLE ELEMENTS USING update()
# =========================================================

s1 = {10, 20, 30}

list1 = [50, 60, 70]

s1.update(list1)

print(s1)

# Explanation:
# update() adds multiple elements from another iterable.
# The iterable can be a list, tuple, or set.


# =========================================================
# 8. update() USING A TUPLE
# =========================================================

s1 = {10, 20, 30}

tuple1 = (80, 90)

s1.update(tuple1)

print(s1)

# Explanation:
# update() accepts a tuple as an iterable.
# Each tuple element is added individually to the set.


# =========================================================
# 9. remove() METHOD
# =========================================================

s1 = {10, 20, 30}

s1.remove(10)

print(s1)

# Explanation:
# remove() deletes the specified element.
# It raises an error if the element does not exist.


# =========================================================
# 10. remove() ERROR
# =========================================================

s1 = {10, 20, 30}

# s1.remove(100)

# Explanation:
# This gives a KeyError because 100 does not exist.
# Use discard() when you want safe removal.


# =========================================================
# 11. discard() METHOD
# =========================================================

s1 = {10, 20, 30}

s1.discard(100)

print(s1)

# Explanation:
# discard() removes an element if it exists.
# It does not produce an error if the element is missing.


# =========================================================
# 12. pop() METHOD
# =========================================================

s1 = {10, 20, 30}

x = s1.pop()

print("Removed:", x)
print("Remaining:", s1)

# Explanation:
# pop() removes and returns an arbitrary element.
# Sets are unordered, so do not depend on which element is removed.


# =========================================================
# 13. clear() METHOD
# =========================================================

s1 = {10, 20, 30}

s1.clear()

print(s1)

# Explanation:
# clear() removes all elements from the set.
# The set becomes empty.


# =========================================================
# 14. UNION USING union()
# =========================================================

s1 = {1, 2, 3}
s2 = {3, 4, 5}

print(s1.union(s2))

# Explanation:
# union() combines all unique elements from both sets.
# Duplicate common elements appear only once.


# =========================================================
# 15. UNION USING | OPERATOR
# =========================================================

s1 = {1, 2, 3}
s2 = {3, 4, 5}

print(s1 | s2)

# Explanation:
# | is the union operator for sets.
# It gives all unique elements from both sets.


# =========================================================
# 16. UNION ORDER
# =========================================================

s1 = {1, 2, 3}
s2 = {3, 4, 5}

print(s1.union(s2))
print(s2.union(s1))

# Explanation:
# Union contains all elements from both sets.
# The displayed order should not be relied upon.


# =========================================================
# 17. INTERSECTION USING &
# =========================================================

s1 = {1, 2, 3}
s2 = {3, 4, 5}

print(s1 & s2)

# Explanation:
# Intersection returns only common elements.
# Here, 3 exists in both sets.


# =========================================================
# 18. INTERSECTION USING intersection()
# =========================================================

s1 = {1, 2, 3}
s2 = {3, 4, 5}

print(s1.intersection(s2))
print(s2.intersection(s1))

# Explanation:
# intersection() finds elements common to both sets.
# The result is the same regardless of which set calls the method.


# =========================================================
# 19. DIFFERENCE USING -
# =========================================================

s1 = {1, 2, 3}
s2 = {3, 4, 5}

print(s1 - s2)

# Explanation:
# Difference returns elements present in s1 but not in s2.
# Here, the result is {1, 2}.


# =========================================================
# 20. DIFFERENCE USING difference()
# =========================================================

s1 = {1, 2, 3}
s2 = {3, 4, 5}

print(s1.difference(s2))
print(s2.difference(s1))

# Explanation:
# Difference depends on the order of the sets.
# s1 - s2 and s2 - s1 can produce different results.


# =========================================================
# 21. SYMMETRIC DIFFERENCE USING ^
# =========================================================

s1 = {1, 2, 3}
s2 = {3, 4, 5}

print(s1 ^ s2)

# Explanation:
# Symmetric difference returns elements not common to both sets.
# Common element 3 is excluded.


# =========================================================
# 22. SYMMETRIC DIFFERENCE USING METHOD
# =========================================================

s1 = {1, 2, 3}
s2 = {3, 4, 5}

print(s1.symmetric_difference(s2))
print(s2.symmetric_difference(s1))

# Explanation:
# It returns elements unique to either set.
# Common elements are removed from the result.


# =========================================================
# 23. SET OPERATIONS SUMMARY
# =========================================================

s1 = {1, 2, 3}
s2 = {3, 4, 5}

print("Union:", s1 | s2)
print("Intersection:", s1 & s2)
print("Difference:", s1 - s2)
print("Symmetric Difference:", s1 ^ s2)

# Explanation:
# | gives all unique elements and & gives common elements.
# - gives first-only elements and ^ gives non-common elements.


# =========================================================
# 24. SUBSET USING issubset()
# =========================================================

s1 = {1, 2, 3}
s2 = {1, 2}

print(s2.issubset(s1))

# Explanation:
# s2 is a subset because all elements of s2 exist in s1.
# issubset() returns True or False.


# =========================================================
# 25. SUBSET USING <=
# =========================================================

s1 = {1, 2, 3}
s2 = {1, 2}

print(s2 <= s1)

# Explanation:
# <= checks whether the left set is a subset of the right set.
# It returns True if all elements exist in the other set.


# =========================================================
# 26. SUPERSET USING issuperset()
# =========================================================

s1 = {1, 2, 3}
s2 = {1, 2}

print(s1.issuperset(s2))

# Explanation:
# s1 is a superset because it contains all elements of s2.
# issuperset() returns True or False.


# =========================================================
# 27. SUPERSET USING >=
# =========================================================

s1 = {1, 2, 3}
s2 = {1, 2}

print(s1 >= s2)

# Explanation:
# >= checks whether the left set is a superset.
# All elements of s2 must exist in s1.


# =========================================================
# 28. isdisjoint()
# =========================================================

s3 = {1, 2, 3}
s4 = {4, 5, 6}

print(s3.isdisjoint(s4))

# Explanation:
# isdisjoint() checks whether two sets have no common elements.
# It returns True when there is no intersection.


# =========================================================
# 29. isdisjoint() WITH COMMON ELEMENT
# =========================================================

s1 = {1, 2, 3}
s2 = {3, 4, 5}

print(s1.isdisjoint(s2))

# Explanation:
# Both sets contain 3.
# Therefore, they are not disjoint.


# =========================================================
# 30. len() FUNCTION
# =========================================================

s1 = {10, 20, 30, 40, 50}

print(len(s1))

# Explanation:
# len() returns the number of unique elements.
# Duplicate elements are not counted multiple times.


# =========================================================
# 31. MEMBERSHIP OPERATORS
# =========================================================

s1 = {10, 20, 30, 40, 50}

print(30 in s1)
print(300 not in s1)
print(60 in s1)

# Explanation:
# 'in' checks whether an element exists in the set.
# 'not in' checks whether an element does not exist.


# =========================================================
# 32. SET DOES NOT SUPPORT INDEXING
# =========================================================

s1 = {10, 20, 30}

# print(s1[0])

# Explanation:
# Sets are unordered and unindexed.
# Therefore, indexing like s1[0] is not allowed.


# =========================================================
# 33. SET DOES NOT SUPPORT SLICING
# =========================================================

s1 = {10, 20, 30, 40}

# print(s1[0:2])

# Explanation:
# Sets do not have indexes.
# Therefore, slicing is also not supported.


# =========================================================
# 34. SET COMPREHENSION - NORMAL METHOD
# =========================================================

s1 = {1, 2, 3, 4, 5}

res = set()

for element in s1:
    res.add(element * element)

print(res)

# Explanation:
# Each element is squared using a loop.
# add() stores each result in a new set.


# =========================================================
# 35. SET COMPREHENSION - ONE LINE
# =========================================================

s1 = {1, 2, 3, 4, 5}

res = {
    element * element
    for element in s1
}

print(res)

# Explanation:
# Set comprehension creates a set in one line.
# The expression is executed for every element.


# =========================================================
# 36. SET COMPREHENSION WITH CONDITION
# =========================================================

s1 = {1, 2, 3, 4, 5}

res = {
    element * element
    for element in s1
    if element % 2 == 0
}

print(res)

# Explanation:
# Only even elements pass the condition.
# Their squares are added to the new set.


# =========================================================
# 37. REMOVE DUPLICATES FROM LIST
# =========================================================

list1 = [10, 20, 30, 10, 20, 40, 50]

unique_values = set(list1)

print(unique_values)

# Explanation:
# Converting a list to a set removes duplicates.
# This is one of the most common uses of sets.


# =========================================================
# 38. COMMON ELEMENTS BETWEEN TWO LISTS
# =========================================================

list1 = [10, 20, 30, 40]
list2 = [30, 40, 50, 60]

common = set(list1) & set(list2)

print(common)

# Explanation:
# Convert both lists into sets.
# Intersection finds the common elements.


# =========================================================
# 39. DIFFERENT ELEMENTS BETWEEN TWO LISTS
# =========================================================

list1 = [10, 20, 30]
list2 = [30, 40, 50]

different = set(list1) ^ set(list2)

print(different)

# Explanation:
# Symmetric difference finds elements unique to each collection.
# Common elements are excluded.


# =========================================================
# 40. IMPORTANT SET RULES
# =========================================================

"""
SET RULES:

1. Duplicates are automatically removed.

2. Sets are unordered.
   Do not depend on the displayed order.

3. Sets are unindexed.
   s1[0] is not allowed.

4. Sets do not support slicing.

5. Sets are mutable.
   We can add and remove elements.

6. Set elements must be hashable.
   Mutable objects like lists cannot normally be set elements.

Example:

Valid:
{10, "Hello", (1, 2)}

Invalid:
{10, [1, 2]}

Because a list is mutable.
"""


# =========================================================
# FINAL INTERVIEW ANSWER
# =========================================================

"""
A Set is an unordered, unindexed, mutable collection
of unique elements in Python.

Important properties:

- Duplicates are automatically removed.
- Sets are unordered.
- Sets do not support indexing or slicing.
- Elements can be added or removed.
- Set operations include union, intersection,
  difference, and symmetric difference.

Common methods:

add()
update()
remove()
discard()
pop()
clear()

Set Operations:

union()                  -> |
intersection()           -> &
difference()             -> -
symmetric_difference()   -> ^

Relationship Methods:

issubset()
issuperset()
isdisjoint()
"""


# =========================================================
# FINAL QUICK COMPARISON
# =========================================================

"""
LIST
--------------------------------
Ordered       -> Yes
Indexed       -> Yes
Duplicates    -> Allowed
Mutable       -> Yes
Syntax        -> []

TUPLE
--------------------------------
Ordered       -> Yes
Indexed       -> Yes
Duplicates    -> Allowed
Mutable       -> No
Syntax        -> ()

SET
--------------------------------
Ordered       -> No
Indexed       -> No
Duplicates    -> Not Allowed
Mutable       -> Yes
Syntax        -> {}

DICTIONARY
--------------------------------
Ordered       -> Insertion order maintained
Indexed       -> No (Access using Keys)
Duplicates    -> Keys No, Values Yes
Mutable       -> Yes
Syntax        -> {}
Data          -> Key : Value
"""