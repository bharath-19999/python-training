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