# 寻找n以内的亲密数对。
# 是自己写的失败的版本，经过更改成功了
# def fac(n):
#     for x in range(2,n):
#         y = 0  
#         for i in range(1,x):
#             if x % i == 0:
#                 y += i
#         sumy = 0
#         for k in range(1,y):
#             if y % k == 0:
#                 sumy += k
#         if sumy == x & x < y:
#             print("{}-{}".format(x, y))
# n = int(input('input:'))
# fac(n)

# 网上找的成功版本
# def fac(x):
#     for a in range(2,x): #1肯定不是亲密数，所以不取
#         b = 0
#         for i in range(1,a):
#             if a % i == 0:
#                 b += i
        
#         r = 0
#         for j in range(1,b):
#             if b % j == 0:
#                 r += j
#         if r == a and a < b:
#             print("{}-{}".format(a, b))

# n = int(input())
# fac(n)

# 寻找第n个默尼森数。

