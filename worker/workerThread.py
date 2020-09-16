from threading import Thread
import time
import sys
sys.path.append("..")
from data.stock import Stock
from data.stockProxy import StockProxy
from data.stockProxySina import StockProxySina
from policy.purePricePolicy import PurePricePolicy
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
            for i in self.stockSet:
                self.policy.runOneTime(self.stockSet[i])
            time.sleep(self.policy.interval)    
