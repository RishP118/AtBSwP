import re
def spd(p):
    if len(p)<8:
        return False
    elif re.search('[0-9]|[A-Z]|[a-z]',p) is None:
        return False
    else:
        return True
p=input("Password: ")
if spd(p):
    print("Strong.")
else:
    print("Weak.")
