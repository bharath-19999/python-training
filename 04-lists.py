"""
=========================================================
PYTHON LISTS - COMPLETE REVISION NOTES
=========================================================

1. LIST BASICS
   - List = Ordered + Indexed + Heterogeneous + Mutable collection
   - Creation: [] or list()
   - Example: [10, "Hello", 20.5]

2. LIST PROPERTIES
   - Ordered
   - Indexed
   - Allows duplicate values
   - Heterogeneous elements allowed
   - Mutable (can be modified)

3. LIST VS TUPLE
   - List  -> Mutable, uses []
   - Tuple -> Immutable, uses ()

4. LIST UNPACKING
   - a, b, c = list1

5. EXTENDED UNPACKING
   - a, *b, c = list1
   - *b collects remaining elements into a list.

6. BUILT-IN FUNCTIONS
   - len()
   - max()
   - min()
   - sum()
   - sorted()

7. LIST METHODS
   - append()
   - extend()
   - insert()
   - remove()
   - pop()
   - clear()
   - count()
   - sort()
   - reverse()

8. SORTING
   - sorted() -> Returns a NEW sorted list.
   - sort()   -> Modifies the ORIGINAL list.

9. ADDING ELEMENTS
   - append(x)       -> Adds one element at end.
   - insert(i, x)    -> Adds element at specific index.
   - extend(list2)   -> Adds multiple elements.

10. REMOVING ELEMENTS
   - remove(x) -> Removes first matching value.
   - pop()     -> Removes and returns element.
   - clear()   -> Removes all elements.
   - del       -> Deletes by index or slicing.

11. MEMBERSHIP
   - in
   - not in

12. REVERSING
   - list[::-1] -> Creates reversed copy.
   - reverse()  -> Modifies original list.

13. ITERATION
   - for loop
   - enumerate() -> Index + Value
   - while loop
   - zip() -> Iterate multiple lists together.

14. SLICING
   - list[start : stop : step]
   - Positive indexing -> 0 to n-1
   - Negative indexing -> -n to -1

15. NESTED LIST
   - List inside another list.
   - Access using list[row][column].
   - Use nested loops.

16. COPYING
   - list2 = list1 -> Same object/reference.
   - deepcopy() -> Completely independent copy.

17. == VS is
   - == compares VALUES.
   - is compares MEMORY/OBJECT identity.

18. CONCATENATION
   - + joins lists.

19. EXTEND
   - extend() modifies the original list.

20. UNPACKING LISTS
   - [*list1, *list2] combines lists.

21. REPETITION
   - list * number

22. HETEROGENEOUS LIST
   - List can contain different data types.

23. DUPLICATES
   - Lists allow duplicate values.
   - count() helps find repeated elements.

=========================================================
QUICK REMEMBER FORMULA

List = Ordered + Indexed + Heterogeneous + Mutable

Creation       -> [] / list()
Duplicates     -> Allowed
Modification   -> Allowed
Unpacking      -> a,b,c = list
Extended       -> *variable

Functions      -> len, max, min, sum, sorted
Methods        -> append, extend, insert
                  remove, pop, clear
                  count, sort, reverse

Loop           -> for
Index + Value  -> enumerate()
Condition Loop -> while
Two Lists      -> zip()

Slicing        -> [start:stop:step]
Nested List    -> Nested loops

Compare Values -> ==
Compare Memory -> is

Join           -> +
Repeat         -> *
Copy           -> deepcopy()

=========================================================
COMPLETE CODE EXAMPLES
=========================================================
"""


# =========================================================
# 1. LIST CREATION
# =========================================================

# Collection of indexed and heterogeneous elements is called a list.
# List is MUTABLE.
# Created using [] or list().

list1 = [10, "Hello", 20.5, True]

print(list1)

# Explanation:
# A list can store different data types.
# Lists are mutable, so elements can be changed.


# =========================================================
# 2. LIST UNPACKING
# =========================================================

list1 = [10, 20, 30, 40, 50]

e1, e2, e3, e4, e5 = list1

print(e1, e2, e3, e4, e5)

# Explanation:
# List elements are unpacked into individual variables.
# The number of variables must match the number of elements.


# =========================================================
# 3. EXTENDED UNPACKING
# =========================================================

list1 = [1000, 100, 10, 0, -10]

ele1, *list2, ele5 = list1

ele2, *list3 = list2

ele3, ele4 = list3

print(ele1, ele2, ele3, ele4, ele5)

# Explanation:
# *variable collects multiple remaining elements into a list.
# This is called extended unpacking.


# =========================================================
# 4. LIST BUILT-IN FUNCTIONS
# =========================================================

list1 = [10, 50, 20, 40, 30]

print(len(list1))
print(max(list1))
print(min(list1))
print(sum(list1))

# Explanation:
# len() gives number of elements.
# max(), min(), and sum() perform operations on numeric elements.


# =========================================================
# 5. COUNT() METHOD
# =========================================================

list2 = [10, 20, 10, 30, 10, 20, 20, 30, 40, 20]

