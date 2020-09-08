#!python
'''
test program
'''

from stock import Stock
from stockProxy import StockProxy
from stockProxySina import StockProxySina

def test():
    print("Test StockProxySina")
    stock1 = Stock('01810', '小米集团-W' ,'hangkong' , 'hk')
    stock2 = Stock('002415', '海康威视' ,'shenzhen' , 'sz')
    stockProxy = StockProxySina()
    stockProxy.updatePrice(stock1)
    print(stock1.getFullID() + " price:" + str(stock1.getPrice()))
    stockProxy.updatePrice(stock2)
    print(stock2.getFullID() + " price:" + str(stock2.getPrice()))
    
if __name__ == '__main__':
    test()