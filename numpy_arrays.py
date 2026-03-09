import numpy as np
# creating array
a=np.array([1,2,3,4,5])
print(a)

# or

b=[1,2,3,4,5]
c=np.array(b)
print(c)
print(type(c))

# user input se
l=[]
for i in range(1,5):
    n=int(input("Enter 4 numbers:"))
    l.append(n)

print(np.array(l))


# to check the dimension of array
print(a.ndim)

# to check the shape of array


# 2d array
e1=[[1,2,3,4]]
e=[
    [1,2,3,4],
    [5,6,7,8]]
e2=np.array(e)
print(e2.ndim)
print(e)


# 3d array
f=[[[1,2,3,4],[5,6,7,8],[9,10,11,1]]]
f1=np.array(f)
print(f1.ndim)


