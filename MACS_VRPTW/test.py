__author__ = 'Lada'
import random

#class Ant defines Ant object
class Ant:
    def __init__(self,id,vcount):
        self.id=id
        self.tour_length=0
        self.visited=[]
        self.veh_count=vcount
        self.vehicles=[]
        self.time=0
        for v in xrange(vcount):
            self.vehicles.append(Vehicle(v))
    
    #each Ant needs to be able to calculate routes for each vehicle 
    def calculate(self,distM,dataM):
        calcDone=False
        while calcDone==False:
            for veh in self.vehicles:
                minT=1000000
                vehID='unknown'
                for veh in self.vehicles:
                    if veh.doneTime<minT:
                        minT=veh.doneTime
                        vehID=veh.id

                nextNode=pickNext(veh.pos,distM,dataM,self.visited,self.time)
                if nextNode=='nothingFound':
                    calcDone=True
                else:
                    self.visited.append(nextNode)
                    veh.tour.append(nextNode)
                    veh.doneTime=max(self.time+distM[veh.pos][nextNode]+dataM[nextNode][6],dataM[nextNode][4]+dataM[nextNode][6])
                    veh.pos=nextNode

    #Ants need to print routes for each vehicle
    def print_routes(self):
        for veh in self.vehicles:
            print 'Vehicle ' + str(veh.id)
            print 'Route '+ str(veh.tour)
            print ''

class Vehicle:
    def __init__(self,id):
        self.id=id
        self.pos=0
        self.tour=[]
        self.doneTime=0


#initialization of ants into a colony
def initAnts(antCount):
    Colony=[]
    for i in xrange(antCount):
        Colony.append(Ant(i))
    return Colony


#procedure to pick the next node
def pickNext(pos,distM,dataM,visited,time):
    nn=distM[0]
    posPicks=[]
    foundOne=False
    for n in xrange(nn.shape[0]):
        if nn[n] !=0 and n not in visited and time+distM[pos][n]<=dataM[n][5]:
            foundOne=True
            posPicks+=(int(100/nn[n])*[n])
        if foundOne==True:
            retVal=random.choice(posPicks)
        else:
            retVal='nothingFound'
    return retVal