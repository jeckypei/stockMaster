
'''
define stock baic information

'''
from datetime import datetime

class Stock(object):
   
    def __init__(self, id, name, area, ex):
        self.name = name
        self.id = id
        self.price = 0
        self.area = area
        self.ex = ex
        self.proxy = {}
        self.datetime = datetime.now()
        
    def getID(self):
        return self.id

    def getFullID(self):
        return self.ex + self.id

    def getName(self):
        return self.name

    def getEx(self):
        return self.ex
        
    def getPrice(self):
        self.updatePrice()
        return self.price

    def updatePrice(self):
        if len(self.proxy) > 0 :
            self.proxy[0].updatePrice(self)
        
    def setPrice(self, price):
        self.price = price
    def setPriceDatetime(self, dt):
        self.datetime = dt    
    def getPriceDatetime(self):
        return self.datetime      
    
    def getLastTradeTime(self):
        return self.lastTradeTime
    
    def setLastTradeTime(self, time):
        self.lastTradeTime = time
        
    def addProxy(self, proxy):
        self.proxy[len(self.proxy)] = proxy    

    def delProxy(self, proxy):
        del self.proxy[proxy.getName()]   
