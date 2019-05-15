import sys
import time
from pytz import timezone
import parsedatetime.parsedatetime as pdt
from datetime import datetime, timedelta


def parse_date(datestring):
    cal = pdt.Calendar()
    maybetime=""
    try:
        maybetime = cal.parse(datestring)
        print("Time from {}".format(datestring))
        print(maybetime)
    except:
        maybetime = cal.parse("tomorrow")
            
    remindtime = time.strftime('%Y-%m-%d %H:%M:%S', maybetime[0]) 
    return remindtime
