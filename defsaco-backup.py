__author__ = 'Lada'
import random

class Colony:
    roster={}
    def __init__(self,id):
        self.id=id

class Ant:
    itinerary =[]
    prec=0
    def __init__(self,id,pos):
        self.id=id
        self.pos=pos
        self.finished=False

    def addArc(self,M,arc):
        self.itinerary.append(arc)
        self.pos=M.Arcs[arc]['spec'][1]

    def showItinerary(self):
        itnr=''
        for arc in self.itinerary:
            itnr+=str(arc)+' '
        return itnr


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