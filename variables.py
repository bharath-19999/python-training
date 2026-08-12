"""
    variables
    *********
        variables are used to "store the data"
        Ex.
            number
            string
            boolean
            list
            ---
            ---
            ---
            ---
        DataType Representing "Type of data"
        Python supports following "DataTypes"
        1) string
        2) int
        3) boolean
        4) list
        5) tuple
        6) dictionary
        7) set
        8) None 

        string
        ******
            collection of characters called as string
            we will represent string in 3 ways
            1) "" (double quotes)
            2) '' (single quotes)
            3) """""" (triple quotes)
        
            (triple quotes) used to define paragraphs
"""

"""   STRING   """
# str = "python"
# print(str[0:2])
# print(str[2:])
# print(str[:5])
# print(str[:9])
# print(f"...{str[::-1]}..")
# print(str[::-2])
# print(str[::-3])

# course = """
#     here, we will cover
#     1) Python
#     2) ML
#     3) DL
#     ---
#     ---
#     ---
# """
# print(course)

# name = "bharath"
# age = "27"
# print(f"employee name is {name} with age {age}")
# print("employee name is {} with age {}".format(name, age))

# str = "text"
# print(str * 3)

# strings are immutable
# str = "Hello"
# str[0] = 'h'
# print(str)
# print('h'+ str[1:])

# count - count no.of char in the string
# print(str.count('l'))

# replace - replace the character
# print(str.replace("l","L"))
# print(str.replace("l","L",3)) --?

# print(["a"] * 3)

"""    INTEGER   """
# integer
# 1) int 2) float 3) complex
# num = 10
# print(float(num))
# num2 = 10.646
# print(int(num2))
# str = "100.98900988888888"
# print(float(str))
# c = 4 + 5j
# print(type(c))
# print(c.real)
# print(c.imag)
# print(10 / 3)  # 3.3333333333333334
# print(10 // 3) # 3
# print(10 % 3)  # 1

"""
MUTABLE
L → List
D → Dictionary
S → Set

IMMUTABLE
I → Integer
F → Float
B → Boolean
S → String
T → Tuple

# Most important for interviews:
# List, Dictionary, and Set are mutable. String, Integer, Float, Boolean, and Tuple are immutable.
# And remember: variables themselves aren't mutable or immutable—the objects they reference are.
"""
"""    BOOLEAN   """
# flag = True
# flag1 = False
# print(f"Value of flag = {flag} and flag1 = {flag1}")
# print(type(flag))

# res = "GenAi" if flag else "AgenticAi"
# print(res)

# print(True + False)
# print(True + True)
# print(True/False)  # division by Zero Error
# print(False/True)
# print(True and True)
# print(True | False)
# print(True ^  False)
# print(True ^ True)

# age = 20
# citizen = False
# if age>18 and citizen:
#     print("Eligible for voting")
# else:
#     print("Not eligible for voting")

"""   LIST    """
# list
# list = [1,2,3,4,5]
# list2 = [7,8]
# print(list)
# print(type(list))
# list.append(3)
# print(list)
# list.remove(3) # remove first occurance of the value
# print(list)
# list.pop(3)  # delete that position value
# print(list)
# list.extend(list2)
# print(list)
# print(list.count(3))
# list.sort()
# print(list)
# list3 = [10,"hello",-34,0,'A']
# print(list3)
# print(list[2])
# print(list[0:2])
# print(list[::-1])
# print(list[::-2])
# print(list[2:3])

# import sys
# list = [2,"hello",-9,78]
# list1 = []
# print(sys.getsizeof(list))
# print(sys.getsizeof(list1))

"""   TUPLE  """
# import sys
# tuple = 10,20,30,40
# print(sys.getsizeof(tuple))
# tuple[0] = 100
# print(tuple) # Err


