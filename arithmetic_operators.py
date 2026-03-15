import numpy as np
# arithmetic operators
a=np.array([1,2,3,4])
addition=a+6
print("Addition:",addition)
subtraction=a-6
print("Subtraction:",subtraction)
mod=a%2
print("Modulus:",mod)
rec=1/a
print("Reciprocal:",rec)
#1 d array addition
arr1=np.array([2,3,4,5])
arr2=np.array([6,7,8,9])
add_arr=arr1+arr2
print("Addition of 1d array:",add_arr)
mult_arr=arr1*arr2
print("Multiplication of 1d array:",mult_arr)

# function apply
var1=np.array([2,3,4,5])
var2=np.array([6,7,8,9],dtype=float)   #float me change kr diya taki reciprocal ka answer float me aaye
add_function=np.add(var1,var2)
print("Addition using function:",add_function)
mult_function=np.multiply(var1,var2)
print("Multiplication using function:",mult_function)
rec=np.reciprocal(var2)
print("Reciprocal using function:",rec)


# 2d array 
arr2d_1=np.array([[1,2,3,4],[5,6,7,8]])
arr2d_2=np.array([[5,6,7,8],[1,2,4,5]])
arr2d_1_add=np.add(arr2d_1,arr2d_2)
print("Addition of 2d array:",arr2d_1_add)
arr_sub=arr2d_1-arr2d_2
print("Subtraction of 2d array:",arr_sub)
