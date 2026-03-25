# Level 1: Basic Statistics & Exploration
# Dataset ka shape aur dimensions check karein.

# Pehli 5 rows ko print karein taakay data ka structure samajh aa sakay.

# Har column ka mean (average) calculate karein.

# Har column ka median aur standard deviation nikalein.

# Pura array ka minimum aur maximum value dhoondein.
import numpy as np
data = np.genfromtxt('winequality-red.csv', delimiter=',', skip_header=1)

print(" Shape:", data.shape)
print(" Dimension:", data.ndim)

print("first 5 rows ",data[:5])

# hrr col ka mean(average)
print("mean ",np.mean(data,axis=0))

# median
print("median ",np.median(data,axis=0))
# standard deviation
print("standard deviation of each row ",np.std(data,axis=0))
# poore table ka std
print("std of full table ",np.std(data))
print("mean of full table ",np.mean(data))