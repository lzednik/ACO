import numpy as np

dataM=np.loadtxt('solomon_r101.txt', skiprows=1)
dueTimes=dataM[:,5]

a=np.argsort(dueTimes)
print(dueTimes)
print('*************')
print(a)

