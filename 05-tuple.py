# collection of hetrogeneous elements
# ordered
# mmutable
# () / tuple() constructor

# import sys
# list1 = [10,20,30,40]
# tuple1 = (10,20,30,40)
# print(sys.getsizeof(list1))
# print(sys.getsizeof(tuple1))

# tuple1 = 10,20,30,40,50
# e1,e2,e3,e4,e5 = tuple1
# print(e1,e2,e3,e4,e5)

# t1 = (10,)    # tuple
# print(type(t1))
# print(t1)

# t1 = 10,20,30,40,50
# e1,*l2,e5 = t1  # l2 = [20,30,40]
# e2,*l3,e4 = l2  # l3 = [30]
# e3,*l4 = l3     # l4 = []
# print(e1,e2,e3,e4,e5)
# print(l2)
# print(l3)
# print(l4)

# t1 = 10,20,30,40,50
# list1 = list(t1)
# print(list1)      # conversion posible

# list1 = ["python","GenAi","ML","DL"]
# t1 = tuple(list1)
# print(t1)

# t1 = 10,50,20,40,30,10
# print(len(t1))
# print(sum(t1))
# print(max(t1))
# print(min(t1))
# print(t1.count(10))
# print(t1.index(20))
# print(sorted(t1))
# print(t1)
# # t1.sort(t1)  not available in tuple

# t1 = 10,20,30,40,50,None
# print(sorted(t1))   # TypeError: '<' not supported between instances of 'NoneType' and 'int'
                    # same with strings and int

# t1 = 10,200,300,4000,59000
# t2 = 100,290,39,390,50
# for element in t1:
#     print(element)

# for _ in t1:
#     print("Hello")

# print(*("Hello" for _ in t1))

# for e1,e2 in zip(t1,t2):    # zip function used to iterate more than one function
#     print(e1,e2,sep="----->")

# for i,e in enumerate(t1):   # when we want index and element we go for enumerate build in function
#     print(i,e,sep="--->")

# t1 = ((10,20,30),
#       (40,50,60),
#       (70,80,90))
# for inner in t1:      # two iterations
#     for e in inner:
#         print(e,end=" ")

# def test():
#     num1,num2 = 10,20
#     return num1+num2,num1-num2,num1*num2,num1/num2,num1,num2
# res = test()
# add,sub,mul,div,n1,n2 = res
# print(add,sub,mul,div,n1,n2)

# t1 = 10,20,30
# print(30 in t1)
# print(300 in t1)  # to check the element present or not 

# d1 = {
#     (10,20) : (30,40)
# }
# print(d1[(10,20)])

# t1 = 10,20
# t2 = 30,40
# t3 = t1 + t2    # (10,20,30,40)
# print(t3)
# t4 = t3 * 2
# print(t4)       # (10,20,30,40,10,20,30,40)

# t1 = 10,30,40
# t1[0] = 1000    # immutable
# print(t1)

# t1 = 10,20,30,40
# t2 = t1 + (50,)
# print(t2)       # add at end, but in another tuple

# res = t2[:2] + (25,) + t2[2:]
# print(res)      # add at middle,nut in anothe tuple