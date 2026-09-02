# s1 = {10,20,30,10,20}
# print(s1)

# s1 = {"Ravi","Ravi","ravi"}
# print(s1)

# list1 = [10,20,30,10,20]
# print(list(set(list1)))

# tuple1 = [10,20,30,10,20]
# print(tuple(set(tuple1)))

# s1 = {}           # empty dictionary
# print(type(s1))

# s2 = set()        # empty set
# print(type(s2))

# s1 = {10,20,30}
# s1.add(40)          # add - adding element to set
# list1 = [50,60,70]
# s1.update(list1)    # update - adding list/tuplr to set
# print(s1)
# tuple1 = (80,90)
# s1.update(tuple1)
# print(s1)

# s1. remove(10)      # remove - remove element(ERROR)
# s1.remove(100)      # ERROR
# s1.discard(100)     # discard - remove element(NO ERROR),safe func

# x = s1.pop()        # remove random element
# s1.clear()          # remove all elements

# s1 = {1,2,3}
# s2 = {3,4,5}
# print(s1.union(s2))     # all elements
# print(s2.union(s1))
# print(s1 | s2)

# print(s1 & s2)          # only common elements
# print(s1.intersection(s2))
# print(s2.intersection(s1))

# print(s1 - s2)          # give all the elements which are diff from the s2
# print(s1.difference(s2))
# print(s2.difference(s1))

# print(s1 ^ s2)          # give only the diff elements in both
# print(s1.symmetric_difference(s2))
# print(s2.symmetric_difference(s1))

# s1 = {1,2,3}
# s2 = {1,2}
# print(s2.issubset(s1))
# print(s2 <= s1)
# print(s1.issuperset(s2))
# print(s1 >= s2)

# s3 = {1,2,3}
# s4 = {4,5,6}
# print(s3.isdisjoint(s4))

# s1 = {10,20,30,40,50}
# print(len(s1))
# print(30 in s1)
# print(300 not in s1)

# set compresion
# eg: search a book in liberary
# s1 = {1,2,3,4,5}
# res = set()
# for element in s1:
#     res.add(element*element)
# print(res)
# print( {element*element for element in s1} )
# print( {element*element for element in s1 if element%2 == 0} )
