# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 08:42:20 2024

@author: yash
"""
#What is Numpy ?

#Arrays In Numpy
#Create ndarray
 
import numpy as np
arr = np.array([10,20,30])
print (arr)

#create a Multi-dimensional Array
arr = np.array([[10,20,30],[40,50,60]])
print(arr)








#Represent the Minimum Deminsions
#Use ndmin param to specvify how many minimum 
#dimemsions you wanted to create an array with
#MinimumDimension 

arr = np.array([10,20,30,40],ndmin = 3)
print(arr)

#Change the Data type
#dtype parameter 

arr = np.array([10,20,30],dtype = complex)
print(arr)

#Get the Dimensions of Array
arr = np.array([[1,2,3,4],[7,8,6,7],[9,10,11,12]])
print(arr.ndim)
print(arr)
###################################

#Finding the size of each item  in the array 
arr = np.array([10,20,30])
print("Each item contain in bytes : ",arr.itemsize)

#Get the size and shape of array
arr = np.array([[10,20,30,40,],[60,70,80,90]])
print("Array Size :",arr.size)
print("Shape :",arr.shape)

#Creation of array
arr = np.array([10,20,30])
print("Array : ",arr)

#Creating array fromm list with type float 

arr = np.array([[10,20,40],[30,40,50]], dtype = 'float')
print("Array created by using list :\n",arr)

#Create a squence of integers using arange()
arr = np.arange(0,20,3)
print("A sequential array with steps of 3: \n",arr)

#Acces single element usiing index 
arr = np.arange(11)
print(arr)
print(arr[2])
print(arr[-2])

print(arr[-5])

#Multi-Dimensional array Indexing 
#Access multi dimensional array element 
#using array indexing 
arr = np.array ([[10,20,30,40,50],[20,30,50,10,30]])
print(arr)
print(arr.shape)
print(arr[1,1])
print(arr[0,4])
print(arr[1,-1])

#Access array elements using slicing 
arr = np.array([0,1,2,3,4,5,6,7,8,9])
x = arr[1:8:2]
print(x)

x = arr[-2:3:-1]
print(x)

x = arr[-2:10]
print(x)

#Indexing in numpy 
multi_arr = np.array([[10,20,10,40],
                      [40,50,70,90],
                      [60,10,70,80],
                      [30,90,40,30]])
multi_arr

#Slicing array 
multi_arr[1,2]
multi_arr[1,:]
multi_arr[:,1]
x = multi_arr[:3,::2]
print(x)

""" 23 April 2024 """
# index array out of bound 
from numpy import array 
#define array
data = array([11,22,33,44,55])
#index data

#stack overflow 
#Holy python

print(data[5])

################################

#index row of two-dimensional array
from numpy import array 
data = array ([
    [11,22],
    [33,44],
    [55,66]])
print(data[0,])# 0th row and all columns 
#[11,22]

################################

#slice a one dimensional array 
from numpy import array
data = array([11,22,33,44,55,])
print(data[1:4])

################################

# negative slicing a one dimensional array 
from numpy import array
data = array([11,22,33,44,55,])
print(data[-2:])

################################ 

#split input and output data
from numpy import array
data = array([
    [11,22,33],
    [44,55,66],
    [77,88,99]])
#separeate data
X,y = data [:,:-1], data[:, -1]
X
y

################################
#brodcast scalar to one-dimensional array
from numpy import array
a = array([1,2,3])
print(a)
#define scalar 
b = 2
print(b)

# brodcast

c = a+b 
print (c)

################################
# vector L1 norm
""" vector l1 norm 
L1 norm is calculated as the sum of 
the absolute vector values,
where the absolute value of a scalar uses 
the notation |a|,
in effect, the norm 
is calculation of the manhattan distance 
from origin of the vector space 
||v1|| = |a1| +|a2| + |a3|
 """

from numpy import array
from numpy import norm
a = array([1,2,3])
print(a)
# calculate norm 
l1 = norm(a,1)
print(l1)

################################
# vector L52 norm
""" 
The notation for L2 norm of a vector x 
is ||x||power 
take the square root of the sum of the 
squarede vector values.
Another name for L2 norm is """

from numpy import array
from numpy import norm
a = array([1,2,3])
print(a)
# calculate norm 
l2 = norm(a)
print(l2)

################################
#triangular matrices
from numpy import array
from numpy import tril
from numpy import triu
#define square matrix
M = array ([
    [1,2,3],
    [1,2,3],
    [1,2,3]])
print(M)
M
# lower tringular matrix
lower = tril(M)
print(lower)
#upper triangular matrix
upper = triu(M)
print(upper)

################################
# diagonal matrix
from numpy import array
from numpy import diag
#define square matrix 
M = array ([
    [1,2,3],
    [1,2,3],
    [1,2,3]])
print(M)
# extract diagonal vector 
d = diag(M)
print(d)
# create diagonal matfrix from vector 
D = diag(d)
print(D)

################################
#identity matrix
from numpy import identity 
I = identity(3)
print(I)

################################
#orthogonal matrix
""" The matrix is said to be orthogonal matrix 
if the product of a matrix and its transpose 
gives an identity value """

from numpy import array
from numpy.linalg import inv
#define orthogonal matrix
Q = array ([
    [1,0],
    [0,-1]])
print(Q)
# inverse equivalence
V = inv(Q)
print(Q.T)
print(V)
#identity equivalance
I = Q.dot(Q.T)
print(I)
################################
from numpy import array 
A = array([
    [1,2],
    [3,4],
    [5,6]])
print(A)
#Calculate transpose
C = A.T
print(C) 

################################
""" 24 April 2024"""

# inverse matrix
from numpy import array 
from numpy.linalg import inv 
#define array 
A = array([
    [1.0,2.0],
    [3.0,4.0]])
print(A)
#inverse matrix
B = inv(A)
print(B)
#multiple A and B
I = A.dot(B)
print(I)

################################
#Sparse matrix
from numpy import array 
from scipy.sparse import csr_matrix
#craete dense matrix 
A = array([
    [1,0,0,1,0,0],
    [0,0,2,0,0,1],
    [0,0,0,2,0,0]])
print(A)

#Convert to sparse matrix (CSR method)
S = csr_matrix(A)
print(S)

# reconstruct dense matrix
B = S.todense()
print(B)

################################



################################












