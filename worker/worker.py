import sys
sys.path.append("..")
from data.stock import Stock
from data.stockProxy import StockProxy
#from data.stockProxySina import StockProxySina
from policy.purePricePolicy import PurePricePolicy
import json
import os
from worker.workerThread import WorkerThread
from notify.notify import Notify


class Worker:
    def __init__(self, configDir):
        self.configDir = configDir
        self.stockDir = configDir + "stock"
        self.policyConfig = {}
        self.stockSet = {}
        self.notify = Notify(configDir)
        pass
    def loadPolicy(self):
        print("load policyfile : " + self.configDir + "policy.json")
        with open(self.configDir + "policy.json", "r") as pf:
            self.policyConfig = json.load(pf)
        #print(self.policyConfig)    
                
    def loadStock(self):
        print("load stock list from : " + self.stockDir)
        flist = os.listdir(self.stockDir) 
        for i in flist:
            fpath = os.path.join(self.stockDir,i)
            print ("  load stock: "+ fpath)
            if not os.path.isfile(fpath):
                continue
            with open(fpath, "r") as pf:
                config = json.load(pf)
                self.addStock(config)
    def startNotify(self):
        print("start notify")
        self.notify.start()           
                
    def addStock(self, config):
        stock = Stock(config["id"], config["name"] ,config["area"] , config["ex"])
        print("  Stock: " + stock.getFullID() + " " + stock.getName())
        self.stockSet[stock.getFullID()] = stock
        stock.setInfo(config)
        pass
    
    def startWork(self):
        self.loadStock()
        self.loadPolicy()
        self.startNotify()
        if self.policyConfig["shareThreadNum"] == 0 :
            self.runPerThread()
        elif self.policyConfig["shareThreadNum"] == 1 :    
            self.runOneThread()
              
    def runPerThread(self):
        print("Per Worker thread")
        if self.policyConfig["defaultPolicy"] == "purePricePolicy" :
            policy = PurePricePolicy(self.notify, self.policyConfig["interval"], self.policyConfig["nonTradeInterval"])
        for i in self.stockSet:
            ss = {}
            ss[0] = self.stockSet[i]
            thread = WorkerThread(ss, policy)
            thread.start()    
                
    def runOneThread(self):
        print("One Worker thread")
        if self.policyConfig["defaultPolicy"] == "purePricePolicy" :
            policy = PurePricePolicy(self.notify, self.policyConfig["interval"], self.policyConfig["nonTradeInterval"])
        thread = WorkerThread(self.stockSet, policy)
        thread.start()      
                
