from threading import Thread
import time
import datetime
import sys
import traceback
sys.path.append("..")
from data.stock import Stock
from data.stockProxy import StockProxy
from data.stockProxySina import StockProxySina
from policy.purePricePolicy import PurePricePolicy
from data.ex import isTradeTime
class WorkerThread(Thread):
    def __init__(self,stockSet, policy):
        self.stockSet = stockSet
        self.policy = policy
        self._stop = False
        Thread.__init__(self)
        if len(self.stockSet) == 1:
            self.setName("stockMaster.worker-" + self.stockSet[0].getFullID())
        else:
            self.setName("stockMaster.worker-All")

    def run(self):
        while not self._stop :
            try:
                for i in self.stockSet:
                    self.policy.runOneTime(self.stockSet[i])
            except Exception as e:
                print(str(e))
                traceback.print_stack()
            #
            
            if (isTradeTime()) : 
                time.sleep(self.policy.interval)  
            else:
                time.sleep(self.policy.nonTradeInterval)      
