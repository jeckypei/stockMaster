'''
test program
'''

import stock
import stockProxy
import stockProxySina

def test():
    stock1 = stock('01810', '小米集团-W' ,'hangkong' , 'hk')
    stockProxy = StockProxySina()
    stockProxy.updatePrice(stock1)
    print(stock1.getPrice())
    
if __name__ == '__main__':
    test()