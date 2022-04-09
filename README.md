# 中国版多因子模型的构建、检验与对比
# Construction, Testing and Comparison of Multi-Factor Models in China

本文对于刚从stata转Python的中国用户更加友好。

## 主要参考文献：

1 Liu, J., Stambaugh, R. F., & Yuan, Y. (2019). Size and value in China.Journal of Financial Economics,134(1), 48-69.

2 Liu, Y., C. Shi, and X. Lian (2019). Refined book-to-market ratio and the cross-section of stock returns in China. Working paper.

## 更新
作者获得了Tushare高级接口权限，因此做出如下更新，方便大家调用tushare数据：

1 更新了基于tushar接口的计算方法(2022.04.09)

2 更新了基于NeweyWest的计算方法(2022.04.09)

3 更新了GRS Test方法(2022.04.09)

## 说明
无论是Github还是CSDN上关于中国版多因子模型的相关讨论较少。
有关Fama_French三、五因子的文件也较少展示数据处理的完整过程。
因此本文将基于python展示:
 
 - 如何通过股票日交易数据构建月度因子.
 - 如何通过python清洗和整理面板数据.
 - 如何通过异象检验多因子模型.
 - 如何计算经NeweyWest调整后的T值.
 - 如何使用GRS Test检验两个多因子模型.


## 数据处理过程

主要的数据处理过程如下:
 
 - 剔除ST股、科创板、B股、次新股、退市股.
 - 剔除月度交易少于14天的数据.
 - 剔除缺失值.
 - 对数据进行上下1%的缩尾处理.
 - 为了有效利用因子信息，本文在每月月初调仓一次.
 - 为了简化分析，交易费用设为0.


## 数据来源

数据来源如下:
 
 - 考虑到本文的受众主要为中国高校学生，且本文作者主要偏向于学术研究，因此将使用中国较为常用的CSMAR数据库（使用csmar对stata用户也更友好）.
 - 为了方便数据处理，本文调用了tushare基本库的数据（注册即可调用）.


## 小声哔哔
由于本文作者正在攻读博士学位，所以后续将视情况更新多因子模型的相关代码。

 
## Thanks
