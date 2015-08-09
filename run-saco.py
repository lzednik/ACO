__author__ = 'Lada'

from defsaco import Ant,Map,NbrSearch,ArcSelectProb

alpha=1

M=Map('M1')

M.addArc({'arc1':{'spec':(1,2),'l':1,'t':1}})
M.addArc({'arc2':{'spec':(2,3),'l':2,'t':1}})
M.addArc({'arc3':{'spec':(2,3),'l':1,'t':1}})
M.addArc({'arc4':{'spec':(3,4),'l':1,'t':1}})


time=0
antCount=2
antFinishCount=0
Colony=[Ant('Lada',1),
        Ant('Amber',1)]
print Colony

while antFinishCount<antCount:
    for ant in Colony:
        if ant.finished != True:
            if ant.pos != 4:
                N=NbrSearch(M,ant.pos,ant.prec)
                ant.addArc(M,ArcSelectProb(M,N))
            else:
                ant.finished=True
                antFinishCount+=1
                M.updateT(ant.itinerary)
                M.evaporate(0.05)
                #print M.Arcs
                print ant.itinerary
    time+=1
    print time
#print(ant1.showItinerary())
#print M.Arcs['arc1']
#print(NbrSearch(M,3,2))
#print M.Arcs