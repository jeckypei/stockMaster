import threading
from threading import Thread
import time
import sys
sys.path.append("..")
from data.stock import Stock
from data.stockProxy import StockProxy
from data.stockProxySina import StockProxySina
#from policy.purePricePolicy import PurePricePolicy

class Notify(Thread) :
    def __init__(self, interval = 10):
        self.event = threading.Event()
        self.toBuyStocks = {}
        self.toBuyLock = threading.Lock()
        self.toSaleStocks = {}
        self.toSaleLock = threading.Lock()
        self.keepStocks = {}
        self.keepLock = threading.Lock()
        self.interval = interval
        self._stop = False
        Thread.__init__(self)
        
    def timerFunc(self):
        self.event.set()
               
    def run(self):
        while (not self._stop and (self.event.wait(self.interval) != None)) :
            self.event.clear()
            self.notifyToBuyStocks()
            self.notifyToSaleStocks()             
            self.notifyKeepStocks()
            print("-----------------------------------------------------------------------------------")
            
    def notifyToBuyStocks(self):
        self.toBuyLock.acquire()
        print ("To Buy Stock (Number:%d)" % len(self.toBuyStocks) )
        for i in self.toBuyStocks:
            stock = self.toBuyStocks[i]
            print ("\t" +stock.getFullID() + "\t"  + stock.getName() + "\tPrice\t" + str(stock.price) + " <= " + str(stock.toBuyPrice) + " " + str(stock.datetime ))
        self.toBuyLock.release()       
    def notifyToSaleStocks(self):
        self.toSaleLock.acquire()
        print ("To Sale Stock (Number:%d)" % len(self.toSaleStocks) )
        for i in self.toSaleStocks:
            stock = self.toSaleStocks[i]
            print ("\t" +stock.getFullID() + "\t"  + stock.getName() + "\tPrice\t" + str(stock.price) + " >= " + str(stock.toSalePrice) + " " + str(stock.datetime ))
        self.toSaleLock.release()     
    def notifyKeepStocks(self):
        self.keepLock.acquire()
        print ("To Keep Stock (Number:%d)" % len(self.keepStocks) )
        for i in self.keepStocks:
            stock = self.keepStocks[i]
            print ("\t" +stock.getFullID() + "\t"  + stock.getName() + "\tPrice\t" + str(stock.price) + " > " + str(stock.toBuyPrice) + " &&  < " + str(stock.toSalePrice) + " " + str(stock.datetime))
        self.keepLock.release()       
    
    def addToBuyStock(self, stock):
        self.toBuyLock.acquire()
        self.toBuyStocks[stock.getFullID()] = stock
        self.toBuyLock.release()
        self.event.set()       
    def delToBuyStock(self, stock):
        self.toBuyLock.acquire()
        del self.toBuyStocks[stock.getFullID()]
        self.toBuyLock.release() 
        self.event.set()         

    def addToSaleStock(self, stock):
        self.toSaleLock.acquire()
        self.toSaleStocks[stock.getFullID()] = stock
        self.toSaleLock.release()
        self.event.set()        
    def delToSaleStock(self, stock):
        self.toSaleLock.acquire()
        del self.toSaleStocks[stock.getFullID()]
        self.toSaleLock.release() 
        self.event.set()   
        
    def addKeepStock(self, stock):
        self.keepLock.acquire()
        self.keepStocks[stock.getFullID()] = stock
        self.keepLock.release()
        self.event.set()        
    def delKeepStock(self, stock):
        self.keepLock.acquire()
        del self.keepStocks[stock.getFullID()]
        self.keepLock.release() 
        self.event.set()   
   
    def stop(self):
        self._stop = True       
