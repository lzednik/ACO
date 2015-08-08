__author__ = 'Lada'

class Ant:
    itinerary =[]
    def __init__(self,id):
        self.id=id
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



def NbrSearch(map,Node):
    arcList=[]
    for arc in map.Arcs:
        if arc.keys()[0][0]==Node:
            arcList.append(arc)
    return(arcList)