__author__ = 'Lada'
import random

#class Ant defines Ant object
class Ant:
    def __init__(self,id,vcount,bestSolution):
        self.id=id
        self.tour_length=0
        self.visited=[]
        self.veh_count=vcount
        self.vehicles=[]
        self.time=0

        for v in range(vcount):
            self.vehicles.append(Vehicle(v))

        for veh in self.vehicles:
            veh.pos=0

    #each Ant needs to be able to calculate routes for each vehicle
    def calculate(self,distM,dataM,pheromones,bestSolution):
        #reset
        for veh in self.vehicles:
            veh.pos=0
            veh.tour=[]
            veh.doneTime=0
        self.tour_length=0
        self.time=0
        self.visited=[]

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
        #need to figure out if update should take place
        if get_customers_visited_count(self.vehicles)>bestSolution.customers_visited:
            bestSolution.customers_visited=get_customers_visited_count(self.vehicles)
            bestSolution.tour=[]
            for veh in self.vehicles:
                bestSolution.tour.append(veh.tour)

            update_pheromone(self.vehicles,pheromones)
            print('updated pheromones')


    #Ants need to print routes for each vehicle
    def print_routes(self,bestSolution):
        print('The best routes so far are:')
        for tour in bestSolution.tour:
            print('Route '+ str(tour))
            print('')

    def print_tourlength(self,dist):
        tour_length=get_tourlength(self,dist)
        print(tour_length)

class Vehicle:
    def __init__(self,id):
        self.id=id
        self.pos=0
        self.tour=[]
        self.doneTime=0

class Solution:
    def __init__(self):
        self.vehicle_count=0
        self.customers_visited=0
        self.tour_length=0
        self.tour=[]

    def print(self):
        print('Results of NN Algorithm:')
        print('')
        print('Number of Vehicles: ' +str(self.vehicle_count))
        print('Number of Visited Customers: ' +str(self.customers_visited))
        print('Total Distance Traveled: ' +str(self.tour_length))
        print('')
        print ('Vehicle''s Tours: ')
        for i in range(self.vehicle_count):
            print('Vehicle '+ str(i+1) + ': '+str(self.tour[i]))

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

            posPicks+=(int(10000000/nn[n]*pheromones[pos][n])*[n])
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

def get_tourlength(vehicles,dist):
    tour_length=0
    for veh in vehicles:
        for i in range(len(veh.tour)-1):
            tour_length+=dist[veh.tour[i]][veh.tour[i+1]]
    return(tour_length)

def get_customers_visited_count(vehicles):
    cs=0
    for veh in vehicles:
        cs+=len(veh.tour)
    return cs