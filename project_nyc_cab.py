import numpy as np

taxi=np.genfromtxt("E:\\Numpy\\nyc_taxis.csv",delimiter=",",skip_header=True)
print(taxi)

# mean speed of all cab rides
# there is no col of speed
speed=taxi[:,7]/(taxi[:,8]/3600)
mean_speed=speed.mean()
print(mean_speed)

# number of rides in feb
rides_feb=taxi[taxi[:,1]==2,1]
print(rides_feb.shape[0])

# no. of ides passenger give mre than 50 dollar
print(taxi[taxi[:, -3] > 50, 1].shape[0])