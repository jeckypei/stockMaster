import abc  
import requests
import logging

import abc  
#from data.stock import Stock
from .stockProxy import StockProxy
from datetime import datetime
'''
http://qt.gtimg.cn/q=hk01810
v_hk01810="100~小米集团-W~01810~22.700~23.550~22.500~515573542.0~0~0~22.700~0~0~0~0~0~0~0~0~0~22.700~0~0~0~0~0~0~0~0~0~515573542.0~2020/09/15 11:17:03~-0.850~-3.61~22.850~22.350~22.700~515573542.0~11632301523.050~0~49.74~~0~0~2.12~5476.861~5476.861~XIAOMI-W~0.00~26.950~8.350~7.58~30.22~0~0~0~0~0~42.89~5.44~2.14~200~110.58~~GP~1.83~0.83";

['100',
 '\\xd0\\xa1\\xc3\\xd7\\xbc\\xaf\\xcd\\xc5-W', 
 '01810', 
 '22.750', 
 '23.550', 
 '22.500', 
 '519189492.0', 
 '0', 
 '0', 
 '22.750', 
 '0', 
 '0', 
 '0', 
 '0', 
 '0', 
 '0', 
 '0', 
 '0', 
 '0', 
 '22.750', 
 '0', 
 '0', 
 '0', 
 '0', 
 '0', 
 '0', 
 '0', 
 '0', 
 '0', 
 '519189492.0', 
 '2020/09/15 11:25:39', 
 '-0.800', 
 '-3.40', 
 '22.850', 
 '22.350', 
 '22.750', 
 '519189492.0', 
 '11714386896.150', 
 '0', 
 '49.85', 
 '', 
 '0', 
 '0', 
 '2.12', 
 '5488.924', 
 '5488.924', 
 'XIAOMI-W', 
 '0.00', 
 '26.950', 
 '8.350', 
 '7.11', 
 '29.28', 
 '0', 
 '0', 
 '0', 
 '0', 
 '0', 
 '42.98', 
 '5.45', 
 '2.15', 
 '200', 
 '111.04', 
 '', 
 'GP', 
 '1.83', 
 '0.8']


'''

class StockProxyTencent(StockProxy):
    API_URL = "http://qt.gtimg.cn/q="
    
    def __init__(self):
        self.url=self.API_URL
        self.dataArray=[]
        self.name = "tencent"
    def updatePrice(self, stock):
        stockInfo = {}
        url=self.url + stock.getFullID()
        r = requests.get(url, timeout=3)
        if r == None:
            print("http request " + url + "Fail, no response")
            return None
        logging.debug(url)
        if r.status_code != requests.codes.ok :
            logging.error("http request error： " + r.status_code + ",url:" + r)    
            print("http request " + url + "Fail, error code: " + r.status_code)
            return None
        #print(r.content)
        dataStr = str(r.content)
        start = dataStr.find("\"", 0)
        end = dataStr.find("\"",start + 1)
        coreStr = str(dataStr[start + 1:end - 1])
        self.dataArray = coreStr.split('~')
        logging.debug("print tencent data:")
        logging.debug(self.dataArray)
        #print(self.dataArray)
        #print("index 30 : " + self.dataArray[30])
        if stock.getEx() == 'hk':
            stockInfo['price'] = (float(self.dataArray[3]))
            stockInfo['datetime'] = (datetime.strptime(self.dataArray[30], '%Y/%m/%d %H:%M' if self.dataArray[31].count(":") == 1 else '%Y/%m/%d %H:%M:%S') )
        elif  stock.getEx() == 'sh':   
            stockInfo['price'] = (float(self.dataArray[3]))
            stockInfo['datetime'] = (datetime.strptime(self.dataArray[30], '%Y%m%d%H%M%S') )
        elif  stock.getEx() == 'sz':   
            stockInfo['price'] = (float(self.dataArray[3])) 
            stockInfo['datetime'] = (datetime.strptime(self.dataArray[30], '%Y%m%d%H%M%S') )
        else:
             logging.error("error： don't support Ex" + r.status_code + ",url:" + r)        
        return ('tencent', stockInfo)
    
    def getPrice(self, stockFullID, time=""):
        pass

    def getName(self):
        return 'sina'
