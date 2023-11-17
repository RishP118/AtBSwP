
import os, re

a = input("Enter: ")

for i in os.listdir():
	if i.endswith(".txt"):

            with open(i,'r') as f:
                data=f.read()
                exp=re.compile(a)
                find=exp.findall(data)

                for j in find:
                    item=j
                if item in data:
                    print("The file {i} contains the expression.")
