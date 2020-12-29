import time
from datetime import datetime, date

# printing date and time values
# for the current date/time

print(time.time())  # timestamp
# Output format: 1609228015.0294833

print(time.localtime(time.time()))  # time struct
# Output format: time.struct_time(tm_year=2020, tm_mon=12, tm_mday=29, tm_hour=2, tm_min=46, tm_sec=55, tm_
# wday=1, tm_yday=364, tm_isdst=0)

print(date.today())  # current date part of ISO 8601 format
# Output format: 2020-12-29

print(datetime.today())  # ISO 8601 date-time
# Output format: 2020-12-29 02:46:55.030485

# Some common date-time conversions
print(datetime.strptime('12/01/2018', '%m/%d/%Y'))
# Output format: 2018-12-01 00:00:00

print(datetime.strptime('12/01/2018', '%m/%d/%Y').isoformat())
# Output format: 2018-12-01T00:00:00

print(datetime.strptime('18/01/12', '%d/%m/%y'))
# Output format: 2012-01-18 00:00:00

print(datetime.strptime('18/01/12', '%d/%m/%y').isoformat())
# Output format: 2012-01-18T00:00:00

print(datetime.strptime('Sun 01 Apr 2018 12:00:00', '%a %d %b %Y %H:%M:%S'))
# Output format: 2018-04-01 12:00:00

print(datetime.strptime('Sun 01 Apr 2018 12:00:00', '%a %d %b %Y %H:%M:%S').isoformat())
# Output format: 2018-04-01T12:00:00
