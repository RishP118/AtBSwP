
import os, re
from pathlib import Path
s=open('libs.txt','w')
s.write('The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was \n unaffected by these events.')
s.close()

s=open('libs.txt','r')
a=s.read()
s.close()
regex=re.compile(r'ADJECTIVE|NOUN|ADVERB|VERB')
t=regex.findall(data)
for i in t:
    if i=="ADJECTIVE" or i=="ADVERB":
        x=input(f"Enter the {i}: \n")
        f=a.replace(i,x,1)
        a=f
    else:
        x=input(f"Enter the {i}: \n")
        f=a.replace(i,x,1)
        a=f
print(a)
b=open('final.txt','w')
c=b.write(a)
b.close()
