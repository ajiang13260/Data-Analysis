    # 生成器	
# L = [x * x for x in range(10)]	
# g = (x * x for x in range(10))	
# # print(L,g)	
# # while True:	
# #     print(next(g))	
# for n in g:	
#     print(n)	

# def fib(max):	
#     n,a,b=0,0,1	
#     while n < max:	
#         # print (b)	
#         yield b	
#         n = n+1	
#         a,b = b,a+b	
#     return 'done'	

# print(fib(6))	

# def odd():	
#     print('step1')	
#     yield 1	
#     print('step2')	
#     yield 2	
#     print('step3')	
#     yield 3	
# o = odd()	
# print(next(o))	
# print(next(o))	
# print(next(o))	

# for n in fib(6):	
#     print(n)	

# g = fib(6)	
# while True:	
#     try:	
#         x = next(g)	
#         print('g:',x)	
#     except StopIteration as e:	
#         print('General reeturn value:',e.value)	
#         break	

# def triangless():	
#     L = [1]	
#     while 1:	
#         yield L	
#         L = [0] + L + [0]	
#         L = [L[i] + L[i+1] for i in range(len(L)-1)]	


# 期待输出:	
# [1]	
# [1, 1]	
# [1, 2, 1]	
# [1, 3, 3, 1]	
# [1, 4, 6, 4, 1]	
# [1, 5, 10, 10, 5, 1]	
# [1, 6, 15, 20, 15, 6, 1]	
# [1, 7, 21, 35, 35, 21, 7, 1]	
# [1, 8, 28, 56, 70, 56, 28, 8, 1]	
# [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]	

# 测试	
# n = 0	
# results = []	
# for t in triangless():	
#     results.append(t)	
#     n = n + 1	
#     if n == 10:	
#         break	
# for t in results:	
#     print(t)	

# if results == [	
#     [1],	
#     [1, 1],	
#     [1, 2, 1],	
#     [1, 3, 3, 1],	
#     [1, 4, 6, 4, 1],	
#     [1, 5, 10, 10, 5, 1],	
#     [1, 6, 15, 20, 15, 6, 1],	
#     [1, 7, 21, 35, 35, 21, 7, 1],	
#     [1, 8, 28, 56, 70, 56, 28, 8, 1],	
#     [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]	
# ]:	
#     print('测试通过')	
# else:	
#     print('测试失败')	