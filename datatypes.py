import numpy as np

arr=np.array([1,2,3,4])
print(arr,arr.dtype)

float1=np.array([1.0,2.0,3.0,4.0])
print(float1,float1.dtype)

string=np.array(["hy","heello","halo"])
print(string,string.dtype)

combo=np.array([1.0,2.0,"hyy",1,2])
print(combo,combo.dtype)


# changing datatypes

x=np.array([1,2,3,4])
print("Datatype before change:",x.dtype)
x1=np.array([1,2,3,4],dtype=np.int8)
print("Datatype after change:",x1.dtype)

x2=np.array([1.0,22.0,3.0],dtype=np.float32)
print("datatype of float after change",x2.dtype)

# using charactters change datatype

x3=np.array([1,2,3,4],dtype="S")
print("datatype of x3",x3.dtype)

x4=np.array([1.0,2.0,3.0,4.0],dtype="i")
print("datatype of x4",x4.dtype)

# as a function
# int -> float ->int

int1=np.array([1,2,3,4])
print("datatye before change ",int1.dtype)
new=np.float16(int1)
print("Datatype after change",new.dtype)
int2=np.int_(new)
print("data type of float to int",int2.dtype)




# directly conversion
x5 = np.array([1,2,3,4])
newd = x5.astype(float)

print(x5)
print(newd)

x6=np.array([1.0,2.0,3.0])
# x6_new=x6.astype(float)  #string ko float me convert nahi kar sakte isliye error aayega
x6_new=x6.astype(str)
print(x6)
print(x6_new)