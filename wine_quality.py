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


# Level 3: Data Manipulation & Logic
# Pura dataset check karein ke kahin koi NaN (Null) value toh nahi.

# "PH" column ki saari values ko update karein (e.g., har value mein 0.1 add karein).

# "Quality" column mein check karein ke kitni unique values hain.

# Ek naya column (array) banayein jo "Fixed Acidity" aur "Volatile Acidity" ka sum ho.

# Dataset ko "Alcohol" column ke mutabiq sort karein (ascending order).

nan=np.isnan(data).any()
print(nan)
nansum=sum(np.isnan(data))
print(nansum)


# "PH" column ki saari values ko update karein (e.g., har value mein 0.1 add karein).
phsum=data[:,-4]+0.1
print(phsum)

# "Quality" column mein check karein ke kitni unique values hain.
qual_unique=np.unique(data[:,-1])
print(qual_unique)

# Ek naya column (array) banayein jo "Fixed Acidity" aur "Volatile Acidity" ka sum ho.

sum_fix_vol=data[:,0]+data[:,1]
print(sum_fix_vol)

# np.column_stack do arrays ko side-by-side jor deta hai
# Humein sum_fix_vol ko 2D banana parega iske liye
new_dataset = np.column_stack((data, sum_fix_vol))

print("Naya dataset shape:", new_dataset.shape)

np.savetxt('new_wine_data.csv', new_dataset, delimiter=',')

print("new excel file saved.")


# Dataset ko "Alcohol" column ke mutabiq sort karein (ascending order).
alcohol_asc=data[:,-2]
sorted_array=np.sort(alcohol_asc)
print(sorted_array)

# poore datet ko alcohol k according sort
sort_indice=np.argsort(data[:,10])
sorted_dataset=data[sort_indice]
print("sorted cols ",sorted_dataset[:,:])

# 1. Pehle normal argsort karein (Ascending)
sort_indices = np.argsort(data[:, 10])

# 2. Is index array ko reverse kar dein [::-1] use karke
descending_indices = sort_indices[::-1]

# 3. Ab data ko in naye indexes ke mutabiq arrange karein
sorted_descending = data[descending_indices]

# Check karein: Pehli 5 rows ka alcohol (Index 10) - Ab ye sabse zyada honi chahiye
print("Sorted Alcohol (Highest to Lowest):\n", sorted_descending[:5, 10])
