__author__ = 'Lada'

import numpy as np
from MACSdefs import Solution

class Truck:
    def __init__(self,id):
        self.id=id
        self.pos=0
        self.tour=[]
        self.time=0
        self.load=0
        self.tourlength=0

#data=np.loadtxt('solomon_r101.txt', skiprows=1)

def nnAlgorithm(data,dist):

    #create nearest neighbor list
    nn=[]
    for i in range(dist.shape[0]):
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
                    truckList[truckCount].tourlength+=(dist[truckList[truckCount].pos][candpos]+data[candpos][6])
                    nxtFound=True

                nxt+=1
            else:
                truckList[truckCount].pos=0
                truckList[truckCount].tour.append(0)
                truckList[truckCount].time+=(dist[truckList[truckCount].pos][0])
                truckList[truckCount].tourlength+=(dist[truckList[truckCount].pos][0])
                truckList[truckCount].load=0


        if nxtFound==False:
            truckCount+=1
            # print('truck count: ' +str(truckCount-1))
            # print('truck load: ' +str(truckList[truckCount-1].load))
            # print('truck itinerary: ' +str(truckList[truckCount-1].tour))
            # print('truck tour length: ' +str(truckList[truckCount-1].tourlength))
            # print('')

    nnsol=Solution()
    nnsol.tour
    for truck in truckList:
        nnsol.tour_length+=truck.tourlength
        nnsol.tour.append(truck.tour)
    nnsol.vehicle_count=truckCount
    nnsol.customers_visited=len(visitedList)-1

    return nnsol
#
# visitedList=[]
# visitedList.append(0)
# truckCount=0
# truckList=[]
# while len(visitedList) < data.shape[0]:
#     truckList.append(Truck(truckCount))
#
#     nxtFound=False
#     nxt=0
#     while nxtFound==False and nxt<len(nn[truckList[truckCount].pos]):
#         candpos=nn[truckList[truckCount].pos][nxt]
#         if ((truckList[truckCount].load+data[candpos][3])<200):
#             if dist[truckList[truckCount].pos][candpos]<(data[candpos][5]-truckList[truckCount].time) and candpos not in visitedList:
#                 truckList[truckCount].pos=candpos
#                 truckList[truckCount].tour.append(candpos)
#                 visitedList.append(candpos)
#                 truckList[truckCount].time+=(dist[truckList[truckCount].pos][candpos]+data[candpos][6])
#                 truckList[truckCount].load+=data[candpos][3]
#                 truckList[truckCount].tourlength+=(dist[truckList[truckCount].pos][candpos]+data[candpos][6])
#                 nxtFound=True
#
#             nxt+=1
#         else:
#             truckList[truckCount].pos=0
#             truckList[truckCount].tour.append(0)
#             truckList[truckCount].time+=(dist[truckList[truckCount].pos][0])
#             truckList[truckCount].tourlength+=(dist[truckList[truckCount].pos][0])
#             truckList[truckCount].load=0
#
#
#     if nxtFound==False:
#         truckCount+=1
#         print('truck count: ' +str(truckCount-1))
#         print('truck load: ' +str(truckList[truckCount-1].load))
#         print('truck itinerary: ' +str(truckList[truckCount-1].tour))
#         print('truck tour length: ' +str(truckList[truckCount-1].tourlength))
#         print('')
#
#
# print(visitedList)
#
# totaldist=0
# for truck in truckList:
#     totaldist+=truck.tourlength
#
#
# print('Total distance is: ' +str(totaldist))