import numpy as np
var=np.array([1,2,3,4])
print(var.shape)

var2=np.array([
    [1,2,3,4],
    [5,6,7,8]
])
print(var2.shape)

var2=np.array([1,2,3,4],ndmin=4)
print(var2)
print(var2.shape)  #means you now have a 4D array where the first three dimensions have a length of 1

# 1 d to multidimension

var3=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
x=var3.reshape(3,4)    #1d to 2d
print(x)
print(x.ndim)


# 1d to 3d
var4=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
y=var4.reshape(2,2,3)  #mtln 2 matrix bnein ge with 2 rws and 3 cols
print(y)
print(y.ndim)

# 3d to 1d
threed_to_one_d=y.reshape(-1)
print(threed_to_one_d)

var5=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
x1=var5.reshape(3,4)    #1d to 2d
print(x1)
print(x1.ndim)
two_to_oned=x1.reshape(-1)
print(two_to_oned)

