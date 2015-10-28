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

distInv=np.where(distM != 0, 1/distM, 0)
#distInv=np.divide(1,distM)

IN=np.zeros(dataM.shape[0])

nnSolution=nnAlgorithm(dataM,distM)
bestSolution=nnSolution
print('Results of NN Algorithm')
bestSolution.print()

beta=2
pheromones=pheromone(distM.shape,nnSolution.tour_length)


#choiceInfo=choiceInfo(pheromones,distInv,beta)



ant=Ant(1,bestSolution)

visited=[]
time=0
#print(dataM[:,0])
#print(Exploration(0,distM,dataM,choiceInfo,IN,visited,time))
Exploration(1,distM,dataM,pheromones,IN,visited,time,beta)
#
# prog=0
# while prog<10:
#     ant.calculate(distM,dataM,pheromones,bestSolution)
#     prog+=1
#
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