__author__ = 'Lada'

from defsaco import Colony,Map,NbrSearch,ArcSelectProb,remCycles

alpha=1

M=Map('M1')

M.addArc({'arc1':{'spec':(1,2),'l':1,'t':1}})
M.addArc({'arc2':{'spec':(2,3),'l':2,'t':1}})
M.addArc({'arc3':{'spec':(2,3),'l':1,'t':1}})
M.addArc({'arc4':{'spec':(2,3),'l':5,'t':1}})
M.addArc({'arc5':{'spec':(3,4),'l':1,'t':1}})
M.addArc({'arc6':{'spec':(3,4),'l':2,'t':1}})



time=0
antFinishTotal=2000
antFinishCount=0

Colony=Colony('Colony1')

Colony.addAnt('Lada',1)
Colony.addAnt('Amber',1)
Colony.addAnt('Lucy',1)
Colony.addAnt('Baby Sam',1)
Colony.addAnt('Natalie',1)
Colony.addAnt('Zoey',1)

while antFinishCount<antFinishTotal:
    for ant in Colony.ants:
        if ant.gotime==time:
            if ant.pos != 4:
                N=NbrSearch(M,ant.pos,ant.prec)
                newArc=ArcSelectProb(M,N)
                ant.addArc(M,newArc,time)
            else:
                antFinishCount+=1
                ant.itinerary=remCycles(ant.itinerary,M)
                print ant.itinerary
                M.updateT(ant.itinerary)
                #M.evaporate(0.05)
                ant.reset(1,time)
        #print ant.id + '  ' +str(ant.itinerary)
        #print M.Arcs

    M.evaporate(0.05)
    time+=1
    print 'time '+str(time)

for arc in M.Arcs:
    print arc +': ' + str(round(M.Arcs[arc]['t'],2))

