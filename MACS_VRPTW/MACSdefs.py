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
        for v in range(vcount):
            self.vehicles.append(Vehicle(v))

    #each Ant needs to be able to calculate routes for each vehicle
    def calculate(self,distM,dataM,pheromones):
        #initially each vehicle is assigned a node
        for veh in self.vehicles:
            nextNode=pickNext(veh.pos,distM,dataM,pheromones,self.visited,self.time)
            if nextNode!='nothingFound':
                self.visited.append(nextNode)
                veh.tour.append(nextNode)
                veh.doneTime=max(self.time+distM[veh.pos][nextNode]+dataM[nextNode][6],dataM[nextNode][4]+dataM[nextNode][6])
                veh.pos=nextNode

        #calculate the rest of the itinerary
        calcDone=False
        tabuL=[]
        while calcDone==False:
            minT=1000000
            vehID='unknown'
            for veh in self.vehicles: #the next vehicle will be the one that gets done first
                if veh.doneTime<minT and veh.id not in tabuL:
                    minT=veh.doneTime
                    vehID=veh.id
            if vehID !='unknown':
                self.time=self.vehicles[vehID].doneTime
                nextNode=pickNext(self.vehicles[vehID].pos,distM,dataM,pheromones,self.visited,self.time)

                if nextNode=='nothingFound':
                    if vehID not in tabuL:
                        tabuL.append(vehID)
                else:
                    nxtNodeFound=True
                    self.visited.append(nextNode)
                    self.vehicles[vehID].tour.append(nextNode)
                    self.vehicles[vehID].doneTime=max(self.time+distM[veh.pos][nextNode]+dataM[nextNode][6],dataM[nextNode][4]+dataM[nextNode][6])
                    self.vehicles[vehID].pos=nextNode

            else:
                calcDone=True
        return update_pheromone(self.vehicles,pheromones)


    #Ants need to print routes for each vehicle
    def print_routes(self):
        for veh in self.vehicles:
            print ('Vehicle ' + str(veh.id))
            print('Route '+ str(veh.tour))
            print('')

class Vehicle:
    def __init__(self,id):
        self.id=id
        self.pos=0
        self.tour=[]
        self.doneTime=0


#initialization of ants into a colony
def initAnts(antCount):
    Colony=[]
    for i in range(antCount):
        Colony.append(Ant(i))
    return Colony


#procedure to pick the next node
def pickNext(pos,distM,dataM,pheromones,visited,time):
    nn=distM[0]
    posPicks=[]
    foundOne=False
    for n in range(nn.shape[0]):
        if nn[n] !=0 and n not in visited and time+distM[pos][n]<=dataM[n][5]:
            foundOne=True
            #print(int(10000000/nn[n]*pheromones[pos][n]))
            posPicks+=(int(10000000/nn[n]*pheromones[pos][n])*[n])
        if foundOne==True:
            retVal=random.choice(posPicks)
        else:
            retVal='nothingFound'
    return retVal


def pheromone(size,nnlen):
    phi=1/(size*(nnlen))
    ph = [[phi for i in range(size)] for i in range(size)]
    return ph

def update_pheromone(vehicles,pheromones):
    for veh in vehicles:
        for i in range(len(veh.tour)-1):
            pheromones[veh.tour[i]][veh.tour[i+1]]*=1.1
            pheromones[veh.tour[i+1]][veh.tour[i]]*=1.1
    return pheromones