import numpy as np
mat=np.matrix([
    [1,2,3],
    [4,5,6]
]
)
print(mat)
print(type(mat))
arr=np.array([
    [1,2,3],
    [4,5,6]
]
)
print(arr)
print(type(arr))

var1=np.matrix(
    [
        [1,2,3],
        [4,5,6]
    ]
)
var2=np.matrix(
    [
        [7,8,9],
        [10,11,12]
    ]
)
print("matrixx addition" , var1+var2)

# For matrix multiplication to work, the number of columns in the first matrix must equal the number of rows in the second matrix.
# print("matrixx multiplication" , var1*var2)


var3=np.matrix(
    [
        [1,2,3],
        [4,5,6],
        [8,9,10]
    ]
)
var4=np.matrix(
    [
        [7,8,9],
        [10,11,12],
        [11,12,13]
    ]
)
print("matrixx multiplication" , var3*var4)

# dot product hota hai
print(var3.dot(var4))
print(type(var3))   #matrix
print(var3.dtype)   #matrix k elements ki dtpe ..jaise int64