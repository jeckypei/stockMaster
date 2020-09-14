# stockMaster is software for chinese A/H stock system
此软件为股票投资辅助工具， Contact Me: WeChat: realjecky , mail: jeckypei@163.com

最终基本模块: 
 
    a) 观察（发现新股票，买卖机会）。  #todo
    
    b) 股票数据获取。 #only support sina and get price， 目前数据获取 没有使用tushare，试用过，糟糕的安装体验，python包依赖的通病。 如果为了获取更多数据不排斥tushare 
    
    c)决策/策略(综合不同策略做出决策)。  # 目前只根据期望价格 简陋
    
    d)预测（公式预测，AI预测）。  #todo
    
    e)通知（打印，邮件#todo，图形#todo）。
 

==========================================================================================================================================


  
  

（1）. how to run this program ?  如何安装运行软件 ？

  1.a） 安装python3. install python3 package on your OS 

  1.b) 下载该库  
     git命令： git clone https://github.com/jeckypei/stockMaster.git
     
     WEB下载文件：     https://github.com/jeckypei/stockMaster/archive/master.zip
  
  1.c)  启动命令start commands:   cd stockMaster ; python3 ./stockMaster.py


（2） configurations 
  in dir : ./config/
  
  
（3） To do list: 
 
 从其他财经site: tencent, hexun,xueqiu获取股票信息
 
 email 通知
 
 #WeChat 通知
 
 Notify 配置文件 
 
 AI预测股价
 
 
（4） release notes

  v1.0:
    get price from sina and judge price by PurePricePolicy, then Notify(print)


（5） bug list
  list it in issues 
  
  
（6）refer doc
     https://blog.csdn.net/otter1010/article/details/105884256/



