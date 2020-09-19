import sys
sys.path.append("..")
from data.stock import Stock
import time
from notify.notify import Notify
class PurePricePolicy :
    def __init__(self, notify = None, interval = 5, nonTradeInterval = 1800, loopCount = -1):
        self.notify = notify
        self.loopCount = loopCount
        self.interval = interval
        self.nonTradeInterval = nonTradeInterval
        self._stop = False
    def flow(self, stock) :
         price = stock.getPrice()
         if price <= stock.toBuyPrice: 
            if stock.notifyToBuy == False:
                 self.notify.addToBuyStock(stock)
                 stock.notifyToBuy = True
            if stock.notifyToSale == True:
                 self.notify.delToSaleStock(stock)
                 stock.notifyToSale = False   
            if stock.notifyKeep == True:
                 self.notify.delKeepStock(stock)
                 stock.notifyKeep = False          
         elif price >= stock.toSalePrice: 
            if stock.notifyToSale == False:
                 self.notify.addToSaleStock(stock)
                 stock.notifyToSale = True
            if stock.notifyToBuy == True:
                 self.notify.delToBuyStock(stock)
                 stock.notifyToBuy = False 
            if stock.notifyKeep == True:
                 self.notify.delKeepStock(stock)
                 stock.notifyKeep = False         
         else: 
            if stock.notifyKeep == False:
                 self.notify.addKeepStock(stock)
                 stock.notifyKeep = True  
            if stock.notifyToBuy == True:
                 self.notify.delToBuyStock(stock)
                 stock.notifyToBuy = False
            if stock.notifyToSale == True:
                 self.notify.delToSaleStock(stock)
                 stock.notifyToSale = False
               

    
    def runOneTime(self, stock):
            self.flow(stock)    
    def stop(self):
        self._stop = True       
         