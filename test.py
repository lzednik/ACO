__author__ = 'Lada'

from defsaco import Map

M=Map('M1')

M.addArc({'arc1':{'spec':(1,2),'l':1,'t':1}})
M.addArc({'arc2':{'spec':(2,3),'l':8,'t':1}})
M.addArc({'arc3':{'spec':(2,3),'l':2,'t':1}})
M.addArc({'arc4':{'spec':(3,4),'l':1,'t':1}})
M.addArc({'arc5':{'spec':(4,5),'l':1,'t':1}})
M.addArc({'arc6':{'spec':(5,2),'l':1,'t':1}})
M.addArc({'arc7':{'spec':(5,6),'l':1,'t':1}})
M.addArc({'arc8':{'spec':(6,4),'l':1,'t':1}})
M.addArc({'arc9':{'spec':(6,7),'l':1,'t':1}})
M.addArc({'arc10':{'spec':(7,8),'l':1,'t':1}})


iti=['arc1','arc2','arc4','arc5','arc6','arc3','arc4','arc5','arc7','arc9','arc10']


#print route
route=''
for arc in iti:
    route+= str(M.Arcs[arc]['spec'])+ '  '
print route

pos=0
posmax=len(iti)-1

newIti=[]
while pos<posmax:
    c= M.Arcs[iti[pos]]['spec'][0]
    pos2=pos+1
    foundLoop=False
    while pos2<posmax and foundLoop==False:
        if c== M.Arcs[iti[pos2]]['spec'][1]:
            print 'loop found at pos ' +str(pos)
            foundLoop=True
            break
        pos2+=1
    if foundLoop!=True:
        newIti.append(iti[pos])
        pos+=1
    else:
        newIti.append(iti[pos2+1])
        pos=pos2+1


#print route
route=''
for arc in newIti:
    route+= str(M.Arcs[arc]['spec'])+ '  '
print route