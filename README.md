# 中国版多因子模型的构建、检验与对比
主要参考文献：

1 Liu, J., Stambaugh, R. F., & Yuan, Y. (2019). Size and value in China.Journal of Financial Economics,134(1), 48-69.

2 Liu, Y., C. Shi, and X. Lian (2019). Refined book-to-market ratio and the cross-section of stock returns in China. Working paper.


## 说明
无论是Github还是CSDN上关于中国版多因子模型的相关讨论较少。
有关Fama_French三、五因子的文件也较少展示数据处理的完整过程。
因此本文将基于python展示:
 
 - 如何通过通过股票日交易数据构建月度因子.
 - Automatically installs QCMA USB drivers if necessary.
 - Gets AID and QCMA directory from QCMA automatically.
 - Automatically downloads required tools (psvimgtools, pkg2zip, bittersmile demo and h-encore itself).
 - Allows user to import necessary files if they've already downloaded them *(optional)*.
 - Grabs CMA encryption key from your account ID.
 - Unpackages bittersmile and repackages it with your encryption key and h-encore.
 - Trims excess bittersmile demo files to reduce h-encore file size from ~240MB to ~13MB **without breaking trophy fix** *(optional)*.
 - Moves finished files to your QCMA directory for copying to your PS Vita.
 - Holds your hand along the way.
 
Basically, you just need to read and interact with your Vita.

## 数据处理过程

This application does everything required for h-encore related to your PC. This means:
 
 - Automatically installs and configures QCMA if it is not already installed.
 - Automatically installs QCMA USB drivers if necessary.
 - Gets AID and QCMA directory from QCMA automatically.
 - Automatically downloads required tools (psvimgtools, pkg2zip, bittersmile demo and h-encore itself).
 - Allows user to import necessary files if they've already downloaded them *(optional)*.
 - Grabs CMA encryption key from your account ID.
 - Unpackages bittersmile and repackages it with your encryption key and h-encore.
 - Trims excess bittersmile demo files to reduce h-encore file size from ~240MB to ~13MB **without breaking trophy fix** *(optional)*.
 - Moves finished files to your QCMA directory for copying to your PS Vita.
 - Holds your hand along the way.
 
Basically, you just need to read and interact with your Vita.


## 数据来源

This application does everything required for h-encore related to your PC. This means:
 
 - 考虑到本文的受众主要为中国高校学生，且本文作者主要偏向于学术研究，因此将使用中国较为常用的CSMAR数据库的股票交易数据.
 - 为了方便数据处理本文.
 - Gets AID and QCMA directory from QCMA automatically.
 - Automatically downloads required tools (psvimgtools, pkg2zip, bittersmile demo and h-encore itself).
 - Allows user to import necessary files if they've already downloaded them *(optional)*.
 - Grabs CMA encryption key from your account ID.
 - Unpackages bittersmile and repackages it with your encryption key and h-encore.
 - Trims excess bittersmile demo files to reduce h-encore file size from ~240MB to ~13MB **without breaking trophy fix** *(optional)*.
 - Moves finished files to your QCMA directory for copying to your PS Vita.
 - Holds your hand along the way.

## 小声哔哔


 
## Thanks
