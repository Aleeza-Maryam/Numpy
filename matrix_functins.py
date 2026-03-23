# TRANSPOSE
import numpy as np
var1=np.array([1,2,3,4,5])
print(np.transpose(var1))   #To see a transpose in action, the array needs to have at least two dimensions

var2=np.matrix([
    [1,2,3,4],
    [5,6,7,8]
])
print(np.transpose(var2))

var3=np.array([[
     [1,2,3,4],
    [5,6,7,8]
],[
 [1,2,3,4],
    [5,6,7,8]

]])
# Original position: [0, 0, 1] (Block 0, Row 0, Column 1) Transposed position: [1, 0, 0] (Block 1, Row 0, Column 0)
print(np.transpose(var3))
# shortcut
print("Shortcut",var3.T)


# swapaxaes    : rows ko col mai col ko row mai
print(np.swapaxes(var2,0,1))      #jo data Axis 0 (Rows) par hai usay utha kar Axis 1 (Columns) par rakh do, aur jo Axis 1 par hai usay Axis 0 par le aao."




# 3. Agar 3D Array ho to?
# 3D array mein hamare paas teen parameters ho sakte hain: 0, 1, aur 2.

# Axis 0: Depth (Layers/Blocks)

# Axis 1: Rows

# Axis 2: Columns

# Agar aap np.swapaxes(var3, 0, 2) likhenge, to ye Blocks aur Columns ki jagah aapas mein badal dega, lekin Rows (1) apni jagah barqarar rahengi.


import numpy as np

# Shape: (2, 3, 2)
# 2 -> Blocks (Layers)
# 3 -> Rows per block
# 2 -> Columns per row

var3d = np.array([
    [ # Block 1
        [1, 2], 
        [3, 4], 
        [5, 6]
    ],
    [ # Block 2
        [7, 8], 
        [9, 10], 
        [11, 12]
    ]
])

print("3D Array:\n", var3d)
print("Shape of Array:", var3d.shape)
# Sirf Axis 0 aur Axis 1 ko swap karein
result = np.swapaxes(var3d, 0, 1)   #apne NumPy ko kaha ke jo Blocks (Axis 0) hain unhein Rows (Axis 1) bana do, aur Rows ko Blocks bana do.
print(result)

# inverse
var33=np.matrix(
    [
        [1,2],
        [3,4]
    ]
 )
print(np.linalg.inv(var33))

# power
print(np.linalg.matrix_power(var33,0))