"""
=========================================================
PYTHON TUPLES - COMPLETE REVISION NOTES
=========================================================

1. TUPLE BASICS
   - Tuple = Ordered + Indexed + Heterogeneous + Immutable collection
   - Creation: () or tuple()
   - Example: (10, "Hello", 20.5)

2. TUPLE VS LIST
   - List  -> Mutable, uses []
   - Tuple -> Immutable, uses ()
   - Tuples generally consume less memory.

3. PACKING
   - t1 = 10, 20, 30
   - Python automatically creates a tuple.

4. UNPACKING
   - a, b, c = t1

5. SINGLE ELEMENT TUPLE
   - (10,) -> Tuple
   - (10)  -> Integer
   - Comma is mandatory.

6. EXTENDED UNPACKING
   - a, *b, c = t1
   - *b collects multiple values into a list.

7. CONVERSION
   - list(t1)  -> Tuple to List
   - tuple(l1) -> List to Tuple

8. FUNCTIONS
   - len(), max(), min(), sum(), sorted()
   - sorted() always returns a LIST.

9. TUPLE METHODS
   - count(x) -> Number of occurrences
   - index(x) -> Position of first occurrence

10. ITERATION
   - for element in tuple
   - enumerate() -> Index + Value
   - zip() -> Iterate multiple tuples together

11. NESTED TUPLE
   - Tuple inside another tuple.
   - Use nested loops.

12. MULTIPLE RETURN VALUES
   - Python returns multiple values as a tuple.

13. MEMBERSHIP
   - in
   - not in

14. DICTIONARY KEY
   - Tuple can be a dictionary key because it is immutable.

15. CONCATENATION
   - + joins tuples

16. REPETITION
   - * repeats tuples

17. IMMUTABILITY
   - Tuple elements cannot be directly changed.

18. MODIFYING A TUPLE
   - Create a new tuple using:
   - Slicing + Concatenation

=========================================================
QUICK REMEMBER FORMULA

Tuple = Ordered + Indexed + Heterogeneous + Immutable

Creation       -> () / tuple()
Packing        -> t = 10,20,30
Unpacking      -> a,b,c = t
Single Element -> (10,)
Extended       -> *variable
Conversion     -> list() / tuple()
Functions      -> len, max, min, sum, sorted
Methods        -> count, index
Iteration      -> for
Index + Value  -> enumerate()
Two Iterables  -> zip()
Nested         -> Nested loops
Membership     -> in / not in
Join           -> +
Repeat         -> *
Modify          -> Not directly possible
Solution       -> Slicing + Concatenation

=========================================================
COMPLETE CODE EXAMPLES
=========================================================
"""


# =========================================================
# 1. TUPLE CREATION
# =========================================================

# Tuple is a collection of indexed and heterogeneous elements.
# Tuple is immutable.
# Created using () or tuple().

t1 = (10, "Hello", 20.5)
print(t1)

# Explanation:
# A tuple can store different data types.
# Once created, its elements cannot be directly modified.


# =========================================================
# 2. MEMORY COMPARISON - LIST VS TUPLE
# =========================================================

import sys

list1 = [10, 20, 30, 40, 50]
tuple1 = (10, 20, 30, 40, 50)

print(sys.getsizeof(list1))
print(sys.getsizeof(tuple1))

# Explanation:
# sys.getsizeof() checks memory used by an object.
# Tuples generally use less memory than lists.


# =========================================================
# 3. TUPLE PACKING AND UNPACKING
# =========================================================

tuple1 = 10, 20, 30, 40, 50

e1, e2, e3, e4, e5 = tuple1

print(e1, e2, e3, e4, e5)

# Explanation:
# Multiple values are automatically packed into a tuple.
# Tuple values can be unpacked into individual variables.


# =========================================================
# 4. SINGLE ELEMENT TUPLE
# =========================================================

t1 = (10,)

print(type(t1))

# Explanation:
# A comma is mandatory for a single-element tuple.
# (10) is an integer, but (10,) is a tuple.


# =========================================================
# 5. EXTENDED UNPACKING
# =========================================================

t1 = 10, 20, 30, 40, 50

e1, *list2, e5 = t1

# list2 = [20, 30, 40]

*list3, e4 = list2

# list3 = [20, 30]

e2, e3 = list3

print(e1, e2, e3, e4, e5)

# Explanation:
# *variable collects multiple remaining values into a list.
# Extended unpacking is useful when variables are fewer than elements.


# =========================================================
# 6. TUPLE TO LIST
# =========================================================

t1 = 10, 20, 30, 40, 50

list1 = list(t1)

print(list1)

# Explanation:
# list() converts a tuple into a list.
# The converted list can be modified.


# =========================================================
# 7. LIST TO TUPLE
# =========================================================

list1 = ["Python", "ML", "DL", "NLP", "GenAI", "AgenticAI"]

tuple1 = tuple(list1)

print(tuple1)

# Explanation:
# tuple() converts a list into a tuple.
# The resulting tuple is immutable.


# =========================================================
# 8. TUPLE FUNCTIONS AND METHODS
# =========================================================

t1 = 10, 50, 20, 40, 30

print(len(t1))
print(max(t1))
print(min(t1))
print(sum(t1))

print(t1.count(10))
print(t1.index(20))

# Explanation:
# len, max, min, and sum are built-in functions.
# count() and index() are tuple methods.


