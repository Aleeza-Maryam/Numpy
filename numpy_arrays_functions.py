import numpy as np

# filled array with zero

ar_zero=np.zeros(4)    #1 dimensional
print(ar_zero)

# 2d or multidimensional array
ar_zero_2d=np.zeros((2,3))
print(ar_zero_2d)
# multidimensional array with 3 dimensions
ar_zero_3d=np.zeros((2,3,4))
print(ar_zero_3d)

# (2,3,4) ka matlab:
# 2 blocks (matrices)
# 3 rows
# 4 columns

# filed with one
ar_one=np.ones(4)
print(ar_one)
# 2d
ar_one_2d=np.ones((2,3))
print(ar_one_2d)

# 3d
ar_one_3d=np.ones((3,2,2))
print(ar_one_3d)


# empty array
ar_empty=np.empty(4)
print(ar_empty)
# 2d
ar_empty_2d=np.empty((2,3))
print(ar_empty_2d)

# empty mai previously memory ka jo array hota wo fill ho jata

# range of elements
ar_range=np.arange(4)
print(ar_range)
# 2d array
ar_range_2d=np.arange(5,10)
print(ar_range_2d)       #np.arange(start, stop)  ..last wla exculde hota hai


# diagonal elements filled with 1's
ar_dia=np.eye(4)   #mtlb 4x4 ka array
print(ar_dia)

# dimensions ko pass
ar_da_dim=np.eye(3,4)   #3 rows and 4 columns
print(ar_da_dim)

# specified interval
ar_spec=np.linspace(0,10,5)
print(ar_spec)   #0 to 10 ke beech 5 equally spaced numbers

