__author__ = 'Lada'
import random

class Ant:
    def __init__(self,id,vcount):
        self.id=id
        self.tour_length=0
        self.visited=[]
        self.veh_count=vcount
        self.vehicles=[]
        for v in xrange(vcount):
            self.vehicles.append(Vehicle(v))

    def calculate(self,distM):
        for veh in self.vehicles:
            nextNode=pickNext(veh.pos,distM)


class Vehicle:
    def __init__(self,id):
        self.id=id
        self.pos=0
        self.tour=[]


def initAnts(antCount):
    Colony=[]
    for i in xrange(antCount):
        Colony.append(Ant(i))
    return Colony



def pickNext(pos,distM):

    nn=distM[0]
    posPicks=[]
    for n in xrange(nn.shape[0]):
        if nn[n] !=0:
            posPicks+=(int(100/nn[n])*[n])
    return random.choice(posPicks)