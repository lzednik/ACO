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

def evaporate(pheromones,p):
    size=len(pheromones)
    for x in xrange(size):
        for y in xrange(size):
            pheromones[x][y]=pheromones[x][y]*(1-p)
    return pheromones

def updatePheromones(pheromones,stats,phi):
    for x in xrange(len(stats.bestsofar['tour'])-1):
        #print str(stats.bestsofar['tour'][x]) + ' ' +str(stats.bestsofar['tour'][x+1])
        #pheromones[stats.bestsofar['tour'][x]][stats.bestsofar['tour'][x+1]]+=phi
        #pheromones[stats.bestsofar['tour'][x+1]][stats.bestsofar['tour'][x]]+=phi

        pheromones[stats.bestsofar['tour'][x]][stats.bestsofar['tour'][x+1]]*=1.05
        pheromones[stats.bestsofar['tour'][x+1]][stats.bestsofar['tour'][x]]*=1.05

    for tour in stats.topFive:
        for x in xrange(len(tour)-1):
            pheromones[tour[x]][tour[x+1]]*=1.04

    return pheromones