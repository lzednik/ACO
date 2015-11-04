__author__ = 'Lada'

from MACSdefs import *
from solviaNN import *
import numpy as np
import math
import time

start_time=time.time()

dataM=np.loadtxt('solomon_r101.txt', skiprows=1)

#create distance matrix
distM=np.zeros((dataM.shape[0],dataM.shape[0]),dtype=np.int8)
for i in range(dataM.shape[0]):
    for j in range(dataM.shape[0]):
            distM[i][j]=math.ceil(float(np.linalg.norm(dataM[i][1:3]-dataM[j][1:3])))

IN=np.zeros(dataM.shape[0])

nnSolution=nnAlgorithm(dataM,distM)
bestSolution=nnSolution
nfbestSolution=nnSolution

print('Results of NN Algorithm')
bestSolution.print()
print('End of results of NN Algorithm')
print('')

beta=2
pheromones=pheromone(distM.shape,nnSolution.tour_length)


#choiceInfo=choiceInfo(pheromones,distInv,beta)



ant=Ant(1,bestSolution)

#ant.calculate(distM,dataM,pheromones,bestSolution,IN,beta)

newSolution=ant.calculate(distM,dataM,pheromones,IN,beta)

if len(newSolution.visited)>5:
    print('woohoo')


print('')
print("Execution time was %s seconds." % round((time.time() - start_time),4))
print('')

#print(Exploration(1,distM,dataM,pheromones,IN,visited,time,beta))


#print(dataM[:,0])
#print(Exploration(0,distM,dataM,choiceInfo,IN,visited,time))
#Exploration(1,distM,dataM,pheromones,IN,visited,time,beta)


#print(distM[1])
#np.savetxt('t2.txt', distM[1], delimiter=',')



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