import abc  

class StockProxy(metaclass=abc.ABCMeta):
    @abc.abstractmethod  
    def updatePrice(self, stock):
        pass
    
    @abc.abstractmethod  
    def getPrice(self, stockID, time):
        pass
