import numpy as np

# rand()
rand=np.random.rand(4)   #1d array with 4 random values between 0 and 1
print(rand)
# 2d array
ar_rand_2d=np.random.rand(2,3)
print(ar_rand_2d)

# randn()  ..normal distribution may return positive or negative close to zero
randn=np.random.randn(4)
print(randn)
randn_2d=np.random.randn(2,3)
print(randn_2d)
