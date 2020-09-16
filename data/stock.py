
'''
define stock baic information

'''
from datetime import datetime
from .stockProxy import StockProxy

class Stock(object):
   
    def __init__(self, id, name, area, ex):
        self.name = name
        self.id = id
        self.area = area
        self.ex = ex
        self.price = 0
        self.pe = 0
        self.roe = 0        
        self.proxy = {}
        self.proxyPrice = {}
        self.proxySrc = ""
        self.newestProxy = None
        self.datetime = None
        self.reqDatetime  = None
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
        self.lowestPrice1Month = 0
        self.averagePrice1Month = 0
        self.highestPrice1Month = 0
        self.lowestPrice5Day = 0
        self.averagePrice5Day = 0
        self.highestPrice5Day = 0
        self.startPriceInDay = 0
        self.endPriceInDay = 0
        self.lowestPriceInDay = 0
        self.highestPriceInDay = 0
        ####
        self.toBuyPrice = 0
        self.valuePrice = 0
        self.toSalePrice = 0
        self.notifyToBuy = False
        self.notifyToSale = False
        self.notifyKeep = False
        
    def setInfo(self, config):
        self.price = config["price"]
        self.pe = config["pe"]
        self.roe = config["roe"]   
        if (len(config["datetime"]) > 0) :
            self.datetime = datetime.strptime(config["datetime"], '%Y-%m-%d %H:%M' if config["datetime"].count(":") == 1 else '%Y-%m-%d %H:%M:%S')
        ####
        self.ipoPrice = config["ipoPrice"]
        self.lowestPrice2Year = config["lowestPrice2Year"]
        self.averagePrice2Year = config["averagePrice2Year"]
        self.highestPrice2Year = config["highestPrice2Year"]
        self.lowestPrice1Year = config["lowestPrice1Year"]
        self.averagePrice1Year = config["averagePrice1Year"]
        self.highestPrice1Year = config["highestPrice1Year"]
        self.lowestPrice6Month = config["lowestPrice6Month"]
        self.averagePrice6Month = config["averagePrice6Month"]
        self.highestPrice6Month = config["highestPrice6Month"]
        self.lowestPrice3Month = config["lowestPrice3Month"]
        self.averagePrice3Month = config["averagePrice3Month"]
        self.highestPrice3Month = config["highestPrice3Month"]
        self.lowestPrice1Month = config["lowestPrice1Month"]
        self.averagePrice1Month = config["averagePrice1Month"]
        self.highestPrice1Month = config["highestPrice1Month"]
        self.lowestPrice5Day = config["lowestPrice5Day"]
        self.averagePrice5Day = config["averagePrice5Day"]
        self.highestPrice5Day = config["highestPrice5Day"]
        self.startPriceInDay = config["startPriceInDay"]
        self.endPriceInDay = config["endPriceInDay"]
        self.lowestPriceInDay = config["lowestPriceInDay"]
        self.highestPriceInDay = config["highestPriceInDay"]
        ####
        self.toBuyPrice = config["toBuyPrice"]
        self.valuePrice = config["valuePrice"]
        self.toSalePrice = config["toSalePrice"]
        ####
        for p in config["proxy"]:
            self.addProxy(StockProxy.newStockProxy(p))
           
    def getID(self):
        return self.id
    
    def getArea(self):
        return self.name

    def getFullID(self):
        return self.ex + self.id

    def getName(self):
        return self.name

    def getEx(self):
        return self.ex
    
    def getPe(self):
        return self.pe
    def setPe(self, pe):
        self.pe = pe
        
    def getRoe(self, roe):
        return self.roe
    def setRoe(self, roe):
        self.roe = roe

       
    def getPrice(self):
        self.updatePrice()
        return self.price

    def updatePrice(self):
        self.proxyPrice = {}
        self.newestProxy = None
        for i in self.proxy:
            rp = self.proxy[i].updatePrice(self)
            if (rp != None):
                self.proxyPrice[rp[0]] = rp [1]
                if self.newestProxy == None and rp[1]['price'] > 0:  
                    self.newestProxy = rp[0]
                elif self.proxyPrice[rp[0]]['datetime'] > self.proxyPrice[self.newestProxy]['datetime'] and rp[1]['price'] > 0:   
                    self.newestProxy = rp[0]
        if self.newestProxy != None:            
            #print("price from: " + self.newestProxy)
            self.price = self.proxyPrice[self.newestProxy]['price']
            self.datetime = self.proxyPrice[self.newestProxy]['datetime']
            self.proxySrc = self.newestProxy
            self.reqDatetime = datetime.now()
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

    def getIpoPrice(self, price):
        return self.ipoPrice
    def setIpePrice(self, price):
        self.ipoPrice = price
    
    def getIpoPrice(self, price):
        return self.ipoPrice
    def setIpePrice(self, price):
        self.ipoPrice = price
            
    def addProxy(self, proxy):
        self.proxy[len(self.proxy)] = proxy    

    def delProxy(self, proxy):
        del self.proxy[proxy.getName()]   
