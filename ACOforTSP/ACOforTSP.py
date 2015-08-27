__author__ = 'Lada'

from init_data import readInstance,calculateDistances

cities=readInstance('cities_geocoded.txt')

distances=calculateDistances(cities)

for d in distances:
    print str(d)+' '+str(distances[d])
