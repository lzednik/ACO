__author__ = 'Lada'

#from init_data import readInstance,calculateDistances,geocode,computeNNlists,pheromone,choiceinfo,tourLenNN
from init_data import *
from construct_solutions import *
from stats import *
#geocode
#geocode('cities.txt','cities_geocoded.txt')
alpha=1
beta=2

cities=readInstance('cities_geocoded.txt')
dist=calculateDistances(cities)
nnList=computeNNlists(dist)


itlen=tourLenNN(nnList)
phi=1/math.log(itlen)

pheromones=pheromone(len(cities),phi)
choiceInfo=choiceinfo(dist,pheromones,alpha,beta)

Colony=initAnts(10)
runStats=antStats()

run=0
while run <100:
    constructSolutions(Colony,nnList,choiceInfo,dist)
    runStats=updateStats(Colony,runStats)
    print runStats.bestsofar
    pheromones=evaporate(pheromones,0.1)
    pheromones=updatePheromones(pheromones,runStats,phi)
    choiceInfo=choiceinfo(dist,pheromones,alpha,beta)
    resetAnts(Colony)
    run+=1

#stats=updateStats(Colony,stats)
