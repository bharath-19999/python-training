"""
    dictionary
        store data in "key & value" pairs
        key and value separated by using ":"
        keys are "immutable"
        values are "mutable"
        we will represent using {} / dict()


"""



# d1 = {}
# print(d1)
# print(type(d1))

# d1 = {
#     "name" : "Emp1",
#     "dept" : "R&D",
#     "salary" : 10000,
#     "id" : 101
# }
# print(d1)
# # print(d1["name"])
# # # print(d1["Address"])  # error: address not present
# # print(d1.get("Address"))    # value ad 'None'
# # print(d1.get("Address","Hyderabad"))    # value as 'Hyderabad'
# print(d1.keys())
# print(d1.values())
# print(d1.items())


# d1 = {}
# d1["key1"] = "GenAi"
# d1["key2"] = "AgenticAi"
# print(d1)

# d1["key1"] = "Genarative Ai"
# print(d1)
# del d1["key1"]
# print(d1)


# d1 = {
#     "key1" : "Hello",
#     "key2" : "FDE",
#     "key3" : "QC"
# }
# for k in d1.keys():
#     print(k,end=" ")
# print("\n")
# for v in d1.values():
#     print(v,end=" ")
# print("\n")
# for k,v in d1.items():
#     print(k,v,sep="----->")


# d1 = {
#     "key1" : "Hello",
#     "key2" : "FDE",
#     "key3" : "QC"
# }
# print("key1" in d1)
# print("key4" in d1)
# d1.pop("key3")  # remove paticular key item
# print(d1)
# d1.popitem()    # remove last item
# print(d1)

# d1 = {
#     "d2" : {
#         "wish" : "Hello"
#     }
# }
# print(d1)
# print(d1["d2"]["wish"])

# for inner in d1.values():
#     for value in inner.values():
#         print(value)


# d1 = {
#     "d2" : {
#         "name" : "bharath"
#     }
# }
# print(d1["d2"]["name"])

# str = "Hello"
# count = {}
# for ch in str:
#     count[ch]=count.get(ch,0)+1
# print(count)

# str = "Hello"
# d = {}
# for ch in str:
#     d[ch] =d.get(ch,0)+1
# print(d)


# str = "java python java ml java python"
# words = str.split(" ")
# count = {}
# print(words)
# for w in words:
#     count[w] = count.get(w,0)+1
# print(count)

# d1 = {
#     "key1" : 100
# }
# d2 = {
#     "key2" : 200
# }
# d3 = {
#     "key3" : 200
# }
# d1.update(d2)
# d1.update(d3)
# print(d1)

# print( { x:x**x for x in range(1,6)})

















# list1 = [{"num1":10},
#          {"num2":20},
#          {"num3":30}]
# print(list1[0]["num1"] + list1[1]["num2"] + list1[2]["num3"])

# res = 0
# for d1 in list1:
#     for x in d1.values():
#         res += x
# print(res)

# d1 = {"a":10, "b":20, "c":10}
# print({ value:key for key,value in d1.items()})

# list1 = [10,20,30]
# list2 = list1.copy()
# list1.append(40)
# print(list2)

# list1 = [10,20]
# list2 = [30,40]
# list1.append(list2)
# print(list1)
# list1.extend(list2)
# print(list1)

# print( [1] * 3 )
# print([[]]*3)

# list1 = [[]] * 3
# list1[0].append(100)
# print(list1)


# list1 = [1,2,3,4,5]
# print(list1)
# for i in list1:
#     if i % 2 ==0:
#         list1.remove(i)
# print(list1)

# list1 = [10,20,30]
# list1.sort()    # change to original list
# print(list1)

# list2 = sorted(list1)
# print(list2)    # no change to original list


# list1 = [10,20,30,10,20,30]
# list2 = []
# for e in list1:
#     if e not in list2:
#         list2.append(e)
# print(list2)

# result = []
# for e in list1:
#     if result.count(e)==0:
#         result.append(e)
# print(result)


# t1 = ("hello")
# print(type(t1))

# t2 = ("hello",)
# print(type(t2))

# list1 = list("hello")
# print(type(list1))
# print(list1)

# str = "hello"
# res = lambda s : len(s)
# print(res(str))

