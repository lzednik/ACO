__author__ = 'Lada'
import random

def constructSolutions(Colony,nnList,choiceInfo,dist):
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
            newpos=ASDecisionRule(ant,nnList,choiceInfo)
            #print 'pos is ' +str(ant.pos)
            ant.tour.append(newpos)
            ant.tour_length+=dist[ant.pos][newpos]
            ant.pos=newpos

    #adding return back home
    for ant in Colony:
        ant.tour_length+=dist[ant.pos][ant.tour[0]]
        ant.tour.append(ant.tour[0])

def ASDecisionRule(ant,nnList,choiceInfo):
    s=sum(choiceInfo[ant.pos])

    selection_probs=[]
    for ch in choiceInfo[ant.pos]:
        selection_probs.append(ch/s)

    plist=[]
    for city in nnList[ant.pos][1]:
        if city[0] not in ant.tour:
            plist+=int(100000*selection_probs[city[0]])*[city[0]]
    return random.choice(plist)

