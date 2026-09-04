"""
=========================================================
PYTHON DICTIONARY - COMPLETE REVISION NOTES
=========================================================

1. DICTIONARY BASICS
   - Dictionary stores data in Key : Value pairs.
   - Key and Value are separated using :.
   - Dictionaries are created using {} or dict().
   - Example:
       {"name": "Bharath", "age": 25}

2. DICTIONARY PROPERTIES
   - Mutable
   - Keys are unique
   - Values can be duplicated
   - Keys must be immutable/hashable
   - Values can be any data type
   - Access values using keys

3. CREATION
   - {}
   - dict()

4. ACCESSING VALUES
   - d1["key"]       -> Direct access
   - d1.get("key")   -> Safe access

5. DIFFERENCE BETWEEN [] AND get()
   - d1["key"]
       If key does not exist -> KeyError

   - d1.get("key")
       If key does not exist -> None

   - d1.get("key", default)
       If key does not exist -> Returns default value

6. IMPORTANT DICTIONARY METHODS
   - keys()
   - values()
   - items()
   - get()
   - update()
   - pop()
   - popitem()

7. ADDING AND UPDATING
   - d1["key"] = value
   - New key -> Adds new key-value pair
   - Existing key -> Updates value

8. DELETING
   - del d1["key"]
   - pop("key")
   - popitem()

9. ITERATION
   - for key in d1
   - for key in d1.keys()
   - for value in d1.values()
   - for key, value in d1.items()

10. MEMBERSHIP
   - "key" in d1
   - Membership checks KEYS by default.

11. NESTED DICTIONARY
   - Dictionary inside another dictionary.
   - Access using multiple keys.

12. FREQUENCY COUNTING
   - Dictionary can count characters or words.
   - get(key, 0) is useful.

13. UPDATE()
   - Combines/updates dictionaries.

14. DICTIONARY COMPREHENSION
   - {key: value for ...}

15. MAXIMUM VALUE
   - max(d1, key=d1.get)
   - Returns key having maximum value.

16. SORTING
   - sorted(d1.items())
   - Sort by key by default.
   - key=lambda item: item[1] -> Sort by value.

17. SUM OF VALUES
   - sum(d1.values())

18. REVERSE KEY AND VALUE
   - {value: key for key, value in d1.items()}

19. DUPLICATE KEYS
   - Dictionary keys must be unique.
   - Last value overwrites previous value.

20. REMOVE DUPLICATE VALUES
   - Check values before adding to a new dictionary.

21. LIST OF DICTIONARIES
   - List can contain multiple dictionaries.
   - Use loops to access values.

=========================================================
QUICK REMEMBER FORMULA

Dictionary = Key : Value

Creation        -> {} / dict()
Access          -> d[key]
Safe Access     -> d.get(key)

All Keys        -> keys()
All Values      -> values()
Key + Value     -> items()

Add/Update      -> d[key] = value
Combine         -> update()

Delete          -> del
Delete by Key   -> pop()
Delete Last     -> popitem()

Iteration Keys  -> for key in d
Iteration Value -> values()
Both            -> items()

Membership      -> Checks Keys

Nested Dict     -> Multiple Keys

Frequency       -> get(key, 0)

Comprehension   -> {key:value for ...}

Max Value       -> max(d, key=d.get)

Sort by Key     -> sorted(d.items())
Sort by Value   -> lambda item:item[1]

Sum Values      -> sum(d.values())

Duplicate Keys  -> Last Value Wins

=========================================================
COMPLETE CODE EXAMPLES
=========================================================
"""


# =========================================================
# 1. DICTIONARY CREATION
# =========================================================

# Dictionary stores data in Key and Value pairs.
# Key and Value are separated using :.
# Dictionary is mutable.
# Created using {} or dict().

d1 = {}

print(d1)
print(type(d1))

# Explanation:
# {} creates an empty dictionary.
# type() confirms that the object is a dictionary.


# =========================================================
# 2. DICTIONARY WITH KEY-VALUE PAIRS
# =========================================================

d1 = {
    "name": "Emp1",
    "dept": "R&D",
    "salary": 10000,
    "id": 101
}

print(d1)

# Explanation:
# Each dictionary element contains a key and its value.
# Keys are used to access corresponding values.


# =========================================================
# 3. ACCESSING DICTIONARY VALUES
# =========================================================

