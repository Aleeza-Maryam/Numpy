import numpy as np
var=np.array([9,8,7,6,5,4])
print(var)
for i in var:
    print(i)

# 2d array
var2=np.array([
    [1,2,3,4,5],
    [6,7,8,9,10]
])
for i in var2:
    print(i)

# 1 by 1 digit agr print krwana to
for j in var2:
    for k in j:
        print(k)

# 3d array

var3=np.array([
    [
        [1,2,3,4],
        [5,6,7,8]
    ],
    [
        [7,6,5,4],
        [9,8,7,6]
    ]
])
print(var3)
for i in var3:
    for j in i:
        for k in j:
            print(k)