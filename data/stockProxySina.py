import abc  
import requests
import logging
import traceback
import abc  
#from data.stock import Stock
from .stockProxy import StockProxy
from datetime import datetime
'''
HangKong stock
request: http://hq.sinajs.cn/list=hk01810
response:
var hq_str_hk01810="NULL,小米集团－Ｗ,24.500,24.150,24.700,21.800,22.400,-1.750,-7.246,22.350,22.400,7971420598,348240834,367.213,0.000,26.950,8.350,2020/09/08,16:08";
NULL,  : 
小米集团－Ｗ, : name
24.500, : start price in the day
24.150, : end price in the lprevious day
24.700, : current price
21.800, : lowest price in the day
22.400, : highest price in the day
-1.750, : 
-7.246, : up/down percent 
22.350,
22.400,
7971420598,
348240834,
367.213,
0.000,
26.950,
8.350,
2020/09/08,16:08

'''

'''
chinese A stock
http://hq.sinajs.cn/list=sz002415
var hq_str_sz002415="海康威视,36.550,36.390,36.300,36.950,35.980,36.290,36.300,42320922,1540964535.920,25100,36.290,7100,36.280,8200,36.270,17300,36.260,31300,36.250,1599,36.300,900,36.310,1300,36.320,7900,36.330,12900,36.340,2020-09-08,15:00:03,00";
海康威视,
36.550,
36.390,
36.300, : current price
36.950,
35.980,
36.290,
36.300,
42320922,
1540964535.920,
25100,
36.290,
7100,
36.280,
8200,
36.270,
17300,
36.260,
31300,
36.250,
1599,
36.300,
900,
36.310,
1300,
36.320,
7900,
36.330,
12900,
36.340,
2020-09-08,15:00:03,00
'''

class StockProxySina(StockProxy):
    API_URL = "http://hq.sinajs.cn/list="
    
    def __init__(self):
        self.url=self.API_URL
        self.dataArray=[]
        self.name = "sina"
    def updatePrice(self, stock):
        stockInfo = {}
        url=self.url + stock.getFullID()
        try:
            r = requests.get(url, timeout=3)
        except requests.exceptions.Timeout as e:  
            print("http request timeout :" + url )
            return
        except requests.exceptions.HTTPError as e:  
            print("http request error :" + url )  
            return    
        except requests.exceptions.ReadTimeout as e:  
            print("http request Readtimeout :" + url)   
            return 
        except Exception as e:
            traceback.print_stack()    
            return    
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
        self.dataArray = coreStr.split(',')
        logging.debug("print sina data:")
        logging.debug(self.dataArray)
        #print(self.dataArray)
        if stock.getEx() == 'hk':
            stockInfo['price'] = (float(self.dataArray[6]))
            stockInfo['datetime'] = (datetime.strptime(self.dataArray[17] + " " +  self.dataArray[18], '%Y/%m/%d %H:%M' if self.dataArray[18].count(":") == 1 else '%Y/%m/%d %H:%M:%S') )
        elif  stock.getEx() == 'sh':   
            stockInfo['price'] = (float(self.dataArray[3]))
            stockInfo['datetime'] = (datetime.strptime(self.dataArray[30] + " " +  self.dataArray[31], '%Y-%m-%d %H:%M' if self.dataArray[31].count(":") == 1 else '%Y-%m-%d %H:%M:%S') )
        elif  stock.getEx() == 'sz':   
            stockInfo['price'] =(float(self.dataArray[3])) 
            stockInfo['datetime'] = (datetime.strptime(self.dataArray[30] + " " +  self.dataArray[31], '%Y-%m-%d %H:%M' if self.dataArray[31].count(":") == 1 else '%Y-%m-%d %H:%M:%S') )
        else:
             logging.error("error： don't support Ex" + r.status_code + ",url:" + r)        
        return ('sina', stockInfo)
    
    def getPrice(self, stockFullID, time=""):
        pass

    def getName(self):
        return 'sina'
