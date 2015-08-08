__author__ = 'Lada'
import random

class Ant:
    itinerary =[]
    prec=0
    def __init__(self,id,pos):
        self.id=id
        self.pos=pos
    def addArc(self,arc):
        self.itinerary.append(arc)
    def showItinerary(self):
        itnr=''
        for arc in self.itinerary:
            itnr+=str(arc)+' '
        return itnr


class Map:
    Nodes=[]
    Arcs=[]

    def __init__(self,name):
        self.name=name

    def addNode(self,node):
        self.Nodes.append(node)

    def addArc(self,arc):
        self.Arcs.append(arc)



def NbrSearch(map,node,pred):
    arcList=[]
    for arc in map.Arcs:
        if arc.values()[0]['spec'][0]==node and arc.values()[0]['spec'][1]!=pred:
            arcList.append(arc)
    return(arcList)

def ArcSelectProb(N):
    tsum=0
    for arc in N:
        tsum+=arc.values()[0]['t']

    plist=[]
    for arc in N:
        plist+=int(100*arc.values()[0]['t']/float(tsum))*arc.keys()

    return random.choice(plist)