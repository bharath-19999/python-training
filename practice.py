""" no parameters no return """
# def test():
#     print("Hello")
# test()

"""with parameters no return"""
# def test(param1, param2):
#     print(f"Hello....{param1},{param2}")
# test("cbk","csk")

"""no paramerter with return"""
# def test():
#     num1 = 10
#     num2 = 20
#     sum = num1+num2
#     return sum
# x = test()
# print(x)

"""with parameters with return"""
# def test(param1,param2,param3):
#     sum = param1+param2+param3
#     return sum
# x = test(10,45,56)
# print(x)

# ---------------------------------------------
"""
1. normal parameter
2. default parameter
3. variable-length parameter
4. keyword parameter
"""
# def test(a,b=15):
#     n = a+b
#     return n
# i = test(13,24) 
# print(i)

# def test(num,name="rama",*param1,**param2):
#     print(f"{num}....{name}....{param1}....{param2}")
# test(12,32,3,23,232,5,43,2,2,4,n="bharath")

# ----------------------------------------------------------

"""Lambda functions"""
# func = lambda n:n**2
# print(func(4))

# func = lambda a,b : a + b
# print(func(4,7))
# sam = lambda x : "even" if x%2==0 else "odd"
# print(sam(12))
# from functools import reduce
# num = (1,2,3,4,5,6)
# func = map(lambda a : a * 100, num)
# print(list(func))
# func = list(filter(lambda n : n%2==0, num))
# print(func)
# func = reduce(lambda a,b: a + b, num)
# print(func)


# n = 1
# m = 2
# def addition():
#     res = n+m
#     print(res)
# addition()
# def sub():
#     res = n-m
#     print(res)
# sub()

"""  Practice """
# def mul(num):
#     x = num * num
#     return x
# res = mul(10)
# print(f"Multiplication of num : {res}")

# x = lambda num : num * num
# print(f"Multiplication of num : {x(10)}")

# str1 = "Hello"
# str2 = "Hellt"
# x = "Strings are same" if str1 == str2 else "strings are different"
# print(x)

"""  sum of two numbers  """
# def addition(num1,num2):
#     sum = num1 + num2
#     return sum
# x = addition(20,30)
# print(f"Addition of two numbers is : {x}")    

""" even or odd  """
# num = int(input("Enter number : "))
# res = "EVEN" if num%2 == 0 else "ODD"
# print(res)

""" largest of 3 numbers  """
# a = int(input("Enter a : "))
# b = int(input("Enter b : "))
# c = int(input("Enter c : "))
# res = "a is greater" if a>b and a>c else "b is greater" if b>c else "c is greater"
# print (res)

"""  calculate factorial  """
# a = int(input("Enter a number : "))
# factorial = 1
# for i in range(1,a):
#     factorial = factorial * (i+1)
# print(factorial)

""""  reverse a string """
# str = input("Enter string : ")
# print(f"reverse of a string is : {str[::-1]}")

"""  palindrome """
# str = input("Enter a string : ")
# res = "Palindrome" if str == str[::-1] else "Not a palindrome"
# print(res)

"""  count vowels """
# str1 = input("Enter a string : ")
# str = str1.lower()
# # str = input("Enter a string : ").lower()
# print(str)
# count = 0
# for i in range(0,len(str)):
#     if str[i] == 'a' or str[i] == 'e' or str[i] == 'i' or str[i] == 'o' or str[i] == 'u':
#         count += 1
# print(f"count is : {count}")

"""  count frequency of each character """  #need to understand
# str = input("Enter a string : ").lower()  
# frequency = {}
# for char in str:
#     frequency[char] += 

"""  check two strings are anagrams  """
# same characters with same length
# different meaning

# str1 = "eat"
# str2 = "tea"
# # if len(str1) == len(str2)
# for str1[i] in range(0,len(str1)):
#     print(str1[i])
#     # for char2 in range(0,len(str2)):
#     #     if char1 == char2:

# def is_anagram(str1,str2):
#     return sorted(str1.lower()) == sorted(str2.lower())
# res = is_anagram("a gentleman","elegant man")
# x = "anagram" if res==True else "not an anagram"
# print(x)

# # str = "Hello"
# # x = sorted(str).lower()
# str = input("Enter a string : ").lower()
# x = sorted(str)
# print(x)


""" find max of list """
# list = [10,50,20,40,30]
# res = max(list)
# print(res)

""" remove duplicates from list"""
# numbers = [1, 2, 2, 3, 3]
# unique_numbers = []

# for item in numbers:
#     if item not in unique_numbers:
#         unique_numbers.append(item)

# print(unique_numbers)  
# # Output: [1, 2, 3]


