import abc  
import requests

class StockProxySina(stockProxy):
    STOCK_API_URL_SINA="http://hq.sinajs.cn/list="
    def __init__(self)
        self.url=STOCK_API_URL_SINA
        
    def updatePrice(self, stock):
        url=self.url + stock.getID()
    
    def getPrice(self, stockFullID, time):
        requests.get()
