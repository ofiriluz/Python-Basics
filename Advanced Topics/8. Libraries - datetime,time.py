# Time is a standard library used for time conventions
# This library is also used by other libraries such as datetime and calender
# The use of this library is to provide information about time c-style
# Its most common use however, is to sleep a thread
import time
time.sleep(3.2) # Seconds
# We can use time to format as we know in c style
time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.gmtime())
time.strptime("30 Nov 00", "%d %b %y")
# We use this to return the time epoch
time.time()
# The datetime library is used to more properly work with dates and times
# It provides basic date and time objects and is more of an high level library for working with time
import datetime
# We can use now to return the datetime object of the current time
# Note that the datetime is a module inside the more global datetime package
datetime.datetime.now()
datetime.date(2003, 12, 1)
datetime.date.today()
# Datetime also gives timedelta operators to work with
dt1 = datetime.datetime.now()
time.sleep(3)
dt2 = datetime.datetime.now()
time_diff = dt2 - dt1 # Returns a timedelta object

# Lastly the calender package provides utilities for calender working
import calendar