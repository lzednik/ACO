import random

#Prob of explore
p=0.8

ar=[]
ar.append(int(10*round(p,2))*['Explore'])
ar.append(int(10*(round(1-p,2)))*['Exploit'])
ar2 = [y for x in ar for y in x]
r=random.choice(ar2)

print(r)


