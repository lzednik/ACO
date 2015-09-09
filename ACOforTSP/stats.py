__author__ = 'Lada'

def updateStats(Colony,stats):
    toursList=[]
    for ant in Colony:
        toursList.append((ant.id,ant.tour_length))
    toursList.sort(key=lambda x: x[1])
    print str(stats.bestsofar['tourLength']) + ' is more than ' + str(toursList[0][1])
    if stats.bestsofar['tourLength']>toursList[0][1]:
        stats.bestsofar['tourLength']=toursList[0][1]
        stats.bestsofar['tour']=Colony[toursList[0][0]].tour

    stats.topFive=[]
    for x in xrange(5):
        stats.topFive.append(Colony[toursList[x][0]].tour)
    return stats
