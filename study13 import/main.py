#模块 Modules 在Python中一个.py的文件就是一个模块  模块中包含函数，包含类（类属性，类方法），包含语句
#模块性开发 代码复用 团队协作  相同变量名在不同的模块中可以反复利用
#创建模块 = 创建一个.py文件

#导入模块 import 模块名
import math
print(math.pi)
print(dir(math)) #查看模块里面有的一下方法
#第二种导入方法  from 模块名称 import 函数/变量/类   也就是导入模块中的特定的内容
from math import pi
print(pi)


#以主程序的形式运行程序
if __name__ == '__main__':
   pass