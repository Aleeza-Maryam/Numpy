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




# Level 2: Slicing & Filtering
# Sirf "Quality" wala column (akhri column) extract karein.

# Un tamam wines ka data alag karein jinki quality 7 ya usse zyada hai.

# Column number 3 (Citric Acid) ki values ko extract kar ke ek naya array banayein.

# "Fixed Acidity" (1st column) ki 10th se 20th row tak ka data dikhayein.

# Woh rows filter karein jahan "Alcohol" ki percentage 10 se kam ho.


quality_col=data[:,-1]
print(quality_col)
greater_7=quality_col>7
var=data[greater_7]
print("Alcohol quality greate or equal 7 ",var)
print("count ",len(var))

citric=data[:,2]
print("citric acid col ",citric)


# "Fixed Acidity" (1st column) ki 10th se 20th row tak ka data dikhayein.
fixed_Acidity=data[10:21,0]
print("fixed acidity rw 10 se 20 ",fixed_Acidity)


# Woh rows filter karein jahan "Alcohol" ki percentage 10 se kam ho.
alcohol=data[:,-2]
alcohol_filter=data[alcohol<10]
print("percentage less than 10",alcohol_filter)
print("count ",len(alcohol_filter))