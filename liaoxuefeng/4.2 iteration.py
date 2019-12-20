    # 迭代	
# d = {'a':1, 'b':2, 'c':3}	
# for key in d:	
#     print(key)	

# for value in d.values():	
#     print(value)	

# for k,v in d.items():	
#     print(k,v)	

# for ch in 'ABC':	
#     print(ch)	

# from collections.abc import Iterable	
# print(isinstance('abc', Iterable))	
# print(isinstance([1,2,3], Iterable))	
# print(isinstance(123, Iterable))	

# for i, value in  enumerate(['A','B','C']):	
#     print(i,value)	

# def findMinAndMax(L):	
#     if L == []:	
#         min = None	
#         max = None	
#     else:	
#         min = L[0]	
#         max = L[0]	
#         for i in L:	
#             if i < min:	
#                 min = i	
#             if i > max:	
#                 max = i	
#     return (min,max)	

# # 测试	
# if findMinAndMax([]) != (None,None):	
#     print('测试失败1')	
# elif findMinAndMax([7]) != (7,7):	
#     print('测试失败2')	
# elif findMinAndMax([7,1]) != (1,7):	
#     print('测试失败3')	
# elif findMinAndMax([7,1,3,9,5]) != (1,9):	
#     print('测试失败4')	
# else:	
#     print('测试成功')	