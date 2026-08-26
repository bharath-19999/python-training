"""
class : collection of variables and functions
"class" is the keyword used to declare the class
"pass" is the keyword used to declare empty class
we can create object to the class
object = memory
instance - separate copies are there. copy1 changes other copies no effect eg: xerox

"""
# example-1
# class Test:
#     pass
# obj = Test()
# print(id(obj))

# class test:
#     num1 = 100   # instance
# obj1 = test()    # to get memory
# x = obj1.num1
# print(x)

# example-2
# class test:
#     num1 = 100
# obj1 = test()
# obj1.num1 = 1000
# obj2 = test()
# x = obj2.num1
# print(x)

# example-3
# class test:
#     num1 = 200
#     num2 = 100
# obj1 = test()
# x = obj1.num1
# y = obj1.num2
# add = x + y
# print(f"add : {add}")
# sub = x - y
# print(f"sub : {sub}")
# mul = x * y
# print(f"mul : {mul}")
# div = x/y
# print(f"div : {div}")

# example-4
""" constructor """
# constructor - initialize the instance variables dynamically
# self - self representing instance
# eg: ATM
# class test:
#     def __init__(self,param1,param2):
#         self.num1 = param1
#         self.num2 = param2
# obj1 = test(200,100)
# x = obj1.num1
# y = obj1.num2
# mul = x * y
# print(f"mul : {mul}")

# example-5
# while declaring the class i donn't know num1 num2. 
# class test:
#     def __init__(self):
#         pass
# obj1 = test()
# obj1.num1 = 100
# obj1.num2 = 20
# x = obj1.num1
# y = obj1.num2
# sub = x - y
# print(f"sub : {sub}")

# example-6
# class test:
#     def addition1(self):
#         num1 = 10
#         num2 = 20
#         res = num1 + num2
#         print(f"add : {res}")
#     def addition2(self):
#         num1 = 10
#         num2 = 20
#         res = num1 + num2
#         return res
#     def addition3(self,param1,param2):
#         res = param1 + param2
#         print(f"add : {res}")
#     def addition4(self,param1,param2):
#         res = param1 + param2
#         return res
# obj1 = test()
# obj1.addition1()
# x = obj1.addition2()
# print(f"add : {x}")
# obj1.addition3(10,20)
# y = obj1.addition4(10,20)
# print(f"add : {y}")


# Example 8

# class Parent:
#     x = 10
# class Child(Parent):
#     y = 20
# obj = Child()
# num1 = obj.x
# num2 = obj.y
# print(num1+num2)

# example 9
# class Parent:
#     def __init__(self,param1):
#         self.num1 = param1
# class Child(Parent):
#     def __init__(self,param1,param2):
#         super().__init__(param1)
#         self.num2 = param2
# obj = Child(200,100)
# print(obj.num1 + obj.num2)

# example 10
# class Parent:
#     def square(self):
#         num1 = 100
#         res = num1 * num1
#         print(res)
#         return res
# class Child(Parent):
#     def cube(self):
#         num1 = 100
#         #res = num1 * num1 * num1
#         res = super().square() * num1
#         print(res)

# class Subchild(Child):
#     def multiplication(self):
#         num1 = 100
#         num2 = 200
#         res = num1 * num2
#         print(res)

# obj = Subchild()
# obj.square()
# obj.cube()
# obj.multiplication()

# example 11
# class Parent1:
#     num1 = 10
# class Parent2:
#     num2 = 20
# class Child(Parent1,Parent2):
#     num3 = 30
# obj  = Child()
# print(obj.num1+obj.num2+obj.num3)

# example 12
# class Parent1:
#     num1 = 100
# class Parent2:
#     num1 = 200
# class Child(Parent1,Parent2):
#     num1 = 300
# obj = Child()
# print(obj.num1)  # 300

# example 13
# class Parent:
#     def test1(self):
#         print("Hello")
# class Child1(Parent):
#     def test2(self):
#         print("Batch-4")
# class Child2(Parent):
#     def test2(self):
#         print("Python...!!")
# obj = Child1()
# obj.test1()
# obj.test2()
# obj1 = Child2()
# obj1.test1()
# obj1.test2()

# example 14
# class Parent:
#     x = 10
# class Child1(Parent):
#     y = 20
# class Child2(Parent):
#     y = 200
# class Subchild(Child1,Child2):
#     z = 2000
# obj = Subchild()
# print(obj.x,obj.y,obj.z)

