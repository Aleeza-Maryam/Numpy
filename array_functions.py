import numpy as np
var1=np.array([5,4,3,7,8])
np.random.shuffle(var1)
print(var1)

# 2d array
var2=np.array([
    [2,3,45,5],
    [7,5,4,3]
])
np.random.shuffle(var2)
print(var2)

# unique
var3=np.array([5,4,3,5,6,7,5,6])
print("unique elements",np.unique(var3))
# index
print("unique numbers with index ",np.unique(var3,return_index=True))
# counting
print("unique number with index and counts ",np.unique(var3,return_index=True,return_counts=True))


# resize (1d se 2d array bn jae ga)
var4=np.array([1,2,3,2,4,5,8,9,10])
x=np.resize(var4,(2,4))
print(x)

var_3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

# 3D se 2D mein convert karna (2 rows, 6 columns)
var_2d = np.resize(var_3d, (2, 6))
print(var_2d)
print("3D Array Shape:", var_3d.shape)

# flatten (ki bhi simension hai usko 1d mai convert)
var5=np.array([
    [1,2,3,4],
    [4,6,7,8]
])
print("Flatten ",var5.flatten())

# order {c , f , a , k}
print("order C , rowwise , by-default",var5.flatten(order="C"))
print("order F , colwise ,",var5.flatten(order="F"))
print("order A , auto , ",var5.flatten(order="A"))
print("order K , ram mai jaise prra wa , ",var5.flatten(order="K"))


# ravel (same flatten kisi bhi dimension ko 1d mai convert krta)
print("Ravel ",np.ravel(var5))
print("Ravel with order ",np.ravel(var5,order="A"))
print("order F , colwise ,",var5.ravel(order="F"))