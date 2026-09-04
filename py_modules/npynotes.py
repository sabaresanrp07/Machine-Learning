#https://numpy.org/doc/stable/user/index.html (numpy guide)

import numpy as np

# print(np.__version__)

# Array (50x faster than list)
# We can perform vectorized operation

##________________________________________________________________________________________________________________________

#Basic array

# zeros() (floating . num)
# arr = np.zeros(3)
# print(arr)

# ones()
# arr = np.ones(2)
# print(arr)

# empty() (give random value from memory)
# arr = np.empty(2)
# print(arr)

# arange(sta , end , step) create array with a range of elem
# arr = np.arange(4)
# print(arr)

# linspace() create arr with specific interval
# arr = np.linspace(0,10,num = 4)
# print(arr)



##________________________________________________________________________________________________________________________

#0D Array (Scaler)
# arr = np.array(42)
# print(arr)

#1D Array (Vector)
# arr = np.array([1, 2, 3, 4, 5])
# print(arr)
# print(type(arr))

#2D Array (Matrix)
# arr = np.array([[1, 2, 3,4], [5, 6,7,8]])
# print(arr)

#3D Array
# arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
# print(arr)
# print(arr.ndim)#Tells the  dimension of the array

#n-D Array (n > 2 Tensor)
# arr = np.array([1, 2, 3], ndmin=5)#make the given array as given Dimenssion
# print(arr)
# print('number of dimensions :', arr.ndim)

##________________________________________________________________________________________________________________________

#Accessing array

#1D array (arr[col])
# arr = np.array([1, 2, 3, 4])
# arr[0] = 100
# print(arr)

#2D array (arr[row,col])
# arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
# print(arr[1])#2nd row
# print(arr[0,1])#2nd element on 1st row

#3D array (arr[row,col,depth])
# arr = np.array([[[1, 2, 3],
#                  [4, 5, 6]],
                  
#                  [[7, 8, 9],
#                   [10, 11, 12]]])
# print(arr[0, 1, 2])

##________________________________________________________________________________________________________________________

#Slicing array (slicing a list is copy but an array is view)

#1D array
# arr = np.array([1, 2, 3, 4, 5, 6, 7])
# print(arr[1::3])

#2D array
# arr = np.array([[1, 2, 3, 4, 5], 
#                 [6, 7, 8, 9, 10],
#                 [11, 12, 13, 14, 15]])
# print(arr[1, 1:])#arr[row selected , col sliced]
# print(arr[1:, 1:])#arr[row sliced , col sliced]

#3D array
# arr = np.array([[[1, 2, 3],
#                  [4, 5, 6]],
                  
#                  [[7, 8, 9],
#                   [10, 11, 12]]])
# print(arr[0:,1:,2:])#arr[row slic , col slic ,depth slic]

##________________________________________________________________________________________________________________________

#Data Types

#INT 
# arr = np.array([1, 2, 3, 4])
# print(arr.dtype)

#U (unicode string) N (number of characters) eg:-(U12,U6)
# arr = np.array(['1', 2, 3, 4])
# print(arr.dtype)#U21 (21 char)

# arr = np.array(['apple', 'banana', 'cherry'])
# print(arr.dtype)#U6 (6 char)

# arr = np.array(['apples_steav'])
# print(arr.dtype)#U12 (12 char)

#Chage dtype

# arr = np.array(['1','2','3','4'], dtype='i4') #i4 (interger 4bytes)
# print(arr)
# print(arr.dtype)

# arr = np.array(['1','2','3','4']) 
# print(arr.dtype)
# newarr=arr.astype('i')#Privent orginal array
# print(newarr.dtype)

##________________________________________________________________________________________________________________________

#Copy / View

#copy() doesn't affact original array 
#view() is just view of original arr

# arr = np.array([1, 2, 3, 4, 5])
# x = arr.copy()
# y = arr.view()
# arr[0] = 42
# print("arr",arr)
# print("x copy of arr",x)
# print("y view of arr",y)

##________________________________________________________________________________________________________________________

#Shape of arr

#2D arr
# arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
# print(arr.shape)

#3D array (row,col,depth)
#                   col1    , col2
# arr = np.array([[[1, 2, 3 ],[4, 5, 6]], #row 1 
#                 #(3 depth^)
#                 [[7, 8, 9],[10, 11, 12]]]) #row 2
# print(arr.shape)

#4D array(a,row,col,depth)
# arr = np.array([[[[1, 2, 3],[4, 5, 6]],
#                   [[7, 8, 9],[10, 11, 12]]],
 
#                   [[[13, 14, 15],[16, 17, 18]],
#                   [[19, 20, 21],[22, 23, 24]]]])
# print(arr.shape)

# arr = np.array([[[[[[[[[[1,2,3,4]]]]]]]]]])
# print(arr.shape)
# print(arr.size)

#Array re-shape
# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
# newarr1 = arr.reshape(4, 3)#(4x3 = 12 so we need 12 elements)
# newarr2 = arr.reshape(2,2,3)#(2x2x3 = 12)
# newarr3 = arr.reshape(2,1,-1)#-1 is unknow numpy fits a num by itself
# print(newarr1)
# print(newarr2)
# print(newarr3)

##________________________________________________________________________________________________________________________

# matrix multiplication

# A = np.array([[1,2],
#               [3,4]])

# B = np.array([[5,6],
#               [7,8]])

# print(A @ B)

##________________________________________________________________________________________________________________________







