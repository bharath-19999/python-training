"""   FUNCTIONS 
## Python Functions — Interview Notes

* Function: Reusable block of code that performs a specific task.
* Syntax: def function_name(parameters):
* Parameter: Variable defined in function.
* Argument: Actual value passed during function call.
* Positional argument: Matched by position → `add(10,20)`.
* Keyword argument: Matched by name → `add(a=10,b=20)`.
* Return: Sends a result back → `return result`.
* Default parameter: def greet(name="Guest").
* *args: Accepts multiple positional arguments as a tuple.
* **kwargs: Accepts multiple keyword arguments as a dictionary.
* Lambda: Anonymous single-expression function → `lambda x: x*x`.
* Built-in: Python-provided functions like `print()`, `len()`, `int()`, `sum()`.
* User-defined: Functions created using `def`.
* Recursive: Function calling itself.
* Higher-order: Function accepts/returns another function.
*   map(): Transforms elements.
*   filter(): Selects elements based on condition.
*   reduce(): Combines elements into one result; requires `functools`.
* Key interview point: Functions improve **code reuse, readability, modularity, and maintainability**.


Common Python built-in functions
| Function      | Purpose                 | Example                         |
| ------------- | ----------------------- | ------------------------------- |
| `print()`     | Display output          | `print("Hello")`                |
| `len()`       | Get length              | `len("Python")` → `6`           |
| `type()`      | Get data type           | `type(10)` → `int`              |
| `int()`       | Convert to integer      | `int("10")` → `10`              |
| `str()`       | Convert to string       | `str(10)` → `"10"`              |
| `float()`     | Convert to float        | `float("10.5")` → `10.5`        |
| `list()`      | Create/convert to list  | `list("abc")` → `['a','b','c']` |
| `tuple()`     | Create/convert to tuple | `tuple([1,2])`                  |
| `dict()`      | Create dictionary       | `dict(a=1)`                     |
| `set()`       | Create set              | `set([1,2,2])`                  |
| `sum()`       | Calculate sum           | `sum([1,2,3])` → `6`            |
| `max()`       | Find maximum            | `max([10,20,5])` → `20`         |
| `min()`       | Find minimum            | `min([10,20,5])` → `5`          |
| `sorted()`    | Sort values             | `sorted([3,1,2])`               |
| `abs()`       | Absolute value          | `abs(-10)` → `10`               |
| `round()`     | Round number            | `round(10.6)` → `11`            |
| `range()`     | Generate sequence       | `range(5)`                      |
| `enumerate()` | Index + value           | `enumerate(["a","b"])`          |
| `zip()`       | Combine iterables       | `zip([1,2],[3,4])`              |
| `map()`       | Transform elements      | `map(int, ["1","2"])`           |
| `filter()`    | Filter elements         | `filter(...)`                   |


"""


# User defiined functions
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
# functions without name
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

# Example -16
# print(list(map(lambda num1:num1*100,[1,2,3,4,5])))
# print ( list(map(lambda x,y:x+y,(1,2,3,4,5),(10,11,12,13,14))))
# print ( list(map(lambda num1,num2:num1-num2,[1,2],[10,11,12,13,14])))  # loop stop after 1,2
# print(list(map(int,"10 20 30 40 50".split())))
# res = map(lambda x:x**x,[1,2,3,4,5])
# x = list(res)
# print(x)
# y = list(res)
# print(y)

# print( tuple(filter(lambda num1:num1>=3,(1,2,3,4,5))))
# print( list (map(lambda num1:num1*num1, filter(lambda num1:num1%2==0, [1,2,3,4,5]))))
# print(list(map(None,[1,2,3,4,5])))
# res = map(lambda x: list(map(lambda y:y*2,x)),[[1,2],[3,4],[5,6]])
# print(list(res))
# from functools import reduce
# print(reduce(lambda num1,num2:num1+num2,[1,2,3,4,5]))

# from functools import reduce
# num = [1,2,3,4,5]
# print(list(map(lambda num:num*2,num)))
# print(list(filter(lambda num:num%2==0,num)))
# print(reduce(lambda num1,num2:num1*num2,num))

"""
map()    → can work with multiple iterables
map(function, iterable1, iterable2)
filter() → works with one iterable
filter(condition/function, iterable)
             ↓              ↓
       True/False       collection
lambda x: x > 3 → function
num1            → iterable

"""
# num1 = (1,2,3,4,5)
# num2 = (3,6,9,12,15)
# print(list(map(lambda x,y:x+y, num1, num2)))
# print(list(filter(lambda x,y:x+y, num1, num2))) # Error - here having 2 iterables i.e., num1,num2

# res = "the is and".split()
# print(res)    # ['the', 'is', 'and']


""" recursive function """
# function calling itself
# def countdown(n):
#     if n == 0:
#       return 
#     print(n)
#     countdown(n-1)
# countdown(5)

# def factorial(n):
#     if n == 0:
#         return 1
#     return n * factorial(n-1)
# print(factorial(5))

# def test_func(item,items=[]):
#     items.append(item)
#     return items
# print( test_func(10))  # [10]
# print( test_func(20))  # [10,20]

# def test_func(item,items=None):
#     if items is None:
#         items = []            # Reset
#         items.append(item)
#         return items
# print( test_func(10))
# print( test_func(20))
   
# list1 = [1,2,3]
# list2 = [1,2,3]
# print(list1 is list2)
# print(list1 == list2)

# list1 = [1,2,3]
# list2 = list1   # same memory location
# print(list1 is list2)
# print(list1 == list2)

# num1 = 100
# num2 = 100
# print(num1 is num2)
# print(num1 == num2)

# num1 = 257
# num2 = 257 
# print(num1 is num2)  # in old laptops it will br false
# print(num1 == num2)

# boolean is the child data type of integer
# print (True + False + True)
# print(isinstance(True,int))
# print(isinstance(False,int))
# print(isinstance(True,bool))

# print(True == 1)
# print(True is 1)

# list1 = [1,2,3]
# list2 = list1
# list2.append(4)   # list1 memory also updated
# print(list1)

# print( tuple(range(5)))
# print( list(range(1,10)))
# print( list(range(0,5,2)))
# print( list(range(10,0,-1)))
# print( list(range(5,0,-2)))

