import sys
sys.path.append("..")
from data.stock import Stock
import time
class PurePricePolicy :
    def __init__(self, interval = 5, loopCount = -1):
        self.loopCount = loopCount
        self.interval = interval
        self._stop = False
    def flow(self, stock) :
        if stock.getPrice() <= stock.toBuyPrice: 
            print ("To Buy: " + stock.getFullID() + " "  + stock.getName() + " CurrentPrice " + str(stock.price) + " <= " + str(stock.toBuyPrice) )
        else:
            pass
            #print ("Don't Buy: " + stock.getFullID() + " "  + stock.getName() + " CurrentPrice " + str(stock.price) + " > " + str(stock.toBuyPrice) )
        #    
        if stock.getPrice() >= stock.toSalePrice: 
            print ("To Sale: " + stock.getFullID() + " "  + stock.getName() + " CurrentPrice " + str(stock.price) + " >= " + str(stock.toSalePrice) )
        else:
            pass
            #print ("Don't Safe: " + stock.getFullID() + " "  + stock.getName() + " CurrentPrice " + str(stock.price) + " < " + str(stock.toSalePrice) )
            
    '''            
    def run(self, stock):
        while ((self._stop == False) and (self.loopCount < 0 or self.loopCount > 0 )) :
            self.flow(stock)    
            self.loopCount -= 1
            time.sleep(self.interval)
    '''        
    
    def runOneTime(self, stock):
            self.flow(stock)    
    def stop(self):
        self._stop = True       
         