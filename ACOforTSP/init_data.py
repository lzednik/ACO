__author__ = 'Lada'

from geopy.distance import vincenty
import pickle,math
from decimal import Decimal, getcontext
from geopy.geocoders import Nominatim



# #geocode
def geocode(fileNameSource,fileNameTarget):
    locs = [line.strip() for line in open(fileNameSource, 'r')]
    geolocator = Nominatim()
    geoLocs=[]

    for loc in locs:
        print 'Geocoding ' + str(loc)
        gloc = geolocator.geocode(loc)
        #geoLocs[loc]=(gloc.latitude,gloc.longitude)
        geoLocs.append({'city':loc,
                        'lat':gloc.latitude,
                        'lon':gloc.longitude})

    with open(fileNameTarget, 'wb') as handle:
        pickle.dump(geoLocs, handle)



#read instance
def readInstance(fileName):
    with open(fileName, 'rb') as handle:
        locs = pickle.loads(handle.read())
    return locs


def calculateDistances(cities):
    dist = [[int(vincenty((cities[i]['lat'],cities[i]['lon']),(cities[j]['lat'],cities[j]['lon'])).miles) for i in xrange(len(cities))] for j in xrange(len(cities))]

    #print vincenty((cities[i]['lat'],cities[i]['lon']),(cities[j]['lat'],cities[j]['lon'])).miles

    return dist

def computeNNlists(dist):
    nnList=[]
    for i in xrange(len(dist)):
        listToSort=[]
        for j in xrange(len(dist)):
            if i != j:
                listToSort.append((j,dist[i][j]))
        listToSort.sort(key=lambda x: x[1])
        nnList.append((i,listToSort))
    return nnList

def pheromone(size,phi):
    #phi=1/math.log(itlen)
    ph = [[phi for i in xrange(size)] for i in xrange(size)]
    return ph

def choiceinfo(dist,pheromones,alpha,beta):
    size=len(dist)
    ch = [[0.0 for i in xrange(size)] for i in xrange(size)]
    for i in xrange(size):
        for j in xrange(size):
            if i!=j:
                #ch[i][j]=alpha*pheromones[i][i]+beta*math.log(dist[i][j])
                ch[i][j]=alpha*pheromones[i][i]+beta*(1/math.log(dist[i][j],10))

    #compute actual probabilities
    # for i in  xrange(size):
    #     s=sum(ch[i])
    #     for j in  xrange(size):
    #         ch[i][j]=ch[i][j]/s
    return ch

def tourLenNN(nnList):
    dist=0
    visited=[]
    cLoc=nnList[0][0]
    visited.append(cLoc)
    while len(visited)<50:
        nextFound=False
        for loc in nnList[cLoc][1]:
            if loc[0] not in visited and nextFound==False:
                visited.append(loc[0])
                dist+=loc[1]
                cLoc=loc[0]
                nextFound=True

    print 'NN-Search estimates initial tour length at '+ str(dist) + ' miles'
    return dist

class Ant:
    def __init__(self,id):
        self.id=id
        self.pos=0
        self.tour_length=0
        self.tour=[]
        self.visited={}

def initAnts(antCount):
    Colony=[]
    for i in xrange(antCount):
        Colony.append(Ant(i))
    return Colony

def resetAnts(Colony):
    for ant in Colony:
        ant.id=0
        ant.pos=0
        ant.tour_length=0
        ant.tour=[]
        ant.visited={}

class antStats:
    def __init__(self):
        self.bestsofar={'tourLength':1000000}
        self.topFive=[]

    def bestsofar(self):
        return self.bestsofar

    def topFive(self):
        return self.topFive


