import abc  
                

class StockProxy(metaclass=abc.ABCMeta):
    @abc.abstractmethod  
    def updatePrice(self, stock):
        pass
    
    @abc.abstractmethod  
    def getPrice(self, stockID, time):
        pass
    
    @abc.abstractmethod  
    def getName(self):
        pass

    @staticmethod
    def newStockProxy(proxyName) :
        if proxyName == "sina":
            from .stockProxySina import StockProxySina
            return StockProxySina()
        elif proxyName == "tencent":
            from .stockProxyTencent import StockProxyTencent
            return StockProxyTencent()

