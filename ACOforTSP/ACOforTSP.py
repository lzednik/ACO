__author__ = 'Lada'

#from init_data import readInstance,calculateDistances,geocode,computeNNlists,pheromone,choiceinfo,tourLenNN
from init_data import *
from construct_solutions import *

#geocode
#geocode('cities.txt','cities_geocoded.txt')
alpha=1
beta=2

cities=readInstance('cities_geocoded.txt')
dist=calculateDistances(cities)
nnList=computeNNlists(dist)


itlen=tourLenNN(nnList)
pheromones=pheromone(len(cities),itlen)
choiceInfo=choiceinfo(dist,pheromones,alpha,beta)

Colony=initAnts(10)

constructSolutions(Colony,nnList,choiceInfo,dist)

#print Colony[2].visited[1]
#print Colony[2].tour

# nc=ASDecisionRule(Colony[0],nnList,choiceInfo)
# print nc
print Colony[0].tour_length
print Colony[1].tour_length
print Colony[2].tour_length
print Colony[3].tour_length
print Colony[4].tour_length
print Colony[4].tour


