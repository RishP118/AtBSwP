import random
numberOfStreaks = 0
l=[]
s=[]
d=[]
for experimentNumber in range(10000):
    v=random.randint(0,1)
    if v==0:
        l.append('H')
    else:
        l.append('T')
c=1
for i in range(len(l)-1):
    if l[i]== l[i+1]:
        c+=1
    else:
        s.append(c)
        d.append(list[i])
        c=1
s.append(c)
d.append(l[i+1])

numberOfStreaks=s.count(6)
print('Chance of streak: %s%%' % (numberOfStreaks / 100))
