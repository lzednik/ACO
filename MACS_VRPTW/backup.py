__author__ = 'Lada'

from MACSdefs import *
from solviaNN import *
import numpy as np
import math

dataM=np.loadtxt('solomon_r101.txt', skiprows=1)

#create distance matrix
distM=np.zeros((dataM.shape[0],dataM.shape[0]),dtype=np.int8)
for i in range(dataM.shape[0]):
    for j in range(dataM.shape[0]):
        distM[i][j]=math.ceil(float(np.linalg.norm(dataM[i][1:3]-dataM[j][1:3])))


nnSolution=nnAlgorithm(dataM,distM)
bestSolution=nnSolution
bestSolution.print()

beta=2
pheromones=pheromone(dataM.shape[0],nnSolution.tour_length)

ant=Ant(1,10,bestSolution)

prog=0
while prog<10:
    ant.calculate(distM,dataM,pheromones,bestSolution)
    prog+=1

#def pickNext(pos,distM,dataM,pheromones,visited,time):



#
# print('final routes are')
# ant.print_routes(bestSolution)
#
# print(dataM[26])
# print(dataM[4])
#
#
# #
# # ant.print_tourlength(distM)
# #
# # #
# # # for ch in choiceInfo:
# # #     print(ch)
# # #
# # # for ph in pheromones:
# # #     for ph1 in ph:
# # #         if ph1 !=9.900990099009901e-06:
# # #             print(ph1)