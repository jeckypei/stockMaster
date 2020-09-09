#!/usr/bin/python3
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
    sinaproxy = StockProxySina()
    stock1.addProxy(sinaproxy)
    print(stock1.getFullID() + " price:" + str(stock1.getPrice()))
    stock2.addProxy(sinaproxy)
    print(stock2.getFullID() + " price:" + str(stock2.getPrice()))
    
if __name__ == '__main__':
    test()
