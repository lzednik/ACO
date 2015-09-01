__author__ = 'Lada'

#from init_data import readInstance,calculateDistances,geocode,computeNNlists,pheromone,choiceinfo,tourLenNN
from init_data import *
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
