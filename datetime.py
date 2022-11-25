import sys
from datetime import datetime

date1 = "Jul/10/2019"
datemask = "%b/%d/%Y"
datetime_object1 = datetime.strptime(date1, datemask)
datetime_object2 = datetime.strptime('07/11/2019 02:45PM', '%m/%d/%Y %I:%M%p')
datetime_object3 = datetime.today()
mydate = datetime.strftime(datetime_object1,'%Y-%m-%d')
myyear = datetime.strftime(datetime_object1,'%Y')
tempdate1 = datetime.strptime('Sun 20 Jul 18:00:00 2018', '%a %d %b %H:%M:%S %Y')
tempdate2 = datetime.strptime('2018-07-21', '%Y-%m-%d')
print(tempdate1 > tempdate2)
print(tempdate1)
print(mydate)
print(datetime_object1)
print(datetime_object2)
print(datetime_object3)
print(myyear)
date = "2018-13-10"
try:
    dateInput = datetime.strptime(date, '%Y-%m-%d')
    print(dateInput)
except ValueError:
    print('Date not recognized. Use YYYY-MM-DD format.')
    sys.exit()