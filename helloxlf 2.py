# 函数式编程
    # 高阶函数
# def add(x,y,f):
#     return f(x)+f(y)

# print(add(-5,6,abs))

    # map/reduce
# def f(x):
#     return x*x
# r = map(f, [1,2,3,4,5,6])
# print(list(r))
# print(r)

# L = []
# for n in [1,2,3,4,5,6]:
#     L.append(f(n))
# print(L)

# print(list(map(str,[1,2,3,4])))
# print(list(map(abs,[-1,-2,3])))

# from functools import reduce
# def fn(x,y):
#     return x*10+y

# print(reduce(fn,[1,2,3,4,5,6,7]))

# def char2num(s):
    # digits = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
#     return digits[s]
# m = map(char2num,'15379')
# print(m)
# n = reduce(fn,m)
# print(n)

# dig = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
# def str2int(s):
#     def fn(x,y):
#         return x*10+y
#     def char2num(s):
#         return dig[s]
#     return reduce(fn,map(char2num,s))

# di = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
# def char2num(s):
#     return di[s]
# def str2int(s):
#     return reduce(lambda x,y: x*10+y, map(char2num,s))
# print(str2int('1357'))

# def normalize(name):
    
# 测试:
# L1 = ['adam', 'LISA', 'barT']
# L2 = list(map(normalize, L1))
# print(L2)