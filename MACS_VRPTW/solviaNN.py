__author__ = 'Lada'

import numpy as np
import math


class Truck:
    def __init__(self,id):
        self.id=id
        self.pos=0
        self.tour=[]
        self.time=0
        self.load=0

data=np.loadtxt('solomon_r101.txt', skiprows=1)

#create distance matrix
dist=np.zeros((data.shape[0],data.shape[0]),dtype=np.int8)
for i in xrange(data.shape[0]):
    for j in xrange(data.shape[0]):
        dist[i][j]=math.ceil(float(np.linalg.norm(data[i][1:3]-data[j][1:3])))


#create nearest neighbor list
nn=[]
for i in xrange(dist.shape[0]):
    nnarg=np.argsort(dist[i]).tolist()
    del nnarg[0]
    nn.append(nnarg)


visitedList=[]
visitedList.append(0)
truckCount=0
truckList=[]
while len(visitedList) < data.shape[0]:
    truckList.append(Truck(truckCount))

    nxtFound=False
    nxt=0
    while nxtFound==False and nxt<len(nn[truckList[truckCount].pos]):
        candpos=nn[truckList[truckCount].pos][nxt]
        if ((truckList[truckCount].load+data[candpos][3])<200):
            if dist[truckList[truckCount].pos][candpos]<(data[candpos][5]-truckList[truckCount].time) and candpos not in visitedList:
                truckList[truckCount].pos=candpos
                truckList[truckCount].tour.append(candpos)
                visitedList.append(candpos)
                truckList[truckCount].time+=(dist[truckList[truckCount].pos][candpos]+data[candpos][6])
                truckList[truckCount].load+=data[candpos][3]

                nxtFound=True

            nxt+=1
        else:
            truckList[truckCount].pos=0
            truckList[truckCount].tour.append(0)
            truckList[truckCount].time+=(dist[truckList[truckCount].pos][0])
            truckList[truckCount].load=0


    if nxtFound==False:
        truckCount+=1
        print 'truck count: ' +str(truckCount-1)
        print 'truck load: ' +str(truckList[truckCount-1].load)
        print 'truck itinerary: ' +str(truckList[truckCount-1].tour)


print visitedList