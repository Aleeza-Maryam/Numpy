import numpy as np
var1=np.array([1,2,3,4])
var2=np.array([6,7,8,9])
res1=np.concatenate((var1,var2))
print(res1)

# 2d array
var1_2d=np.array([
    [1,2,3,4],
    [5,6,7,8]
])
var2_2d=np.array([
    [9,8,7,6],
    [5,4,3,2]
])

res2=np.concatenate((var1_2d,var2_2d))
print(res2)

# axis parameter
ar_new=np.concatenate((var1_2d,var2_2d),axis=1)   #axis 1row
print(ar_new)
ar_new1=np.concatenate((var1_2d,var2_2d),axis=0)   #axis 0 column
print(ar_new1)

# stack k through merge
var3=np.array([1,2,3,4])
var4=np.array([5,6,7,8])
res3=np.stack((var3,var4))
print(res3)
res4=np.stack((var3,var4),axis=1)
print(res4)



# 1. np.concatenate() (Jodna)
# Ye tab use hota hai jab aapko arrays ko unki existing dimension mein hi aage badhana ho. Agar aap do 1D arrays ko concatenate karenge, toh result bhi ek 1D array hi milega.

# Logic: Ye arrays ko "end-to-end" chipka deta hai.

# Result: Dimension wahi rehti hai (1D + 1D = 1D).

# 2. np.stack() (Teh Lagana)
# Ye tab use hota hai jab aapko arrays ko ek ke upar ek rakh kar nayi dimension banani ho. Agar aap do 1D arrays ko stack karenge, toh result ek 2D array ban jayega (jaise aapne apne code mein dekha).

# Logic: Ye arrays ko "ek ke upar ek" ya "side-by-side" rakh kar ek naya block banata hai.

# Result: Dimension badh jati hai (1D + 1D = 2D).

# stack parameters
print("stack simple ",np.stack((var1,var2)))
print("stack with horizontal ",np.hstack((var1,var2)))
print("stack with vertical ",np.vstack((var1,var2)))
print("stack with height ",np.dstack((var1,var2)))
