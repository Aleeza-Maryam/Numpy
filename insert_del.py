import numpy as np
var1=np.array([1,4,2,6,4])
x=np.insert(var1,2,1)
print(x)

y=np.insert(var1,(2,3,1),4)
print(y)
z=np.insert(var1,(2,3,4,1),4.5)
print(z)

# 2d aray
var2=np.array([
    [5,4,3,6],
    [9,8,6,4]
])
v1=np.insert(var2,1,7,axis=1)
print(v1)

v2=np.insert(var2,1,[7,1],axis=1)
print(v2)

# Row 0 ke index 3 par 7, aur Row 1 ke index 3 par 0 insert karna
v11 = np.insert(var2, 3, [7, 0], axis=1)
print(v11)
v12=np.insert(var2,2,[1,1],axis=0)
print(v12)