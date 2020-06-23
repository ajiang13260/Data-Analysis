# 问题1 创建一个边界为1，内部为0的二维数组
# import numpy as np
# x = np.ones((10,10))
# print(x)
# x[1:-1,1:-1] = 0
# print(x)

    # 补充
# 创建一个10*10的全1数组
# import numpy as np
# x = np.ones((10,10))
# y = np.full((10,10),1)
# # print(x)
# # print(y)
# z = np.full((10,10),np.pi)
# # print(z)
# j = np.array([[1,2,3],[4,5,6]],dtype=np.float64)
# k = np.full_like(j,3)
# print(k)

# 问题2 如何创建一个单位数组
# import numpy as np
# x = np.identity(10)
# y = np.eye(10)
# print(x)
# print(y)
# z = np.eye(8,k=-1)
# print(z)

# 问题3 如何用radom模块从正态分布和均匀分布中各采样若干元素
# import numpy as np
# r = np.random.normal(0,5,100)
# # print(r)
# u = np.random.uniform(-5,5,100)
# print(u)

# 进一步，对于一个二维数组，如何从中有放回或者无放回地采样k行数据
# import numpy as np
# A = np.random.rand(3,5)
# print(A)
# print(A.shape[0])
# s = np.arange(A.shape[0])
# print(s)
# mask = np.random.choice(s,2,replace=True)
# print(mask)
# print(A[mask])

# 问题4 numpy当中数组的布尔索引
# import numpy as np
# X = np.arange(1,101)
# print(X)
# print(X[X>50])
# print(X[(X<50)&(X%2 == 0)])
# # X[X%2 == 0] = 0
# # print(X)
# XX = np.where(X%2 == 0,-1,X)
# print(XX)

# numpy中矢量化运算和广播的思想
import numpy as np
scores = np.array([[94,99,34],[23,45,78]])
scores_mean = scores.mean(axis=1,keepdims=True)
print(scores-scores_mean)