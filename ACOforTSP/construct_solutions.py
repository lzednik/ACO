__author__ = 'Lada'
import random

def constructSolutions(Colony,nnList):
    size=len(nnList)
    for ant in Colony:
        for i in xrange(size):
            ant.visited[i]=False
        ant.tour=[]
        ant.pos=random.randint(0,size-1)
        ant.tour.append(ant.pos)
    step=1
    while step < size:
        step+=1
        #for k in xrange(size):


#this needs to be redone so that the probabilities are not part of the choice info
#the reason for this is that the probability of selecting a city that is already in list
#must be zero
def ASDecisionRule(ant,nnList,choiceInfo):
    selection_probs=[]
    for city in nnList[ant.pos][1]:
        if city[0] not in ant.tour:
            selection_probs+=(int(100000*choiceInfo[ant.pos][city[0]]))*[city[0]]
    return random.choice(selection_probs)

