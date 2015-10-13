__author__ = 'Lada'

from MACSdefs import *
import numpy as np
import math

#ACS_VEI=initAnts(100)


dataM=np.loadtxt('solomon_r101.txt', skiprows=1)

#create distance matrix
distM=np.zeros((dataM.shape[0],dataM.shape[0]),dtype=np.int8)
for i in range(dataM.shape[0]):
    for j in range(dataM.shape[0]):
        distM[i][j]=math.ceil(float(np.linalg.norm(dataM[i][1:3]-dataM[j][1:3])))


nnlen=1000
alpha=1
beta=2
pheromones=pheromone(dataM.shape[0],nnlen)
#print pickNext(1,distM)
ant=Ant(1,10)

prog=0
while prog<100:
    pheromones=ant.calculate(distM,dataM,pheromones)
    prog+=1

print('final routes are')
ant.print_routes()

ant.print_tourlength(distM)

#
# for ch in choiceInfo:
#     print(ch)
#
# for ph in pheromones:
#     for ph1 in ph:
#         if ph1 !=9.900990099009901e-06:
#             print(ph1)