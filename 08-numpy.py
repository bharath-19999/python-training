# Example-1
# import numpy as np
# print(np.__version__)

# Example-2
# import numpy as np
# arr1 = np.array([100,200,300])
# arr2 = np.array([[10,20,30],
#                 [20,40,50],
#                 [30,60,70]])
# arr3 = np.array([[[1,2,3]]])
# print(arr1.shape)
# print(arr1.dtype)
# print(arr1.ndim)

# Eaxmple-3
# import numpy as np
# arr1 = np.zeros((2,3))
# print(arr1)

# arr2 = np.ones((3,3))
# print(arr2)

# arr3 = np.eye(3)
# print(arr3)

# arr4 = np.arange(0,10,1)
# print(arr4)

# arr5 = np.arange(0,10,2)
# print(arr5)

# arr6 = np.linspace(0,1,4)
# print(arr6)

# arr7 = np.array([1,2,3,4,5],dtype=int)
# print(arr7)

# Example-4
# import numpy as np
# arr8 = np.full(5,3)
# print(arr8)
# arr9 = np.full((2,2),5)
# print(arr9)

# Example-5
# import numpy as np
# list1 = np.array([10,20,30,40,50])
# print(list1[0:2])
# print(list1[:3])
# print(list1[:0+1])
# print(list1[2:])
# print(list1[2:5])
# print(list1[-1])
# print(list1[-4:])
# print(list1[-5:-1])
# print(list1[::2])
# print(list1[::3])
# print(list1[::-1])
# print(list1[::-2])
# print(list1[::-3])

# list2 = np.array([[10,20,30],
#                   [40,50,60],
#                   [70,80,90]])
# print(list2[0][0], list2[0,0])
# print(list2[1][1], list2[1,1])
# print(list2[2][2], list2[2,2])

# print(list2[:,1])
# print(list2[:,0])
# print(list2[:,2])
# print(list2[:,0:2])
# print(list2[:,1:3])
# print(list2[:,1:])

# print(list2[:,1])       # [20,50,80]
# print(list2[0:1:,1])
# print(list2[0:2:,1])

# import numpy as np
# arr1 = np.array([10,20,30])
# arr2 = np.append(arr1,40)
# print(arr1)
# print(arr2)
# arr1 = np.array([10,20,30])
# arr2 = np.append(arr1,[40,50])      # added 40 50 to the array 
# print(arr1)
# print(arr2)
# arr1 = np.array([1,2,3,4,5])        # [100,1000,1000,4,5]
# arr1[0] = 100                       # update 100 at paticular index
# arr1[1:3] = 1000                    # update 1000 within that range
# arr1[arr1 <100] = 10000             # update 10000 where ever the condition met
# print(arr1)

# arr1 = np.array([1,3,4,5])
# arr2 = np.insert(arr1,1,2)
# print(arr2)
# arr1 = np.array([1,2,3,4,5])
# arr2 = np.delete(arr1,1)
# print(arr2)

# arr2 = np.delete(arr1,[2,4])
# print(arr2)

# import numpy as np
# arr1 = np.array([[10,20,30],
#                  [40,50,60]])
# row3 = [70,80,90]
# arr2 = np.vstack((arr1,row3))
# print(arr2)
# arr1 = np.array([[10,20],
#                  [40,50],
#                  [70,80]])
# col3 = np.array( [[30],[60],[90]] )
# arr2 = np.hstack((arr1,col3))
# print(arr2)