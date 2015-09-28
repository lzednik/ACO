__author__ = 'Lada'

class Ant:
    def __init__(self,id):
        self.id=id
        self.pos=0
        self.tour_length=0
        self.tour=[]
        self.visited={}

def initAnts(antCount):
    Colony=[]
    for i in xrange(antCount):
        Colony.append(Ant(i))
    return Colony