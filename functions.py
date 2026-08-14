# no parameters no return
# def test():
#     print("Hello")
# test()

# with parameters no return
# def test(param1, param2):
#     print(f"Hello....{param1},{param2}")
# test("cbk","csk")

# no paramerter with return
# def test():
#     num1 = 10
#     num2 = 20
#     sum = num1+num2
#     return sum
# x = test()
# print(x)

# with parameters with return
# def test(param1,param2,param3):
#     sum = param1+param2+param3
#     return sum
# x = test(10,45,56)
# print(x)

# ---------------------------------------------

# 1. normal parameter
# 2. default parameter
# 3. variable-length parameter
# 4. keyword parameter
# def test(a,b=15):
#     n = a+b
#     return n
# i = test(13,24) 
# print(i)

# def test(num,name="rama",*param1,**param2):
#     print(f"{num}....{name}....{param1}....{param2}")
# test(12,32,3,23,232,5,43,2,2,4,n="bharath")

# ----------------------------------------------------------

# Lambda functions
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
# res = is_anagram("Heart","EARth")
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



"""    class  """
# def test():
#     print("welcome to funtions!!") 

# test()

""" no parameter no return type"""
# def addition():
#     num1 = 10
#     num2 = 20
#     res = num1 + num2
#     print(f"Addition : {res}")
# addition()

""" no parameter with return type"""
# def addition():
#     num1 = 100
#     num2 = 200
#     res = num1 + num2
#     return res
# x = addition()
# print(f"Addition : {x}")

""" with parameter no return type"""
# def addition(num1,num2):
#     res = num1 + num2
#     print(f"Addition : {res}")
# addition(100,200)

""" with parameter with return type"""
# def addition(num1,num2):
#     res = num1 + num2
#     return res
# x = addition(200,100)
# print(f"Addition : {x}")


""" keyword parameter"""
# def db_func(username,password):
#     res = "Login Success" if username == "vpro" and password == "Vpro@123" else "Login Failed"
#     return res
# res = db_func(password = "Vpro@123", username = "vpro")
# print(res)

""" variable length parameter"""
# def test(*param1):
#     print(sum(param1))
# test(10,20)

# def test(*param1,*param2):  #err

""" combination of positional parameter and variable length parameter"""
# def test(param1,param2,*param3):
#     print(param1,param2,param3)
# test(1,2,3,4)

# def test(*param1):
#     return sum(param1)
# x = test(10,20,30)
# print(f"sum : {x}")

""" Default parameter """
# def test(param1="Hello"):
#     print(param1)
# test()
# test("Welcome")
# test(None)

"""  order """
# def test(p1,p2,p3=100,p4=50,*p5):
#     print(p1,p2,p3,p4,p5)
# # test()
# test(10,20)
# test(10,20,200,300,1,2,3)
""" tricky"""
# def test(p1,p2=100,p3=()):
#     print(p1,p2,p3)
# test(p1=10,p3=(100,1000))

# def test(p1,p2=100,*p3):  # unhappy point - unjustification
#     print(p1,p2,p3)
# test(p1=10,p3=(100,1000))

""" keyword length parameter """
# def test(**param1):
#     print(param1)
# test(x=10,key2=20)

# def test(p1,p2=100,*p3,**p4):
#     print(p1,p2,p3,p4)
# test(10,1000,2,3,4,5,key1=10,key2=400)

"""  lambda functions """
# x = lambda num1: num1*num1
# res = x(10)
# print(res)

# res = lambda num1:"even" if num1%2==0 else "odd"
# print(res(10))

# res = lambda x,y,z: x if x>y and x>z else y if y>z else z 
# print(res(10,20,30))

""" curring/closure"""
# outer = lambda num1: lambda num2: lambda num3:num1+num2+num3
# middle = outer(10)
# inner = middle(20)
# res = inner(30)
# print(res)