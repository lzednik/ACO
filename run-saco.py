__author__ = 'Lada'

from defsaco import Colony,Ant,Map,NbrSearch,ArcSelectProb

alpha=1

M=Map('M1')

M.addArc({'arc1':{'spec':(1,2),'l':1,'t':1}})
M.addArc({'arc2':{'spec':(2,3),'l':2,'t':1}})
M.addArc({'arc3':{'spec':(2,3),'l':1,'t':1}})
M.addArc({'arc4':{'spec':(3,4),'l':1,'t':1}})


time=0
antCount=6
antFinishCount=0

Colony=Colony('Colony1')

Colony.addAnt('Lada',1)
Colony.addAnt('Amber',1)
Colony.addAnt('Lucy',1)
Colony.addAnt('Baby Sam',1)
Colony.addAnt('Natalie',1)
Colony.addAnt('Zoey',1)


while antFinishCount<antCount:
    for ant in Colony.ants:
        #print 'before '+ ant.id +'  ' +str(ant.itinerary) + '  '+str(ant.pos)
        if ant.finished != True:
            if ant.pos != 4:
                N=NbrSearch(M,ant.pos,ant.prec)
                newArc=ArcSelectProb(M,N)
                #print newArc
                ant.addArc(M,newArc)
            else:
                ant.finished=True
                antFinishCount+=1
                M.updateT(ant.itinerary)
                M.evaporate(0.05)
                #print M.Arcs
        print 'after '+ ant.id +'  ' +str(ant.itinerary) + '  '+str(ant.pos)
    time+=1
    print 'time '+str(time)
#print(ant1.showItinerary())
#print M.Arcs['arc1']
#print(NbrSearch(M,3,2))
#print M.Arcs