print(list2.count(10))
print(list2.count(20))
print(list2.count(100))

# Explanation:
# count() returns the number of occurrences of an element.
# If the element does not exist, it returns 0.


# =========================================================
# 6. FINDING AVERAGE
# =========================================================

list3 = [100, 10, 0]

average = sum(list3) / len(list3)

print(average)

# Explanation:
# sum() adds all elements.
# len() gives the number of elements to calculate the average.


# =========================================================
# 7. sorted() FUNCTION
# =========================================================

list4 = [10, 50, 20, 40, 30]

res = sorted(list4)

print(res)
print(list4)

# Explanation:
# sorted() creates and returns a new sorted list.
# The original list remains unchanged.


# =========================================================
# 8. sort() METHOD
# =========================================================

list5 = [10, 50, 20, 40, 30]

list5.sort()

print(list5)

# Explanation:
# sort() modifies the original list.
# It does not create a separate sorted list.


# =========================================================
# 9. APPEND, INSERT AND EXTEND
# =========================================================

list1 = [10, 20, 30]

list1.append(40)
list1.append(60)

list1.insert(4, 50)

list2 = [70, 80, 90, 100]

list1.extend(list2)

print(list1)

# Explanation:
# append() adds one element at the end.
# insert() adds at a specific index and extend() adds multiple elements.


# =========================================================
# 10. DIFFERENCE BETWEEN append() AND extend()
# =========================================================

list1 = [10]
list2 = [20, 30]

list1.extend(list2)

print(list1)

list1 = [10]

list1.append(list2)

print(list1)

# Explanation:
# extend() adds individual elements from another list.
# append() adds the complete list as one element.


# =========================================================
# 11. REMOVE, POP AND CLEAR
# =========================================================

list1 = [10, 20, 10, 20, 30, 40, 50, 10]

list1.remove(10)

print(list1)

list1.pop()

print(list1)

list1.clear()

print(list1)

# Explanation:
# remove() removes the first matching value.
# pop() removes an element, and clear() removes all elements.


# =========================================================
# 12. del KEYWORD
# =========================================================

list1 = [10, 20, 30, 40, 50]

del list1[0]

print(list1)

# Explanation:
# del deletes an element using its index.
# Here, the first element is removed.


# =========================================================
# 13. remove() METHOD
# =========================================================

list1 = [10, 20, 30, 40, 50]

list1.remove(10)

print(list1)

# Explanation:
# remove(value) removes the first occurrence of the value.
# It removes based on value, not index.


# =========================================================
# 14. DELETE USING SLICING
# =========================================================

list1 = [10, 20, 30, 40, 50]

del list1[1:3]

print(list1)

# Explanation:
# Slicing selects a range of elements.
# del removes all selected elements.


# =========================================================
# 15. MEMBERSHIP OPERATORS
# =========================================================

list1 = [10, 20, 30, 40, 50]

print(30 in list1)
print(300 not in list1)
print(60 in list1)

# Explanation:
# 'in' checks whether an element exists.
# 'not in' checks whether an element does not exist.


# =========================================================
# 16. REVERSING A LIST
# =========================================================

list1 = [10, 20, 30, 40, 50]

print(list1[::-1])

list1.reverse()

print(list1)

# Explanation:
# [::-1] creates a reversed version using slicing.
# reverse() modifies the original list.


# =========================================================
# 17. FOR LOOP ITERATION
# =========================================================

list1 = [10, 20, 30, 40, 50]

for element in list1:
    print(element, end=" ")

print()

# Explanation:
# The for loop accesses one element at a time.
# Each element is stored temporarily in 'element'.


# =========================================================
# 18. enumerate()
# =========================================================

list1 = [10, 20, 30, 40, 50]

for index, element in enumerate(list1):
    print(index, element, sep=" ---> ")

# Explanation:
# enumerate() provides both index and value.
# It is useful when you need element position.


# =========================================================
# 19. WHILE LOOP ITERATION
# =========================================================

list1 = [10, 20, 30, 40, 50]

i = 0

while i < len(list1):

    print(list1[i])

    i = i + 1

# Explanation:
# i represents the index of the list.
# The loop continues until i reaches the list length.


# =========================================================
# 20. zip()
# =========================================================

list1 = [10, 20, 30, 40, 50]
list2 = [1000, 2000, 3000, 4000, 5000]

for e1, e2 in zip(list1, list2):
    print(e1, e2, sep=" -----> ")

# Explanation:
# zip() pairs elements from two lists based on their position.
# First elements are paired together, then second elements, and so on.


# =========================================================
# 21. LIST SLICING
# =========================================================

list1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# Positive index: 0 to 9
# Negative index: -10 to -1

print(list1[0:7:2])
print(list1[1:6:2])
print(list1[:1])
print(list1[::2])
print(list1[::-2])
print(list1[::3])
print(list1[::-3])

# Explanation:
# Slicing format is [start : stop : step].
# stop index is excluded from the result.


