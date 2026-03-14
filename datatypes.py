import numpy as np

arr=np.array([1,2,3,4])
print(arr,arr.dtype)

float=np.array([1.0,2.0,3.0,4.0])
print(float,float.dtype)

string=np.array(["hy","heello","halo"])
print(string,string.dtype)

combo=np.array([1.0,2.0,"hyy",1,2])
print(combo,combo.dtype)