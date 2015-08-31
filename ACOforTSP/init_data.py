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

def pheromone(size,itlen):
    phi=1/math.log(itlen)
    ph = [[phi for i in xrange(size)] for i in xrange(size)]
    return ph

def choiceinfo(dist,pheromones,alpha,beta):
    size=len(dist)
    ch = [[0.0 for i in xrange(size)] for i in xrange(size)]
    for i in xrange(size):
        for j in xrange(size):
            if i!=j:
                ch[i][j]=alpha*math.log(pheromones[i][i])+beta*(math.log(dist[i][j]))
    return ch

def tourLenNN(nnList):
    dist=0
    tabu=[]
    cLoc=nnList[0][0]
    tabu.append(cLoc)
    while len(tabu)<50:
        nextFound=False
        for loc in nnList[cLoc][1]:
            if loc[0] not in tabu and nextFound==False:
                tabu.append(loc[0])
                dist+=loc[1]
                cLoc=loc[0]
                nextFound=True

    print 'NN-Search estimates initial tour length at '+ str(dist) + ' miles'
    return dist
