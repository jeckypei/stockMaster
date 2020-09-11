
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
        ####
        self.ipoPrice = 0
        self.lowestPrice2Year = 0
        self.averagePrice2Year = 0
        self.highestPrice2Year = 0
        self.lowestPrice1Year = 0
        self.averagePrice1Year = 0
        self.highestPrice1Year = 0
        self.lowestPrice6Month = 0
        self.averagePrice6Month = 0
        self.highestPrice6Month = 0
        self.lowestPrice3Month = 0
        self.averagePrice3Month = 0
        self.highestPrice3Month = 0
        self.lowestPriceToday = 0
        self.highestPriceToday = 0
        ####
        self.toBuyPrice = 0
        self.valuePrice = 0
        self.toSalePrice = 0
        
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
