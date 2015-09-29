__author__ = 'Lada'

from MACSdefs import *
import numpy as np
import math

#ACS_VEI=initAnts(100)


data=np.loadtxt('solomon_r101.txt', skiprows=1)

#create distance matrix
distM=np.zeros((data.shape[0],data.shape[0]),dtype=np.int8)
for i in xrange(data.shape[0]):
    for j in xrange(data.shape[0]):
        distM[i][j]=math.ceil(float(np.linalg.norm(data[i][1:3]-data[j][1:3])))

print pickNext(1,distM)
ant=Ant(16,3)
ant.calculate(distM)

