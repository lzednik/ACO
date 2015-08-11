__author__ = 'Lada'

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
        self.itinerary=[]
    def addArc(self,arc):
        self.itinerary.append(arc)
