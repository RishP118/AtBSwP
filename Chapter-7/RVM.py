
import re
def strp(s,p):
    ask= input("Do you want to remove specific characters from string? ")
    if ask=="No":
        return s.strip()
    else:
        p=input("Enter character to be removed: ")
        sreg=re.compile(p)
        return sreg.sub("", s)
p=""
s= input("Enter: ")
print(strp(s,p))
