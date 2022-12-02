import sys
from datetime import UTC, datetime

date1 = "Jul/10/2019"
datemask = "%b/%d/%Y"
datetime_object1 = datetime.strptime(date1, datemask)
datetime_object2 = datetime.strptime('07/11/2019 02:45PM', '%m/%d/%Y %I:%M%p')
datetime_object3 = datetime.today()
mydate = datetime.strftime(datetime_object1,'%Y-%m-%d')
myyear = datetime.strftime(datetime_object1,'%Y')
tempdate1 = datetime.strptime('Sun 20 Jul 18:00:00 2018', '%a %d %b %H:%M:%S %Y')
tempdate2 = datetime.strptime('2018-07-21', '%Y-%m-%d')
tempdate3 = datetime.strftime(tempdate1, '%H:%M:%S')
print(tempdate1 > tempdate2)
print(tempdate1)
print(tempdate3)
print(mydate)
print(datetime_object1)
print(datetime_object2)
print(datetime_object3)
print(myyear)

dt = datetime(2016, 7, 27, 12, 30, 45, tzinfo=UTC)
print("1: " + str(dt))

dt_now = datetime.now(tz=UTC)
print("2: " + str(dt_now))

dt_utcnow = datetime.utcnow().replace(tzinfo=UTC)
print("3: " + str(dt_utcnow))

date = "2018-13-10"

try:
    dateInput = datetime.strptime(date, '%Y-%m-%d')
    print(dateInput)
except ValueError:
    print('Date not recognized. Use YYYY-MM-DD format.')
    sys.exit()