# =========================================================
# 9. SORTING A TUPLE
# =========================================================

t1 = 10, 50, 20, 40, 30

res = tuple(sorted(t1))

print(res)
print(t1)

# Explanation:
# sorted() sorts elements but returns a list.
# tuple() converts the sorted list back into a tuple.


# =========================================================
# 10. SORTING INCOMPATIBLE DATA TYPES
# =========================================================

# This will give an error.

# t1 = 10, 50, 20, 40, 30, None
# print(sorted(t1))

# Explanation:
# Python cannot compare None and integers.
# All elements should be comparable for sorting.


# This will also give an error.

# t1 = ["Hello", "Welcome", "Hi", 10]
# print(sorted(t1))

# Explanation:
# Python cannot compare strings and integers.
# Different incompatible types cannot be sorted together.


# =========================================================
# 11. NORMAL TUPLE ITERATION
# =========================================================

t1 = 10, 200, 3000, 30000, 300000, 20

for element in t1:
    print(element)

# Explanation:
# The loop accesses one element at a time.
# Each element is temporarily stored in 'element'.


# =========================================================
# 12. GENERATOR EXPRESSION
# =========================================================

t1 = 10, 200, 3000, 30000, 300000, 20

print(*("Vpro" for _ in t1))

# Explanation:
# "Vpro" is generated once for every element in t1.
# * unpacks all generated values while printing.


# =========================================================
# 13. ENUMERATE()
# =========================================================

t1 = 10, 200, 3000, 30000, 300000, 20

for index, element in enumerate(t1):
    print(index, element)

# Explanation:
# enumerate() gives both index and element.
# It is useful when you need position and value.


# =========================================================
# 14. ZIP()
# =========================================================

t1 = 10, 200, 3000, 30000, 300000, 20
t2 = 100, 1000, 10000, 100000, 2, 2

for element1, element2 in zip(t1, t2):
    print(element1, element2)

# Explanation:
# zip() combines elements based on their positions.
# First element of t1 pairs with first element of t2.


# =========================================================
# 15. NESTED TUPLE
# =========================================================

t1 = (
    (10, 20, 30),
    (40, 50, 60),
    (70, 80, 90)
)

for inner in t1:

    for element in inner:
        print(element, end=" ")

    print()

# Explanation:
# The outer loop accesses each inner tuple.
# The inner loop accesses individual elements.


# =========================================================
# 16. FUNCTION RETURNING MULTIPLE VALUES
# =========================================================

def test():

    num1, num2 = 200, 100

    return (
        num1 + num2,
        num1 - num2,
        num1 * num2,
        num1 / num2,
        num1,
        num2
    )


t1 = test()

add, sub, mul, div, n1, n2 = t1

print(add, sub, mul, div, n1, n2)

# Explanation:
# Multiple returned values are automatically returned as a tuple.
# The returned tuple can be unpacked into variables.


# =========================================================
# 17. MEMBERSHIP OPERATORS
# =========================================================

t1 = 10, 20, 30, 40, 50

print(30 in t1)
print(300 in t1)
print(3000 not in t1)

# Explanation:
# 'in' checks whether an element exists.
# 'not in' checks whether an element does not exist.


# =========================================================
# 18. TUPLE AS DICTIONARY KEY
# =========================================================

d1 = {
    (10, 20): (10, 20)
}

print(d1[(10, 20)])

# Explanation:
# Tuples can be dictionary keys because they are immutable.
# The tuple key is used to access its corresponding value.


# =========================================================
# 19. TUPLE CONCATENATION AND REPETITION
# =========================================================

t1 = 10, 20
t2 = 30, 40

t3 = t1 + t2

t4 = t3 * 2

print(t4)

# Explanation:
# + joins two tuples together.
# * repeats the tuple multiple times.


# =========================================================
# 20. TUPLE IMMUTABILITY
# =========================================================

# t1 = (10, 20, 30, 40, 50)

# t1[0] = 1000

# Explanation:
# This gives a TypeError because tuples are immutable.
# Tuple elements cannot be directly changed.


# =========================================================
# 21. ADDING AN ELEMENT TO A TUPLE
# =========================================================

t1 = 10, 20, 30, 40

t2 = t1 + (50,)

print(t2)

# Explanation:
# We cannot directly add elements to a tuple.
# We create a new tuple using concatenation.


# IMPORTANT:

# (50)  -> Integer
# (50,) -> Tuple


# =========================================================
# 22. INSERTING AN ELEMENT USING SLICING
# =========================================================

t1 = 10, 20, 30, 40

t2 = t1 + (50,)

res = t2[:2] + (25,) + t2[2:]

print(res)

# Explanation:
# Slicing divides the tuple into two parts.
# A new tuple is created by inserting (25,) between them.


# Step-by-step:

# t2 = (10, 20, 30, 40, 50)

# t2[:2]
# (10, 20)

# (25,)
# (25,)

# t2[2:]
# (30, 40, 50)

# Final:
# (10, 20) + (25,) + (30, 40, 50)

# Output:
# (10, 20, 25, 30, 40, 50)


# =========================================================
# FINAL INTERVIEW ANSWER
# =========================================================

"""
Tuple is an ordered, indexed, heterogeneous, and immutable
collection in Python.

It supports:
- Packing
- Unpacking
- Indexing
- Slicing
- Iteration
- Concatenation
- Repetition

However, tuple elements cannot be directly modified.
"""