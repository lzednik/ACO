__author__ = 'Lada'
import random
import numpy as np

#vehicle object
class Vehicle:
    def __init__(self,id):
        self.id=id
        self.pos=0
        self.tour=[]
        self.doneTime=0

#solution object
class Solution:
    def __init__(self):
        self.vehicle_count=0
        self.customers_visited=0
        self.tour_length=0
        self.tour=[]
        self.visited=[]

    def print(self):
        print('Solution Data:')
        print('')
        print('Number of Vehicles: ' +str(self.vehicle_count))
        print('Number of Visited Customers: ' +str(self.customers_visited))
        print('Total Distance Traveled: ' +str(self.tour_length))
        print('')
        print ('Vehicle''s Tours: ')
        for i in range(self.vehicle_count):
            print('Vehicle '+ str(i+1) + ': '+str(self.tour[i]))

#class Ant defines Ant object
class Ant:
    def __init__(self,id,nfbestSolution):
        self.id=id
        self.vehicles=[]
        self.time=0
        self.solution=nfbestSolution
        self.solution.vehicle_count-=1
        self.solution.tour_length=0
        self.solution.visited=[]
        self.solution.visited.append(0)
        for v in range(self.solution.vehicle_count):
            self.vehicles.append(Vehicle(v))


    #each Ant needs to be able to calculate routes for each vehicle
    def calculate(self,distM,dataM,pheromones,IN,beta):
        #reset
        for veh in self.vehicles:
            veh.pos=0
            veh.tour=[]
            veh.doneTime=0
        #sorted due time
        sortedDueTimeRefs=np.argsort(dataM[:,5])
        #perform calculation
        calcDone=False
        minTime=1000000
        tour_length=0
        while calcDone==False:
            for veh in self.vehicles:
                if veh.doneTime<=self.time:
                    if ExploreExploitDecision(0.9) =='Explore':  #pass probability of exploration
                        print('Exploration')
                        nextPos=Exploration(veh.pos,distM,dataM,pheromones,IN,self.solution.visited,self.time,beta)

                        #update vehicle
                        veh.doneTime=max(self.time+distM[veh.pos][nextPos]+dataM[nextPos][6],dataM[nextPos][6])
                        if minTime>veh.doneTime:
                            minTime=veh.doneTime
                        veh.pos=nextPos
                        veh.tour.append(nextPos)
                        self.solution.visited.append(nextPos)
                        self.solution.tour_length+=1
                        IN[nextPos]+=1
                    #else:
                    #    print('Exploitation')
            #print('orig tour len: ' +str(tour_length))
            #print('new tour len: ' +str(self.solution.tour_length))
            print('self solution visited is:' +str(self.solution.visited))
            if tour_length==self.solution.tour_length:
                calcDone=True
                #insert procedure
                print('****************')
                print('Insert Procedure')
                for loc in sortedDueTimeRefs:
                    print('for loc %s the due time is %s' % (loc,dataM[loc][5])) #due time
                print('****************')

            else:
                tour_length=self.solution.tour_length
        return self.solution
        # #initially each vehicle is assigned a node
        # for veh in self.vehicles:
        #     nextNode=pickNext(veh.pos,distM,dataM,pheromones,self.visited,self.time)
        #     if nextNode!='nothingFound':
        #         self.visited.append(nextNode)
        #         veh.tour.append(nextNode)
        #         veh.doneTime=max(self.time+distM[veh.pos][nextNode]+dataM[nextNode][6],dataM[nextNode][4]+dataM[nextNode][6])
        #         veh.pos=nextNode
        #
        # #calculate the rest of the itinerary
        # calcDone=False
        # tabuL=[]
        # while calcDone==False:
        #     minT=1000000
        #     vehID='unknown'
        #     for veh in self.vehicles: #the next vehicle will be the one that gets done first
        #         if veh.doneTime<minT and veh.id not in tabuL:
        #             minT=veh.doneTime
        #             vehID=veh.id
        #     if vehID !='unknown':
        #         self.time=self.vehicles[vehID].doneTime
        #         nextNode=pickNext(self.vehicles[vehID].pos,distM,dataM,pheromones,self.visited,self.time)
        #
        #         if nextNode=='nothingFound':
        #             if vehID not in tabuL:
        #                 tabuL.append(vehID)
        #         else:
        #             nxtNodeFound=True
        #             self.visited.append(nextNode)
        #             self.vehicles[vehID].tour.append(nextNode)
        #             self.vehicles[vehID].doneTime=max(self.time+distM[veh.pos][nextNode]+dataM[nextNode][6],dataM[nextNode][4]+dataM[nextNode][6])
        #             self.vehicles[vehID].pos=nextNode
        #
        #     else:
        #         calcDone=True
        # #need to figure out if update should take place
        # if get_customers_visited_count(self.vehicles)>bestSolution.customers_visited:
        #     bestSolution.customers_visited=get_customers_visited_count(self.vehicles)
        #     bestSolution.tour=[]
        #     for veh in self.vehicles:
        #         bestSolution.tour.append(veh.tour)
        #
        #     update_pheromone(self.vehicles,pheromones)
        #     print('updated pheromones')

    #
    # #Ants need to print routes for each vehicle
    # def print_routes(self,bestSolution):
    #     print('The best routes so far are:')
    #     for tour in bestSolution.tour:
    #         print('Route '+ str(tour))
    #         print('')
    #
    # def print_tourlength(self,dist):
    #     tour_length=get_tourlength(self,dist)
    #     print(tour_length)
    #
    #


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
    phi=1/(size[0]*(nnlen))
    ph=np.empty(size)
    ph.fill(phi)
    return ph

# def choiceInfo(pheromones,distInv,beta):
#     ch=[a*pow(b,beta) for a,b in zip(pheromones,distInv)]
#     return ch

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

def ExploreExploitDecision(p):
    ar=[]
    ar.append(int(10*round(p,2))*['Explore'])
    ar.append(int(10*(round(1-p,2)))*['Exploit'])
    ar2 = [y for x in ar for y in x]
    return(random.choice(ar2))

#procedure to pick the next node
def Exploration(pos,distM,dataM,pheromones,IN,visited,time,beta):
    delivery_time=np.maximum(distM[pos]+time,dataM[:,4])
    delta_time=delivery_time-time
    dist=np.multiply(delta_time,dataM[:,5]-time)
    distance=np.subtract(dist,IN)

    # print('xxxxxxxxxxx')
    # print(distance)
    # print('xxxxxxxxxxx')

    distance=np.maximum(np.ones(dataM.shape[0]),distance)


    eta=1/distance
    etaPow=np.power(eta,beta)
    tosum=np.multiply(pheromones[pos],etaPow)
    thesum=np.sum(tosum)
    probs=np.divide(tosum,thesum)

    probmin=1/np.min(probs)
    probs2=np.round(np.multiply(probs,probmin),0).astype(int)
    # print('selection probabilities:')
    # print(probs2)
    np.savetxt('t1.txt', probs2, delimiter=',')
    probs3=[]
    for pos in range(probs2.shape[0]):
        if pos not in visited:
            probs3+=(probs2[pos]*[pos])
    return random.choice(probs3)

