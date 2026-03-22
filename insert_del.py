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


# delete
var=np.array([1,2,3,4,5])
print(var)
d=np.delete(var,2)
print(d)


# 2d array
var22=np.array([
    [1,2,3,4],
    [5,6,7,8]
])

# To delete the first two columns (indices 0 and 1)
e1 = np.delete(var22, [0, 1], axis=1)
e2=np.delete(var22,[0],axis=0)
e=np.delete(var22,[0,1])
print(e)
print(e1)
print("e2 is", e2)

var33=np.array([
    [
        [1,2,3],
        [4,5,6]

    ],
    [
        [7,8,9],
        [10,11,12]
    ]]
)
# 9 is at the 8th index (counting from 0)
e3 = np.delete(var33, 8)
print(e3)
var44=np.array(
    [
    [
        [1,2,3],
        [4,5,6]

    ],
    [
        [7,8,9],
        [10,11,12]
    ]]
)
e4=np.delete(var44,[1,0],axis=0)
print(e4)

sheet1 = var44[0]
print(sheet1)
# This removes 7 and 10 specifically
e44 = np.delete(var44, [6, 9])
print(e44)
# This deletes the 0th column from BOTH sheets
e45 = np.delete(var44, 0, axis=2)
#axis0 depth axis1rows axiscolumns

print(e45)
# You cannot have a 3D array where one sheet has 3 columns and the other sheet has 2 columns. NumPy arrays must be perfectly "rectangular" (uniform) in their dimensions.