__author__ = 'Lada'
import numpy as np

#data=np.loadtxt('solomon_r101.txt', skiprows=1)

# print data[0]
# print data[0][0]
# print data[0][1]
# print data[0][2]
# print data[0][3]
# print data[0][4]
# print data[0][5]
# print data[0][6]

a = np.array((3 ,0))
b = np.array((0, 4))

#computing euclidian distance
dist = np.linalg.norm(a-b)
print dist
