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



# neditor function agr baar baar for loop ni lgana chahte
print("nditer")
var4=np.array([
    [
        [1,2,3,4],
        [5,6,7,8]
    ],
    [
        [7,6,5,4],
        [9,8,7,6]
    ]
])
for i in np.nditer(var4):
    print(i)

var5=np.array([
    [1,2,3,4],
    [5,6,7,8]
])
print("var5")
for i in np.nditer(var5):
    print(i)

# parameters
for i in np.nditer(var5,flags=['buffered'], op_dtypes="S"):    #buffered wle flag mai iterate wla data store hoga
    print(i)

# denumerate function se hum inde bhi sath print kr skte
for d,i in np.ndenumerate(var5):
    print(d,i)


var6=np.array([
    [
        [1,2,3,4],
        [5,6,7,8]
    ],
    [
        [7,6,5,4],
        [9,8,7,6]
    ]
])
for i,d in np.ndenumerate(var6):
    print(i,d)