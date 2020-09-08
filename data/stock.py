
'''
define stock baic information

'''
def class Stock(Object):
   
    def __init__(self, id, name, area, stockEx):
        self.name = name
        self.id = id
        self.price = 0
        self.lastTradeTime = ""
        self.area = ""
        self.stockEx = ""
        
    def getID(self):
        return self.id
    def getFullID(self):
        self.stockEx+self.name
    def getName(self):
        return self.name
        
    def getPrice(self):
        return self.price
    def setPrice(self, price):
        self.price = price
    
    def getLastTradeTime(self):
        return self.lastTradeTime
    def setLastTradeTime(self, time):
        return self.lastTradeTime = lastTradeTime
    
        
    