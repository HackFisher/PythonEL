# land_tools
Tools for generating land resouce models
陆地产生逻辑顺序
ele.pkg
- findclosedelem -> 寻找距离资源点附近坐标
- findotherelem -> 生成其他坐标
- putelem -> 生成资源
1. ele.pkg||main.go -> 整数化
2. produce/all.go -> 随机化
3. produce/addCharacteristic.go -> 特殊化,生成保留地标示和地块id
4. map/landData.go -> 统计

首先定义了资源地，然后根据距离寻找距离小于3的关闭地块，
然后生成其他地块，然后判断类型寻找资源


## others
document.md 对于该资源生成规则等的描述

