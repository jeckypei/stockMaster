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
    print(stock1.getFullID() + "\tprice:" + str(stock1.getPrice()) + "\t" +str(stock1.getPriceDatetime()))
    stock2.addProxy(sinaproxy)
    print(stock2.getFullID() + "\tprice:" + str(stock2.getPrice()) + "\t"+ str(stock2.getPriceDatetime()))
    
if __name__ == '__main__':
    test()
