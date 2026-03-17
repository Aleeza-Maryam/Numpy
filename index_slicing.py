import numpy as np
var=np.array([1,2,3,4])
print(var[2])
# negative indexing startsfrom -1 frm right
print(var[-1])

# 2d array

var2=np.array([
    [1,2,3],
    [4,5,6]
])
print(var2[1,2])
print(var2[1])        #full row retrieve
# 3d array

var3=np.array([
    [
        [1,2,3],
        [4,5,6]
    ],
    [
    [7,8,0],
    [10,11,12]
    ]
])
print(var3)
# 2ndmatrix ka 11 chahiye

print(var3[1,1,1])
print(var3[0])   #pora 1st matrix
print(var3[0,1,])     #comma lgao end pe ya na lgao


#------------------------------------------------- slicing-------------------------------------------------------
# 1d array
sl1=np.array([1,2,3,4])
print(sl1[1:3])
print(sl1[1:])
print(sl1[:])

# step / jump
sl2=np.array([1,2,3,4,5,6,7,8,9,10])
print(sl2[::2])          #1 word ki jump
print(sl2[2:8:1])