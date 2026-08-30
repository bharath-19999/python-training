# Lists
# collection of indexed and hetrogeneous elements
# [] / list() constructor
# immutable
# slicing


# list1 = [10,20,30,40]
# e1,e2,e3,e4 = list1
# print(e1,e2,e3,e4)

# list1 = [10,20,30,40,-50]
# e1,*list2,e3 = list1
# print(e1,list2,e3)
# e4,*list3 = list2
# print(e4,list3)
# e6,*e7 = list3
# print(e6,e7)

# list = [10,20,30,40,-60]
# print(len(list))
# print(max(list))
# print(min(list))
# print(sum(list))

# list2 = [10,10,10,20,30,20,10,30,20]
# print(list2.count(10))

# list = [100,0,50]
# print(sum(list)/len(list))

# list4 = [10,50,40,30,5]
# res = sorted(list4)
# print(res)
# print(list4)  # no change to original list4

# list5 = [10,5,30,20,50]
# list5.sort()
# print(list5)    # change to the orginal list5

# list1 = [10,20,30]
# list1.append(40)
# print(list1)
# list1.insert(2,50)
# print(list1)
# list2 = [60,70]
# list1.extend(list2)
# print(list1)

# list1 = [10,20,30,10,20]
# print(list1)
# list1.remove(10) # remove first occuring element
# print(list1)
# list1.pop() # remove last element
# print(list1)
# list1.clear()   # remove all the elements
# print(list1)


# list1 = [10,20,30,40,50]
# print(list1)
# del list1[0]    # remove paticular element
# print(list1)

# # list1.remove(10)    # error
# del list1[1:3]
# print(list1)

# list1 = [20,30,40,50,-10]
# print(10 in list1) # checks element is there or Not
# print(300 in list1)

# list1 = [10,20,30,40,50]
# print(list1)
# print(list1[::-1])
# list1.reverse
# print(list1)

# list1 = [10,20,30,40,50]
# for i in list1:
#     print(i,end = " ")

# for index,e in enumerate(list1): # for indexed list we use enumerator
#     print(index,e,sep="-->")


# list1 = [1,2,3,4,5]
# list2 = [10,20,30,40,50]
# for e1,e2 in zip(list1,list2):
#     print(e1,e2,sep="------>")

# list1 = [10,20,30,40,50,60,70,80,90,100]
# print(list1[0:7:2])
# print(list1[1:6:2])
# print(list1[:1])
# print(list1[::2])
# print(list1[::-2])
# print(list1[::3])
# print(list1[::-3])

# list1 = [[10,20,30],[40,50,60],[70,80,90]]
# print(list1[0][0])
# print(list1[1][1])
# print(list1[2][2])
# for inner in list1:
#     for index,element in enumerate(inner):
#         print(index,element,sep="---->")
#     print("-----------")

# list1 = [[10,20],[30,40]]
# list2 = list1
# list1[0].append(30)
# print(list2)

# deep copy
# import copy
# list1 = [[10,20],[30,40]]
# list2 = copy.deepcopy(list1)
# list1[0][0]=100
# print(list1)
# print(list2)

# "==" - compare values
# "is" - compare memory
# list1 = [10,20,30]
# list2 = [10,20,30]
# list2 = list1
# print(list1 == list2)
# print(list1 is list2)

# list1 = [10,20]
# list2 = [30,40]
# list3 = list1 + list2
# print(list1)

# list1.extend(list2)
# print(list1)
# # '*' - externally performs concatination
# list3 = [*list1,*list2]
# print(list3)

# list1 = [10,20,30]
# list2 = list1 * 3
# print(list2)

# list1 = ["Hello",10,10.1,True,[10,20],(10,20),{"name":"Hello"},{10,20},None]
# print(list1)

# list1 = [10,20,30,10,20,40]
# list2 = []
# for element in list1:
#     if list1.count(element)>1:
#         list2.append(element)
# print(set(list2))