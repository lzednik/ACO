__author__ = 'Lada'


def remCycles(iti,M):
    pos=0
    posmax=len(iti)-1

    toRemovePos=[]
    while pos<posmax:
        c= M.Arcs[iti[pos]]['spec'][0]
        pos2=pos+1
        foundLoop=False
        while pos2<posmax and foundLoop==False:
            if c== M.Arcs[iti[pos2]]['spec'][1]:
                print 'loop found at pos ' +str(pos)+ ' ' +str(pos2)
                for x in range (pos,pos2+1):
                    toRemovePos.append(x)
                foundLoop=True
                pos=pos2+1
            else:
                pos2+=1
        pos+=1

    #delete loops
    toRemovePos.sort(reverse=True)
    for x in toRemovePos:
        del iti[x]
    return iti