# search
import numpy as np
var=np.array([1,2,3,4,2,5,6,2,6,7])
x=np.where(var==2)
print(x)

x1=np.where(var%2==0)
print(x1)

# search sorted array
var1=np.array([1,2,3,4,5,6,7])
x1=np.searchsorted(var1,4)
print(x1)
x2=np.searchsorted(var1,7,side="right")
print(x2)

# list bhi pass kr skte
x3=np.searchsorted(var1,[4,5,6],side="right")
print(x3)

# sort array
var3=np.array([7,6,5,4,8,6,5,4,3])
x=np.sort(var3)
print(x)

var_4=np.array(['a','s','c','f'])
print("sort ",np.sort(var_4))

# 2d array
var5=np.array([
    [5,4,3,2],
    [5,6,7,8],
    [8,9,5,4]
])
print(np.sort(var5))
# filter array

var6=np.array(['f','a','g','h'])
f=[True,False,True,False]
new=var6[f]
print(new)
print(type(new))

var7=np.array(
    [4,5,6,7]
)
z=[True,True,False,True]
var8=var7[z]
print("result ",var8)




var_22d = np.array([
    [10, 20], # Row 0
    [30, 40], # Row 1
    [50, 60]  # Row 2
])

# Hume sirf 1st aur 3rd row chahiye
z1 = [True, False, True] 
res = var_22d[z1]
res1 = var_22d[var_22d > 25]
print(res)
print(res1)

