__author__ = 'Lada'
import random

def constructSolutions(Colony,nnList,choiceInfo):
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
        for ant in Colony:
            ant.pos=ASDecisionRule(ant,nnList,choiceInfo)
            ant.tour.append(ant.pos)




def ASDecisionRule(ant,nnList,choiceInfo):
    s=sum(choiceInfo[ant.pos])
    selection_probs=[]
    for ch in choiceInfo[ant.pos]:
       selection_probs.append(ch/s)
    # plist=[]
    for city in nnList[ant.pos][1]:
        if city[0] not in ant.tour:
            selection_probs+=int(100000*selection_probs[city[0]])*[city[0]]
    return random.choice(selection_probs)

