__author__ = 'Lada'

#from init_data import readInstance,calculateDistances,geocode,computeNNlists,pheromone,choiceinfo,tourLenNN
from init_data import *
from construct_solutions import *
from stats import *
#geocode
#geocode('cities.txt','cities_geocoded.txt')
alpha=1
beta=3

cities=readInstance('cities_geocoded.txt')
dist=calculateDistances(cities)
distnorm=calculateDistancesNorm(cities)
nnList=computeNNlists(distnorm)



nnListfoNN=computeNNlists(dist)
itlen=tourLenNN(nnListfoNN)

phi=1

pheromones=pheromone(len(cities),phi)
choiceInfo=choiceinfo(distnorm,pheromones,alpha,beta)

Colony=initAnts(100)
runStats=antStats()

run=0
while run <20:
    constructSolutions(Colony,nnList,choiceInfo,dist)
    runStats=updateStats(Colony,runStats)
    print runStats.bestsofar
    pheromones=evaporate(pheromones,0.1)
    pheromones=updatePheromones(pheromones,runStats,phi)
    choiceInfo=choiceinfo(distnorm,pheromones,alpha,beta)
    resetAnts(Colony)
    run+=1

#stats=updateStats(Colony,stats)
print ''
# for x in xrange(51):
#     print cities[runStats.bestsofar['tour'][x]]

print''

