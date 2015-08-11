__author__ = 'Lada'
import random

class Colony:
    def __init__(self,id,):
        self.id=id
        self.ants=[]

    def addAnt(self,id,pos):
        self.ants.append(Ant(id,pos))

class Ant:
    def __init__(self,id,pos):
        self.id=id
        self.pos=pos
        self.finished=False
        self.itinerary =[]
        self.prec=0
        self.gotime=0

    def addArc(self,M,arc,time):
        self.itinerary.append(arc)
        self.pos=M.Arcs[arc]['spec'][1]
        self.gotime=time+M.Arcs[arc]['l']

    def reset(self,pos):
        self.pos=pos
        self.finished=False
        self.itinerary =[]
        self.prec=0
        self.gotime=0


    # def totalTime(self,M):
    #     ttime=0
    #     for arc in self.itinerary:
    #         ttime+=M.Arcs[arc]['spec']['l']
    #     return ttime

    # def showItinerary(self):
    #     itnr=''
    #     for arc in self.itinerary:
    #         itnr+=str(arc)+' '
    #     return itnr


class Map:
    Arcs={}

    def __init__(self,name):
        self.name=name

    def addArc(self,arc):
        self.Arcs.update(arc)

    def updateT(self,itinerary):
        for arc in itinerary:
            self.Arcs[arc]['t']+=1

    def evaporate(self,p):
        for arc in self.Arcs:
            self.Arcs[arc]['t']=((1-p)*self.Arcs[arc]['t'])


def NbrSearch(map,node,pred):
    arcList=[]
    for arc in map.Arcs.keys():
        if map.Arcs[arc]['spec'][0]==node and map.Arcs[arc]['spec'][1]!=pred:
            arcList.append(arc)
    return(arcList)

def ArcSelectProb(M,N):
    tsum=0
    for arc in N:
        tsum+=M.Arcs[arc]['t']

    plist=[]
    for arc in N:
        plist+=int(100*M.Arcs[arc]['t']/float(tsum))*[arc]
    return random.choice(plist)