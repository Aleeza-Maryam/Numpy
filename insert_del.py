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
v12=np.insert(var2,2,1,axis=0)
print(v12)


var3=np.array(

[
     [
        [1,2,3,4],
        [5,6,7,8]
    ],
    [
        [9,20,11,12],
        [13,42,23,45]
    ]
]
   
)

#Axis 0: Nayi "Layer" Insert Karna
vaxis0=np.insert(var3,1,[[10,20,30,14]],axis=0)
print(vaxis0)
# vaxis0 = np.insert(var3, 1, nayi_layer, axis=0) Simple Alfaz Mein: Axis 0: Matlab ek naya Page add karna. Index 1: Matlab purane Page 0 aur Page 1 ke darmiyan naya page rakhna.



# Agar aap axis=1 use karte hain, toh har layer ke andar ek nayi row insert hogi.
vaxis1=np.insert(var3,1,[10,20,30,40],axis=1)
print(vaxis1)

# Har row ke index 1 par '99' insert karna
v_axis2 = np.insert(var3, 1, 99, axis=2)
print(v_axis2)