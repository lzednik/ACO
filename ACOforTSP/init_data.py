__author__ = 'Lada'


from geopy.distance import vincenty
import pickle
import itertools


# from geopy.geocoders import Nominatim
# import pickle

#
# #geocode
# locs = [line.strip() for line in open("cities.txt", 'r')]
# geolocator = Nominatim()
# geoLocs={}
#
# for loc in locs:
#     gloc = geolocator.geocode(loc)
#     geoLocs[loc]=(gloc.latitude,gloc.longitude)
#
# with open('cities_geocoded.txt', 'wb') as handle:
#     pickle.dump(geoLocs, handle)



#read instance
def readInstance(fileName):
    with open(fileName, 'rb') as handle:
        locs = pickle.loads(handle.read())
    return locs


def calculateDistances(cities):
    dist={}
    combs=itertools.combinations(cities, 2)

    for comb in combs:
        d=round(vincenty(cities[comb[0]], cities[comb[1]]).miles,2)
        #print str(comb)+' '+ str(d)
        dist[comb]=d
    return dist