d1 = {
    "name": "Emp1",
    "dept": "R&D",
    "salary": 10000,
    "id": 101
}

print(d1["name"])

# Explanation:
# Square brackets access a value using its key.
# The key must exist in the dictionary.


# =========================================================
# 4. ACCESSING A NON-EXISTING KEY
# =========================================================

d1 = {
    "name": "Emp1"
}

# print(d1["Address"])

# Explanation:
# Using [] with a missing key produces a KeyError.
# Therefore, get() is safer when a key may not exist.


# =========================================================
# 5. get() METHOD
# =========================================================

d1 = {
    "name": "Emp1"
}

print(d1.get("Address"))

# Explanation:
# get() safely accesses a dictionary value.
# If the key does not exist, it returns None.


# =========================================================
# 6. get() WITH DEFAULT VALUE
# =========================================================

d1 = {
    "name": "Emp1"
}

print(d1.get("Address", "Hyderabad"))

# Explanation:
# get(key, default) returns the default value if the key is missing.
# Here, "Hyderabad" is returned.


# =========================================================
# 7. keys(), values() AND items()
# =========================================================

d1 = {
    "name": "Emp1",
    "dept": "R&D",
    "salary": 10000
}

print(d1.keys())
print(d1.values())
print(d1.items())

# Explanation:
# keys() returns all keys and values() returns all values.
# items() returns key-value pairs.


# =========================================================
# 8. ADDING DATA TO A DICTIONARY
# =========================================================

d1 = {}

d1["key1"] = "GenAI"
d1["key2"] = "AgenticAI"

print(d1)

# Explanation:
# Assigning a new key adds a new key-value pair.
# Dictionaries can be modified because they are mutable.


# =========================================================
# 9. UPDATING A DICTIONARY VALUE
# =========================================================

d1 = {
    "key1": "GenAI"
}

d1["key1"] = "Generative AI"

print(d1)

# Explanation:
# If the key already exists, its value is updated.
# The old value is replaced.


# =========================================================
# 10. DELETE USING del
# =========================================================

d1 = {
    "key1": "GenAI",
    "key2": "AgenticAI"
}

del d1["key1"]

print(d1)

# Explanation:
# del removes a key-value pair using its key.
# The specified key must exist.


# =========================================================
# 11. ITERATING THROUGH KEYS
# =========================================================

d1 = {
    "key1": "Hello",
    "key2": "FDE",
    "key3": "QC"
}

for key in d1.keys():
    print(key, end=" ")

print()

# Explanation:
# keys() provides all dictionary keys.
# The loop accesses one key at a time.


# =========================================================
# 12. ITERATING THROUGH VALUES
# =========================================================

d1 = {
    "key1": "Hello",
    "key2": "FDE",
    "key3": "QC"
}

for value in d1.values():
    print(value, end=" ")

print()

# Explanation:
# values() provides all dictionary values.
# The loop accesses one value at a time.


# =========================================================
# 13. ITERATING THROUGH KEYS AND VALUES
# =========================================================

d1 = {
    "key1": "Hello",
    "key2": "FDE",
    "key3": "QC"
}

for key, value in d1.items():
    print(key, value, sep=" ---> ")

# Explanation:
# items() returns key-value pairs.
# Both key and value can be unpacked into variables.


# =========================================================
# 14. ITERATING DIRECTLY THROUGH DICTIONARY
# =========================================================

d1 = {
    "name": "Bharath",
    "skill": "Python"
}

for key in d1:
    print(key)

# Explanation:
# Iterating directly through a dictionary returns keys.
# It is similar to iterating using d1.keys().


# =========================================================
# 15. MEMBERSHIP OPERATORS
# =========================================================

d1 = {
    "key1": "Hello",
    "key2": "FDE",
    "key3": "QC"
}

print("key1" in d1)
print("key4" in d1)

# Explanation:
# Membership in a dictionary checks keys by default.
# It does not check values.


# =========================================================
# 16. pop() METHOD
# =========================================================

d1 = {
    "key1": "Hello",
    "key2": "FDE",
    "key3": "QC"
}

removed_value = d1.pop("key3")

print(removed_value)
print(d1)

# Explanation:
# pop(key) removes the specified key-value pair.
# It also returns the removed value.


# =========================================================
# 17. popitem() METHOD
# =========================================================