# =========================================================
# 22. IMPORTANT SLICING EXAMPLES
# =========================================================

list1 = [10, 20, 30, 40, 50]

print(list1[0:3])
print(list1[:3])
print(list1[2:])
print(list1[::2])
print(list1[::-1])

# Explanation:
# Slicing can select specific portions of a list.
# A negative step moves through the list in reverse.


# =========================================================
# 23. NESTED LIST
# =========================================================

list1 = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

print(list1[0][0])
print(list1[1][1])
print(list1[2][2])

# Explanation:
# First index selects the inner list.
# Second index selects an element from that inner list.


# =========================================================
# 24. NESTED LIST USING LOOPS
# =========================================================

list1 = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

for inner in list1:

    for index, element in enumerate(inner):
        print(index, element, sep=" --- ")

    print("-------------------")

# Explanation:
# Outer loop accesses each inner list.
# Inner loop accesses elements inside each inner list.


# =========================================================
# 25. LIST REFERENCE / SHALLOW ASSIGNMENT
# =========================================================

list1 = [[10, 20], [30, 40]]

list2 = list1

list1[0].append(30)

print(list2)

# Explanation:
# list2 = list1 means both variables refer to the same object.
# Changes made through list1 are visible through list2.


# =========================================================
# 26. DEEP COPY
# =========================================================

import copy

list1 = [[10, 20], [30, 40]]

list2 = copy.deepcopy(list1)

list1[0][0] = 100

print(list1)
print(list2)

# Explanation:
# deepcopy() creates a completely independent copy.
# Changes in the original nested list do not affect the copied list.


# =========================================================
# 27. == VS is
# =========================================================

list1 = [10, 20, 30]

list2 = [10, 20, 30]

print(list1 == list2)
print(list1 is list2)

# Explanation:
# == compares values.
# is compares whether both variables refer to the same object.


# =========================================================
# 28. SAME REFERENCE EXAMPLE
# =========================================================

list1 = [10, 20, 30]

list2 = list1

print(list1 == list2)
print(list1 is list2)

# Explanation:
# Values are equal, so == returns True.
# Both variables reference the same object, so is returns True.


# =========================================================
# 29. LIST CONCATENATION USING +
# =========================================================

list1 = [10, 20]

list2 = [30, 40]

list3 = list1 + list2

print(list3)

# Explanation:
# + joins two lists and creates a new list.
# The original lists remain unchanged.


# =========================================================
# 30. LIST COMBINATION USING extend()
# =========================================================

list1 = [10, 20]

list2 = [30, 40]

list1.extend(list2)

print(list1)

# Explanation:
# extend() adds elements of list2 into list1.
# The original list1 is modified.


# =========================================================
# 31. LIST COMBINATION USING UNPACKING
# =========================================================

list1 = [10, 20]

list2 = [30, 40]

list3 = [*list1, *list2]

print(list3)

# Explanation:
# * unpacks all elements from both lists.
# A new combined list is created.


# =========================================================
# 32. LIST REPETITION
# =========================================================

list1 = [10, 20, 30]

list2 = list1 * 3

print(list2)

# Explanation:
# * repeats all list elements.
# Here, the list is repeated three times.


# =========================================================
# 33. HETEROGENEOUS LIST
# =========================================================

list1 = [
    "Hello",
    10,
    10.1,
    True,
    [10, 20],
    (10, 20),
    {"name": "Hello"},
    {10, 20, 10},
    None
]

print(list1)

# Explanation:
# A list can store different data types.
# It can even contain other collections.


# =========================================================
# 34. FINDING DUPLICATE ELEMENTS
# =========================================================

list1 = [10, 20, 30, 10, 20, 30, 40]

list2 = []

for element in list1:

    if list1.count(element) > 1:
        list2.append(element)

print(set(list2))

# Explanation:
# count() checks how many times each element occurs.
# set() removes duplicate values from list2.


# =========================================================
# 35. BETTER WAY TO FIND DUPLICATES
# =========================================================

list1 = [10, 20, 30, 10, 20, 30, 40]

duplicates = []

for element in list1:

    if list1.count(element) >= 1 and element not in duplicates:
        duplicates.append(element)

print(duplicates)

# Explanation:
# This finds duplicate elements without converting the result to a set.
# 'element not in duplicates' prevents adding the same duplicate again.


# =========================================================
# 36. LIST MUTABILITY
# =========================================================

list1 = [10, 20, 30]

list1[0] = 100

print(list1)

# Explanation:
# Lists are mutable.
# We can directly change elements using their index.


# =========================================================
# FINAL INTERVIEW ANSWER
# =========================================================

"""
List is an ordered, indexed, heterogeneous, and mutable
collection in Python.

Lists:
- Allow duplicate values
- Can be modified
- Support indexing and slicing
- Support iteration
- Support append, insert, extend
- Support remove, pop, and clear
- Support sorting and reversing
- Can contain different data types

Common methods:
append(), extend(), insert(), remove(),
pop(), clear(), count(), sort(), reverse()
"""