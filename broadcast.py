import numpy as np
var1=np.array([1,2,3,4])
var2=np.array([1,2,3])
# print(var1+var2)   #error aae ga

var3=np.array([1,2,3])      #1x3
var4=np.array([[1],[2],[3]])    #3x1       1 aur 3 common hain
print("additin of var3 var4 is ",var3+var4)
print(var3.shape)
print(var4.shape)

var5=np.array([1,2,3,4])
print(var5)
print(var5.shape)
var6=np.array([
    [1],
    [2],
    [3],
    [4]
])
print(var6)
print(var6.shape)
print(var5-var6)


var7=np.array([1,2,3])
print(var7)
print(var7.shape)
var8=np.array([
    [1],
    [2],
    [3],
    [4]
])
print(var8)
print(var8.shape)
print(var7+var8)