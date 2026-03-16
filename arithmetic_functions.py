import numpy as np
# min function
var1=np.array([1,2,3,4])
print("Min in array is ",np.min(var1))
# max
print("Max in array is ",np.max(var1))

# position of min
print("Position of min in var1 is ", np.argmin(var1))
print("Position of max in var1 is ", np.argmax(var1))

# 2d array mai min
var2=np.array([
    [1,2,3,4],
    [5,6,7,8]
])
print("Min in 2d array is ",np.min(var2,axis=0))  # 0 col  hai 1 row
print("Max in 2d array is ",np.max(var2,axis=1))
# position
print("min position in 2d is ",np.argmin(var2))
# np.argmax() maximum value ki position return karta hai. Is array me maximum value = 8 hai.
print("max position in 2d is ",np.argmax(var2))

# sqrt
print("Sqrt of var1 (1d) is ",np.sqrt(var1))
print("Sqrt of var2 (2d) is ",np.sqrt(var2))

# sin
print("Sin of var1 (1d) is ",np.sin(var1))
print("Sin of var2 (2d) is ",np.sin(var2))

# cos
print("cos of var1 (1d) is ",np.cos(var1))
print("cos of var2 (2d) is ",np.cos(var2))

# commulative sum
print("Commulative sum of var1",np.cumsum(var1))

# Default me NumPy 2d array ko 1D me treat karta hai.  [1 2 3 4 5 6 7 8]
print("Commulative sum of var2(2d) ",np.cumsum(var2))