d1 = {
    "key1": "Hello",
    "key2": "FDE",
    "key3": "QC"
}

d1.popitem()

print(d1)

# Explanation:
# popitem() removes the last inserted key-value pair.
# It also returns the removed key-value pair.


# =========================================================
# 18. NESTED DICTIONARY
# =========================================================

d1 = {
    "d2": {
        "wish": "Hello"
    }
}

print(d1["d2"]["wish"])

# Explanation:
# d1["d2"] accesses the inner dictionary.
# ["wish"] accesses "Hello" from the inner dictionary.


# =========================================================
# 19. ITERATING THROUGH NESTED DICTIONARY
# =========================================================

d1 = {
    "d2": {
        "wish": "Hello"
    }
}

for inner in d1.values():

    for value in inner.values():
        print(value)

# Explanation:
# The outer loop accesses the inner dictionary.
# The inner loop accesses values inside it.


# =========================================================
# 20. CHARACTER FREQUENCY
# =========================================================

text = "Hello"

count = {}

for ch in text:
    count[ch] = count.get(ch, 0) + 1

print(count)

# Explanation:
# get(ch, 0) returns the current count or 0 if the key is new.
# Each occurrence increases the count by 1.


# =========================================================
# 21. CHARACTER FREQUENCY STEP BY STEP
# =========================================================

text = "Hello"

count = {}

for ch in text:

    # First occurrence:
    # count.get(ch, 0) returns 0
    # 0 + 1 = 1

    # Next occurrence:
    # Existing count is returned
    # Existing count + 1

    count[ch] = count.get(ch, 0) + 1

print(count)

# Output:
# {'H': 1, 'e': 1, 'l': 2, 'o': 1}

# Explanation:
# Dictionary keys store characters.
# Dictionary values store their frequency.


# =========================================================
# 22. split() METHOD
# =========================================================

text = "java python java ml java python"

words = text.split(" ")

print(words)

# Explanation:
# split(" ") divides the string using spaces.
# It returns a list of words.


# =========================================================
# 23. update() METHOD
# =========================================================

d1 = {
    "key1": 100
}

d2 = {
    "key2": 200
}

d3 = {
    "key3": 300
}

d1.update(d2)
d1.update(d3)

print(d1)

# Explanation:
# update() adds key-value pairs from another dictionary.
# Existing keys are updated if they are already present.


# =========================================================
# 24. DICTIONARY COMPREHENSION
# =========================================================

result = {
    x: x ** x
    for x in range(1, 6)
}

print(result)

# Explanation:
# Dictionary comprehension creates a dictionary in one line.
# Each x becomes a key and x ** x becomes its value.


# =========================================================
# 25. DICTIONARY COMPREHENSION SHORT VERSION
# =========================================================

print({x: x ** x for x in range(1, 6)})

# Explanation:
# This is a compact way to create a dictionary.
# It follows {key: value for ...} syntax.


# =========================================================
# 26. FIND KEY WITH MAXIMUM VALUE
# =========================================================

d1 = {
    "std1": 80,
    "std2": 90,
    "std3": 75
}

x = max(d1, key=d1.get)

print(x, d1.get(x))

# Explanation:
# max() finds the key with the largest value.
# key=d1.get tells max() to compare dictionary values.


# =========================================================
# 27. SORT DICTIONARY BY KEY
# =========================================================

d1 = {
    "John": 80,
    "Anil": 90,
    "Venkat": 75
}

res = dict(sorted(d1.items()))

print(res)

# Explanation:
# sorted(d1.items()) sorts key-value pairs by key.
# dict() converts the sorted result back into a dictionary.


# =========================================================
# 28. SORT DICTIONARY BY VALUE
# =========================================================

d1 = {
    "John": 80,
    "Anil": 90,
    "Venkat": 75
}

res = dict(
    sorted(
        d1.items(),
        key=lambda item: item[1]
    )
)

print(res)

# Explanation:
# item[0] represents the key and item[1] represents the value.
# lambda item: item[1] tells sorted() to sort using values.


# =========================================================
# 29. SUM OF DICTIONARY VALUES
# =========================================================

expenses = {
    "Rent": 50000,
    "Travel": 10000,
    "Food": 20000
}

print(sum(expenses.values()))

# Explanation:
# values() returns all dictionary values.
# sum() adds all numeric values.