# nums = [1,4,3,1,2,3]
# uniq_num = []

# for item in nums:
#     print(item)

"""  find even numbers in list """
# list = [10,21,30,49,52,69,70,80]
# list2 = []
# for i in list:
#     if i%2==0:
#         list2.append(i)
# print(list2)

""" find second largest number in list """
# list = [30,20,50,10,40]
# list2 = sorted(set(list))
# print(list2)
# if len(list2) > 2:
#     print(list2[-2])
# else:
#     print("list has more than one number")

"""  calculate sum of list elements """
# list = [30,20,-50,10,40]
# # for i in list:
# #     sum = sum + i
# x = sum(list)
# print(x)

"""  write default function """
# def func(p1=10,p2=30):
#     return p1 + p2
# x = func(40)
# print(x)

""" *args """
# def func(*args):
#     return sum(args)
# x = func(10,20,10,40)
# print(x)

""" **kwargs """
# def func(**kwargs):
#     print(kwargs)
# x = func(
#     name = "bharath",
#     age = "27",
#     gender = "Male"
# )
# print(x)

""" functions returning multiple values """
# def calculate(p1,p2):
#     sum = p1 + p2
#     difference = p1 - p2
#     multiplication = p1 * p2
#     division = p1/p2
#     print(f"sum : {sum} \ndiff : {difference} \nmul : {multiplication} \ndiv : {division}")
# calculate(20,40)

""" Lambda + functions """
""" square a numbers  """
# list = [2,4,5]
# list2 = [0]
# x = lambda s:s*s
# for i in list: 
#     res = x(i)
#     list2.append(res)
# print(list2)

"""even numbers"""
# numbers = [1, 2, 3, 8, 4, 5, 6]
# num2 = []
# func = lambda x : x
# for i in numbers:
#     if i%2 == 0:
#         res = func(i)
#         num2.append(res)
# print(num2)

""" reduce,map,filter function"""
# Function        What it does                            Input Size vs Output Size
# map()           Transforms every item in a list         Always the exact same length
# filter()        Selects specific items based on a rule  Same length or shorter
# reduce()        Combines all items cumulatively         Always reduces to one single value

# from functools import reduce
# numbers = [1, 2, 3, 4, 5]
# # lambda x, y: x + y takes two arguments and add(any operation) them
# total_sum = reduce(lambda x, y: x + y, numbers)
# print(total_sum)  # Output: 15

# res = list(map(lambda x:x*x,numbers))
# res = list(filter(lambda x:x%2==0,numbers))
# print(res)

""" leap year"""
# divisible by 400 - leap year
# division by 100 - not leap year
# divisible by 4 - leap year

# year = int(input("enter year : "))
# res = "leap year" if year%4==0 and (year%400==0 or year%100!=0) else "not a leap year"
# print(res)
# if(year%4==0 and (year%100!=0 or year%400==0)):
#     print("leap year")
# else:
#     print("not a leap year")
# #print(res)




# -------------------------------


# fun definition
# def func():
#     print("Hello")
# func()

# no parameter no return type
# def func():
#     a = 10
#     b = 20
#     res = a + b
#     print(res)
# func()

# no parameter with return type
# def func():
#     a = 20
#     b = 30
#     res = a + b
#     return res
# x = func()
# print(x)

# with parameters no return type
# def func(a,b):
#     add = a + b
#     print(add)
# func(10,20)

# with parameter with return type
# def func(a,b):
#     add = a + b
#     return add
# res = func(12,9)
# print(res)


# positional parameters
# def func(a,b):
#     print(a,b)
#     add = a + b
#     print(add)
# func(b=10,a=20)

# default parameters
# def func(a="hello", b="world"):
#     print(a,b)
# func("Hi","Bharath")

# keyword length parameters
# def func(*args):
#     print(args)
# func(10,20,30)

# variable length parameter
# def func(**kwargs):
#     print(kwargs)
# func(name="bharath",age=27)

# def func(p1,p2=9,p3=()):
#     print(p1,p2,p3)
# func(10,8,0,1,2,3,4)

# a = 256
# b = 678
# if (a is b):
#     print("True")
#     print(id(a))
#     print(id(b))
# else:
#     print("False")
#     print(id(a))
#     print(id(b))




tuple1 = (101,29,40)
# print(len(tuple1))
# print(tuple(sorted(tuple1)))

# for e in tuple1:
#     print(e)

# for i,e in enumerate(tuple1):
#     print(i,e,sep="-->")

# tuple2 = (102,2,40)

# for a,b in zip(tuple1,tuple2):
#     print(a,b,sep="-->")

print(*(e for e in tuple1))