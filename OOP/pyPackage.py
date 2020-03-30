import  calendar
from datetime import datetime,timedelta

cal=calendar.calendar(2020)
print(type(cal))
print(cal)

t1=datetime.now()
print( t1.strftime("%Y-%m-%d %H:%M:%S"))
td=timedelta(hours=1)
#当前时间加上时间间隔后
print((t1+td).strftime("%Y-%m-%d %H:%M:%S"))

a=int("12345",base=16)