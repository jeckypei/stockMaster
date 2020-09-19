
import datetime
def isTradeTime():
    dt = datetime.datetime.now()
    secondInDay = dt.hour*60*60 + dt.minute * 60 + dt.second
    startTime = 8 * 60*60 + 58*60 
    endTime = 16 * 60*60 + 20*60 
    if (dt.weekday() <= 5) and  (secondInDay > startTime and secondInDay < endTime):
        return True
    return False  

