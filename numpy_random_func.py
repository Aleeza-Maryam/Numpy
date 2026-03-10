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


# ranf()
ranf=np.random.ranf(4)  # random float  1d array with 4 random values between 0.0(include) and 1.0(exclude)
print(ranf)
ranf_2d=np.random.ranf((2,3))
print(ranf_2d)

# randint()     ye 2 numbers k beech random value generate krta
randint=np.random.randint(1,10,5 )  #1 to 10 ke beech 5 random integers generate krta hai
print(randint)
randint_2d=np.random.randint(1,20,(2,3))
print(randint_2d)
