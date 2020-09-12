import sys
sys.path.append("..")
from data.stock import Stock
from data.stockProxy import StockProxy
from data.stockProxySina import StockProxySina
from policy.purePricePolicy import PurePricePolicy
import json
import os
from worker.workerThread import WorkerThread

class Worker:
    def __init__(self, configDir):
        self.configDir = configDir
        self.stockDir = configDir + "stock"
        self.policyConfig = {}
        self.stockSet = {}
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
                
    def addStock(self, config):
        stock = Stock(config["id"], config["name"] ,config["area"] , config["ex"])
        print("  Stock: " + stock.getFullID() + " " + stock.getName())
        self.stockSet[stock.getFullID()] = stock
        stock.setInfo(config)
        pass
    
    def startWork(self):
        self.loadStock()
        self.loadPolicy()
        if self.policyConfig["shareThreadNum"] == 0 :
            self.runPerThread()
        elif self.policyConfig["shareThreadNum"] == 1 :    
            self.runOneThread()
              
    def runOneThread(self):
        if self.policyConfig["defaultPolicy"] == "purePricePolicy" :
            policy = PurePricePolicy(self.policyConfig["interval"])
        for i in self.stockSet:
            ss = {}
            ss[0] = self.stockSet[i]
            thread = WorkerThread(ss, policy)
            thread.start()    
                
    def runPerThread(self):
        if self.policyConfig["defaultPolicy"] == "purePricePolicy" :
            policy = PurePricePolicy(self.policyConfig["interval"])
        thread = WorkerThread(self.stockSet, policy)
        thread.start()      
                
