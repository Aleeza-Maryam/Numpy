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
    n=int(input("Enter 5 numbers:"))
    l.append(n)

print(np.array(l))