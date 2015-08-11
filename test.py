__author__ = 'Lada'

from test2 import Colony,Ant

colony1=Colony('Colony1')

colony1.addAnt('Lada',1)
colony1.addAnt('Amber',2)
colony1.ants[0].addArc((1,2))
colony1.ants[1].addArc((3,4))
colony1.ants[0].addArc((2,3))

for ant in colony1.ants:
    if ant.id=='Lada':
        ant.id='Zoey'
    print ant.id + '   ' + str(ant.itinerary)





# ant1=Ant('Lada',5)
# print ant1.id
# ant1.addArc((1,2))
# ant1.addArc((2,3))
# print ant1.itinerary



#ant1=Ant('Lada',1)

#print colony1.roster.values()

# a=Ant('Amber',2)
# print a.id