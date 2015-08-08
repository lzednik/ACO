__author__ = 'Lada'

from defsaco import Ant,Map,NbrSearch

M=Map('M1')

M.addNode(1)
M.addNode(2)
M.addNode(3)
M.addNode(4)

M.addArc({(1,2):1})
M.addArc({(2,3):1})
M.addArc({(2,3):2})
M.addArc({(4,4):1})


ant1=Ant('Lada')

ant1.addArc((1,2))
ant1.addArc((2,3))

#print(ant1.showItinerary())

print(NbrSearch(M,2))