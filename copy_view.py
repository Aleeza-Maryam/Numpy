import numpy as np
var=np.array([1,2,3,4])
co=np.copy(var)
print("Copy :",co)

var1=np.array([7,8,9,10])
vi=var1.view()
print("view:",vi)

print("Copy one ")
var7=np.array([4,5,6,7])
cop=np.copy(var7)
cop[0]=8
print('var7 ',var7)
print("copy ",cop)

print("view ")
var8=np.array([3,4,5,6])
vie=var8.view()
vie[0]=8
print("var 8",var8)
print("view ",vie)