# =========================================================
# 30. REVERSE KEY AND VALUE
# =========================================================

d1 = {
    "key1": 100,
    "key2": 200
}

d2 = {
    value: key
    for key, value in d1.items()
}

print(d2)

# Explanation:
# The original value becomes the new key.
# The original key becomes the new value.


# =========================================================
# 31. DUPLICATE KEYS
# =========================================================

d1 = {
    "key1": 100,
    "key1": 1000
}

print(d1)

# Explanation:
# Dictionary keys must be unique.
# The last value overwrites the previous value.


# =========================================================
# 32. DICTIONARY WITH DUPLICATE VALUES
# =========================================================

d1 = {
    "A": 10,
    "B": 20,
    "C": 10,
    "D": 20,
    "E": 30
}

print(d1)

# Explanation:
# Dictionary keys must be unique.
# Dictionary values can be duplicated.


# =========================================================
# 33. REMOVE DUPLICATE VALUES
# =========================================================

d1 = {
    "A": 10,
    "B": 20,
    "C": 10,
    "D": 20,
    "E": 30
}

result = {}

for key, value in d1.items():

    if value not in result.values():
        result[key] = value

print(result)

# Explanation:
# Each value is checked before adding it to result.
# Only the first occurrence of each value is stored.


# =========================================================
# 34. LIST OF DICTIONARIES
# =========================================================

list1 = [
    {"num1": 10},
    {"num1": 20},
    {"num1": 30}
]

print(
    list1[0]["num1"] +
    list1[1]["num1"] +
    list1[2]["num1"]
)

# Explanation:
# list1[index] accesses a dictionary.
# ["num1"] accesses the value from that dictionary.


# =========================================================
# 35. SUM VALUES FROM LIST OF DICTIONARIES
# =========================================================

list1 = [
    {"num1": 10},
    {"num1": 20},
    {"num1": 30}
]

res = 0

for d1 in list1:

    for value in d1.values():
        res += value

print(res)

# Explanation:
# The outer loop accesses each dictionary.
# The inner loop accesses values and adds them.


# =========================================================
# 36. REVERSE KEY-VALUE USING COMPREHENSION
# =========================================================

d1 = {
    "a": 10,
    "b": 20,
    "c": 10
}

result = {
    value: key
    for key, value in d1.items()
}

print(result)

# Explanation:
# Values become keys and keys become values.
# Duplicate values can overwrite previous keys.


# IMPORTANT:
# Original:
# {"a": 10, "b": 20, "c": 10}

# Reversed:
# {10: "c", 20: "b"}

# Because dictionary keys must be unique.


# =========================================================
# 37. DICTIONARY KEYS MUST BE IMMUTABLE/HASHABLE
# =========================================================

d1 = {
    "name": "Bharath",
    101: "Employee",
    (10, 20): "Tuple Key"
}

print(d1)

# Explanation:
# String, integer, and tuple can be dictionary keys.
# Lists and dictionaries cannot be keys because they are mutable.


# =========================================================
# 38. DICTIONARY VALUES CAN BE ANY DATA TYPE
# =========================================================

d1 = {
    "name": "Bharath",
    "age": 25,
    "skills": ["Python", "GenAI"],
    "address": {
        "city": "Hyderabad"
    },
    "active": True
}

print(d1)

# Explanation:
# Dictionary values can contain any data type.
# Values can also contain lists or nested dictionaries.


# =========================================================
# 39. IMPORTANT: [] VS ()
# =========================================================

count = {
    "H": 1
}

print(count["H"])

# print(count("H"))

# Explanation:
# [] is used to access a dictionary value using a key.
# () is used to call a function or method.


# =========================================================
# FINAL INTERVIEW ANSWER
# =========================================================

"""
Dictionary is a mutable collection that stores data in
Key : Value pairs.

Important properties:

- Created using {} or dict()
- Keys must be unique
- Keys must be immutable/hashable
- Values can be duplicated
- Values can be any data type
- Dictionary is mutable
- Values are accessed using keys

Common methods:

get()
keys()
values()
items()
update()
pop()
popitem()

Important concept:

d[key]        -> Direct access
d.get(key)    -> Safe access

Membership:

key in d      -> Checks keys

Frequency:

count[ch] = count.get(ch, 0) + 1
"""