# example 15    method overriding       (polymorphism)
# class Parent:
#     def db_conn(self):
#         print("oracle conn soon")
# class Child(Parent):
#     def db_conn(self):
#         print("postgress conn soon")   
# obj = Child()
# obj.db_conn()

# example 16 method overloading
# class Test:
#     def __init__(self):
#         pass
#     def __init__(self,param1):
#             self.param1 = param1
#     def __init__(self,param1,param2):
#                 self.param1 = param1
#                 self.param2 = param2
# obj = Test(10,20)
# print(obj.param1 + obj.param2)

# class Test:
#     def add(self,a,b):
#         print(a)
#     def add(self,a,b,c):
#         print(a + b + c)
# obj = Test()
# obj.add(1,2,3)

# class Test:
#     def add(self,*param1):
#         print( sum(param1) )
# obj = Test()
# obj.add(1,2)
# obj.add(4,5,6)  # to acheive the overloading we use tuple

# private
# class Test:
#     def __init__(self):
#         self.__balance = 50000
# obj = Test()
# obj.__balance

# # example 18   encapsulation
# class Bank:
#     def __init__(self,balance):
#         self.__balance = balance
#     def get_balance(self):
#         return self.__balance
#     def set_balance(self,new_balance):
#         self.__balance = new_balance
# obj = Bank(50000)
# print(obj.get_balance())
# obj.set_balance(100000)
# print(obj.get_balance())

# class Bank:
#     def __init__(self,balance):
#         self.__balance = balance
# b = Bank(20000)
# print(b.__balance)   # cann't print the private variables

# class Bank:
#     def __func(self):
#         print("Hello")
# obj = Bank()
# obj.__func()    # cann't call the private funtions

# class Bank:
#     def __func(self):
#         print("Hello")
#     def func2(self):
#         self.__func()   # achevied by calling private funtion from public function
# obj = Bank()
# obj.func2()

# example 19
# class Test:
#     clg_name = "CBIT"   # class level variables
# print(Test.clg_name)

# example 20
# class Test:
#     clg = "CBIT"   # class variable
#     def __init__(self,name): 
#         self.x = name
# obj1 = Test("Std1")
# obj2 = Test("Std2")
# print(obj1.x,Test.clg,sep="--->")
# print(obj2.x,Test.clg,sep="--->")

# example 21
# class Test:
#     pass
# obj1 = Test()
# obj1.x = "Hello"    # instance variable
# print(obj1.x)   # access instance variable

# empty class with add/access instace variable
# class Test:
#     pass
# obj = Test()
# obj.num1 = 100
# obj.num2 = 200
# print(obj.num1 + obj.num2)

# class Test:
#     def __init__(self):
#         num1 = 100
#         num2 = 200
# obj = Test()
# print(obj.num1 + obj.num2)

# class Demo:
#     pass
# Demo.clg = "CBIT"   # add class variable
# print(Demo.clg )    # access class variable

# example-23
# class Demo:
#     pass
# Demo.num1 = 100 # class variables
# Demo.num2 = 200 # class variable
# obj1 = Demo()
# print(obj1.num1 + obj1.num2) # instace variable, but no declaration 

# example-24
# class Demo:
#     pass
# obj1 = Demo()
# Demo.num1 = 2000
# # obj1.num1 = 100
# print(obj1.num1)
# print(Demo.num1)

# example-25
# class Test:
#     clg = "CBIT"
# Test.clg = "CBIT college" 
# obj = Test()
# print(obj.clg)  # class variable modified with instance

# example-26
# class Test:
#     clg = "CBIT"
#     @classmethod    # decorator
#     def change_clg(cls,new_clg):
#         cls.clg = new_clg
# Test.change_clg("CBIT College")
# print(Test.clg)
# obj = Test()  # CBIT College
# print(obj.clg)    # CBIT College

# example-27
# from abc import ABC,abstractmethod
# class Test(ABC):
#     @abstractmethod         # parent class don't know the implementation. child class knows it. with the help of 329 and 331 we acheive it
#     def add(self):
#         pass
# class Child(Test):
#     def add(self):
#         num1 = 200
#         num2 = 100
#         res = num1 + num2
#         print(res)
# obj = Child()
# obj.add()

