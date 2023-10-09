import numpy as np
# 使用pandas的dataframe创建一个6行5列的整数随机数矩阵
from pandas import DataFrame
#给矩阵添加行索引和列索引
a = DataFrame(np.random.randint(0,10,size=(6,5)),index=['a','b','c','d','e','f'],columns=['A','B','C','D','E'])
print(a)
