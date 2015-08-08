__author__ = 'Lada'

from defsaco import Ant,Map,NbrSearch,ArcSelectProb

alpha=1

M=Map('M1')

M.addNode(1)
M.addNode(2)
M.addNode(3)
M.addNode(4)

M.addArc({'arc1':{'spec':(1,2),'l':1,'t':1}})
M.addArc({'arc2':{'spec':(2,3),'l':2,'t':2}})
M.addArc({'arc3':{'spec':(2,3),'l':1,'t':1}})
M.addArc({'arc4':{'spec':(3,4),'l':1,'t':1}})


ant1=Ant('Lada',2)
N=NbrSearch(M,ant1.pos,ant1.prec)

ant1.addArc(ArcSelectProb(N))

print(ant1.showItinerary())
#print(NbrSearch(M,3,2))
#print M.Arcs