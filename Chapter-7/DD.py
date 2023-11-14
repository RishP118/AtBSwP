
import re
date=re.compile(r'(\d\d)/(\d{2})/(\d{4})')
s=date.search('11/08/2023')
day=str(s.group(1))
month=str(s.group(2))
year=str(s.group(3))
if int(year)>=1000 and int(year)<=2999:
    if month in ["04","06","09","11"]:
        if int(day)<=30:
            print(s.group())
        else:
            print("The date does not exist.")
      if month in ["01","03","05","07","08","10","12"]:
        if int(day)<=31:
            print(s.group())
        else:
            print("The date does not exist.")
    if month=="02":
        if int(year)%400==0 or int(year)%100!=0 and int(year)%4==0) and int(day)<=29:
		print(s.group())

        elif month=="02" and not int(year)%400==0or int(year)%100!=0 and int(year)%4==0) and int(day)<=28:
            print(s.group())
        else:
            "The date does not exist."
else:
    print("The date does not exist.")

