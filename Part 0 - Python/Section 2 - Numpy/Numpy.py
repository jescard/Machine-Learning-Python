import numpy as np

#the basics
a = np.array([1,2,3], dtype = 'int16')
b = np.array([[1,2,3], [9,8,7]])

#Dimention
a.ndim
b.ndim

#Shape
a.shape
b.shape

#Get type
a.dtype

#Get size
a.itemsize

#Get Total size
a.nbytes

#Accessing/Changing specific elements
a = np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
#Get specific element [r,c]
a[1,5]
a[0,:]
a[:,2]
a[1,4] = 20
a[1,:] = 2
#[starting index: end index: steps]
a[0, 1:6:2]

#Initializing different types of array
#All zeros 
np.zeros((5,2))
#All ones
np.ones((2,3))
#Any other number
np.full((2,2), 99)
#Random Decimal
np.random.rand(4,2)
#Identity
np.identity(4)

#Copy array
b = a.copy()

#statistics
np.min(a)
np.max(a) 
np.sum(a)