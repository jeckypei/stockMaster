import threading
from threading import Thread
import time
import datetime
import sys
import json
sys.path.append("..")
from data.stock import Stock
from data.stockProxy import StockProxy
import prettytable as prettytable
import smtplib
from email.mime.text import MIMEText
from email.header import Header
#from data.stockProxySina import StockProxySina
#from policy.purePricePolicy import PurePricePolicy

class Notify(Thread) :
    def __init__(self, configDir ):
        self.event = threading.Event()
        self.toBuyStocks = {}
        self.toBuyLock = threading.Lock()
        self.toBuyMsg = ""
        self.toSaleStocks = {}
        self.toSaleLock = threading.Lock()
        self.toSaleMsg = ""
        self.keepStocks = {}
        self.keepLock = threading.Lock()
        self.keepMsg = ""
        self.printMsg = ""
        self.emailMsg = ""
        self.wechatMsg = ""
        self.configDir = configDir
        self.configFile = self.configDir + "/notify.json"
        with open(self.configFile, "r") as pf:
            self.config = json.load(pf)
        self.interval = self.config["interval"]    
        self._stop = False
        Thread.__init__(self)
        
    def timerFunc(self):
        self.event.set()
               
    def run(self):
        while (not self._stop and (self.event.wait(self.interval) != None)) :
            print("\n\n\t\t\t" + str(datetime.datetime.now()))
            self.event.clear()
            self.notify()
            
            
    def notifyToBuyStocks(self):
        self.toBuyMsg = ("\nTo Buy Stock (Number:%d)\n" % len(self.toBuyStocks) )
        tbl = prettytable.PrettyTable()
        tbl.field_names = ["ID", "Name", "source", "Price", "ToBuy Price", "ToSale Price", "Time"]
        self.toBuyLock.acquire()
        for i in self.toBuyStocks:
            stock = self.toBuyStocks[i]
            tbl.add_row([stock.getFullID(), stock.getName(),stock.proxySrc,stock.price ,stock.toBuyPrice, stock.toSalePrice , stock.datetime])
        self.toBuyLock.release() 
        self.toBuyMsg = self.toBuyMsg + tbl.get_string() 
        if self.config["email"]['notifyKeep'] == True:
            self.emailMsg = self.emailMsg + self.toBuyMsg
        if self.config["print"]['notifyKeep'] == True:
            self.printMsg = self.printMsg + self.toBuyMsg      
    def notifyToSaleStocks(self):
        self.toSaleMsg =  ("\nTo Sale Stock (Number:%d)\n" % len(self.toSaleStocks) )
        tbl = prettytable.PrettyTable()
        tbl.field_names = ["ID", "Name", "source", "Price", "ToBuy Price", "ToSale Price", "Time"]
        self.toSaleLock.acquire()
        for i in self.toSaleStocks:
            stock = self.toSaleStocks[i]
            tbl.add_row([stock.getFullID(), stock.getName(),stock.proxySrc,stock.price ,stock.toBuyPrice, stock.toSalePrice , stock.datetime])
        self.toSaleLock.release()     
        self.toSaleMsg = self.toSaleMsg + tbl.get_string() 
        if self.config["email"]['notifyKeep'] == True:
            self.emailMsg = self.emailMsg + self.toSaleMsg
        if self.config["print"]['notifyKeep'] == True:
            self.printMsg = self.printMsg + self.toSaleMsg 
             
    def notifyKeepStocks(self):
        self.keepMsg = ("\nTo Keep Stock (Number:%d)\n" % len(self.keepStocks) )
        tbl = prettytable.PrettyTable()
        tbl.field_names = ["ID", "Name", "source", "Price", "ToBuy Price", "ToSale Price", "Time"]
        self.keepLock.acquire()
        for i in self.keepStocks:
            stock = self.keepStocks[i]
            tbl.add_row([stock.getFullID(), stock.getName(),stock.proxySrc,stock.price ,stock.toBuyPrice, stock.toSalePrice , stock.datetime])
        self.keepLock.release()    
        self.keepMsg = self.keepMsg + tbl.get_string()    
        if self.config["email"]['notifyKeep'] == True:
            self.emailMsg = self.emailMsg + self.keepMsg
        if self.config["print"]['notifyKeep'] == True:
            self.printMsg = self.printMsg + self.keepMsg        
    def notify(self):
        self.printMsg = ""
        self.emailMsg = ""
        self.wechatMsg = ""
        self.notifyToBuyStocks()
        self.notifyToSaleStocks()             
        self.notifyKeepStocks()  
        if len(self.printMsg) > 0:
            print(self.printMsg)
        if len(self.emailMsg) > 0:
            self.sendEmail("StockMaster Notify " + str(datetime.datetime.now()) , self.emailMsg)    
         
    
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
    
    def sendEmail(self, title, content):
        mail_host = self.config["email"]["smtpServer"] 
        mail_port = self.config["email"]["port"] 
        sslEnable = self.config["email"]["sslEnable"] 
        mail_sslPort = self.config["email"]["sslPort"] 
        mail_user = self.config["email"]["id"]     
        mail_password= self.config["email"]["password"]  
        sender = self.config["email"]["sender"]  
        receivers = self.config["email"]["receivers"]    
        message = MIMEText(content, 'plain', 'utf-8')
        #message['From'] = Header("菜鸟教程", 'utf-8')
        #message['To'] =  Header("测试", 'utf-8')
        message['From'] = Header(sender)
        message['To'] = Header(','.join(receivers)) 

        message['Subject'] =  title 
        try:
            if sslEnable == False:
                smtpObj = smtplib.SMTP(mail_host, mail_port) 
                #smtpObj.connect(mail_host, mail_port) 
            else:
                smtpObj = smtplib.SMTP_SSL(mail_host, mail_sslPort) 
            smtpObj.login(mail_user, mail_password)  
            smtpObj.sendmail(sender, receivers, message.as_string())
        except smtplib.SMTPException as e:
            print("Error: could not send email" + str(e))
        finally:
            if (smtpObj != None):
                smtpObj.quit()