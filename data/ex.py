
import datetime
def isTradeTime(ex):
    dt = datetime.datetime.now()
    secondInDay = dt.hour*60*60 + dt.minute * 60 + dt.second
    if ex == 'hk' :
        startTime = 8 * 60*60 + 59*60 
        endTime = 16 * 60*60 + 10*60 
    elif ex == 'all':
        startTime = 8 * 60*60 + 59*60 
        endTime = 16 * 60*60 + 10*60 
    elif ex == 'sh' or ex == "sz":
        startTime = 9 * 60*60 + 14*60 
        endTime = 15 * 60*60 + 1*60       
    if (dt.weekday() <= 4) and  (secondInDay >= startTime and secondInDay <= endTime):
        return True
    return False  

