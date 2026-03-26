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


# Level 4: Advanced Analysis
# "Quality" aur "Alcohol" ke darmiyan correlation coefficient nikalein.

# Alcohol ki values ko categorize karein (e.g., >11 ko 1 aur <11 ko 0 assign karein).

# Pura array ka percentile (25th, 50th, 75th) calculate karein.

# Column-wise Sum nikal kar check karein ke kaunsa feature sabse bada weight rakhta hai.

# Dataset ko do hisson mein split karein (80% training aur 20% testing) NumPy indexing ke zariye.

corr_matrix = np.corrcoef(data[:, 10], data[:, 11])

# Hum [0, 1] position se asal value nikaalte hain
# Humein poora table nahi chahiye, sirf woh ek number chahiye jo dono ka talluq bataye.

# 0 ka matlab hai Pehli Row

# 1 ka matlab hai Doosra Column
correlation = corr_matrix[0, 1]
print(f"Alcohol aur Quality ka Correlation: {correlation:.4f}")
# Alcohol ki values ko categorize karein (e.g., >11 ko 1 aur <11 ko 0 assign karein).
alcohol = data[:, 10]

# 11 se zyada ko 1 (Strong) aur kam ko 0 (Light) assign karein
# np.where(condition, value_if_true, value_if_false)
alcohol_category = np.where(alcohol > 11, 1, 0)

print("Pehli 10 Alcohol Categories:", alcohol_category[:10])
print("Strong wines (1) ka total count:", np.sum(alcohol_category))

# Pura array ka percentile (25th, 50th, 75th) calculate karein.
# Percentiles batate hain ke aapka data kahan khara hai. Maslan, 50th percentile (Median) batata hai ke aadhi wines ki values is se kam hain.
p25, p50, p75 = np.percentile(data, [25, 50, 75])

print(f"25th Percentile: {p25}")
print(f"50th Percentile (Median): {p50}")
print(f"75th Percentile: {p75}")

# Column-wise Sum nikal kar check karein ke kaunsa feature sabse bada weight rakhta hai.
# axis=0 matlab column-wise sum
col_sums = np.sum(data, axis=0)

print("Har column ka total sum:\n", col_sums)