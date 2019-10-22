#!/usr/bin/env python3
#-*- coding:utf-8 -*-

# 第一个python程序
    # 输入和输出
# name = 'Pheobe'
# print('hello,',name)
# name2 = input('enter your name:')
# print('hello',name2)
# print('1024 * 768 =',1024 * 768)

# python基础
    # 数据类型和变量
# print('I\'m OK.')
# print('I\'m learning\npython')
# print('\\\n\\')

# print('''line1
# ...line2
# ...line3''')
# print('''line1
# line2
# line3''')
# print(r'''line1
# line2
# line3''')

# print(r'''hello,\n
# world''')
# print('''hello,\n
# world''')

# print(True)
# print(False)
# print(2<3)
# print(2>3)

# print(2>3 and 6>4)
# print(2>3 or 6>4)
# print(not 2>3)

# age = 10
# if age>=18:
#     print('adult')
# else:
#     print('child')

# a = 123
# print(a)
# a = '123'
# print(a)

# int a = 123 这句好像不符合python语法
# print(a)
# a = '123'
# print(a)

# a = 'ABC'
# b = a
# a = 'XYZ'
# print(b)

# print(10/3)
# print(10//3)
# print(10%3)

# n = 123
# f = 456.789
# s1 = 'Hello,World'
# s2 = 'Hello,\'Adam\''
# s3 = r'Hello,"Bart"'
# s4 = r'''Hello,
# Lisa!'''
# print(n,f,s1,s2,s3,s4)

    # 字符串和编码
# print('包含中文的str')
# print(ord('A'))
# print(ord('中'))
# print(chr(66))
# print(chr(25991))
# print('\u4e2d\u6587')
# print(chr(20013)+chr(25991))

# x = b'ABC'
y = 'ABC'
# print(x,y)
# import types
# print(type(x))
# print(type(y))
# print(y.encode('ascii'))
# print('中文'.encode('utf-8'))
# print('中文'.encode('ascii'))

# print(b'ABC'.decode('ascii'))
# print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))
# print(b'\xe4\xb8\xad\xff'.decode('utf-8',errors='ignore'))

# print(len(y))
# print(len(b'\xe4\xb8\xad\xe6\x96\x87'))
# print(len('中文'.encode('utf-8')))

# print('hello, %s world.' % ('the fucking'))
# print('Hi, %s, you have $%d.' % ('Michael',100000))

# print('%2d-%02d' % (3,1))
# print('%2d-%20d' % (3,1))
# %和d之间的数字表示什么？虽然能通过改变数字感觉出来，但是不确切
# print('%.2f' % 3.1415926)

# print('age:%s. gender:%s' % (25, True))

# print('grouth rate: %d %%' % 7)

# print('hello,{0},成绩提升了{1:.1f}%'.format('小明',17.125))
# s1 = 72
# s2 = 85
# r = (s2-s1)/s1
# print('%s, 成绩提升了%f%%' % ('小明', r))

    # 使用list和tuple
# classmates = ['Michael','Bob','Tracy']
# print(classmates)
# print(len(classmates))
# print(classmates[0])
# print(classmates[-1])
# classmates.append('Adam')
# classmates.insert(1,'Jack')
# print(classmates.pop(1))
# classmates[1]='Sarah'
# print(classmates)

# L = ['apple', 123, True]
# S = ['python','java',['asp','php'],'scheme']
# print(L)
# print(S)
# print(len(S))
# print(S[2][1])

# t = (1)
# t1 = (1,)
# t2 = (1,2,['x','y'])
# t2[2][0] = 'A'
# t2[2][1] = 'B'
# print(t2)

# L = [
#     ['Apple','Google','Microsoft'],
#     ['Java','Python','Ruby','PHP'],
#     ['Adam','Bart','Lisa']
# ]
# print(L[0][0])
# print(L[1][1])
# print(L[2][2])

    # 条件判断
# age = 5
# if age>=18:
#     print('your name is',age)
#     print('adult')
# elif age>=6:
#     print('your name is',age)
#     print('teenager')
# else: 
#     print('your name is',age)
#     print('kid')

# x = []
# if x:
#     print('Ture')
# else:
#     print('False')

# s = input('birth:')
# birth = int(s)
# if birth>=2000:
#     print('00后')
# else:
#     print('00前')

# height = 1.75
# weight = 80.5
# bmi = weight/(height**2)
# if bmi < 18.5:
#     print('过轻')
# elif bmi <= 25:
#     print('正常')
# elif bmi <= 28:
#     print('过重')
# elif bmi <=32:
#     print('肥胖')
# else:
#     print('严重肥胖')

# 参考别人的，找到了自己的问题源于elif条件设置错误
# height = 1.75
# weight = 80.5
# BMI=weight/(height**2)
# # print('Your BMI is {0:.2f} '.format(BMI))
# if BMI < 18.5:
#     print('过轻')
# elif BMI <= 25:
#     print('正常')
# elif  BMI <= 28:
#     print('过重')
# elif BMI <= 32:
#     print('肥胖')
# elif BMI > 32:
#     print('严重肥胖')

    # 循环
# names = ['Michael','Bob','Mike']
# for name in names:
#     print(name)

# sum = 0
# for x in range(101):
#     sum = sum + x
# print(sum)

# sum = 0
# n = 99
# while n > 0:
#     sum = sum + n
#     n = n - 2
# print(sum)

# L = ['Bart', 'Lisa', 'Adam']
# for name in L:
#     print('Hello,' + name + '!')

# n = 1
# while n <= 100:
#     if n >= 10:
#         break
#     print(n)
#     n = n + 1
# print('End')

# n = 0
# while n < 10:
#     n = n + 1
#     if n % 2 == 0:
#         continue
#     print(n)

    # 使用dict和set
# d = {'Michael':98,'Bob':66,"Gloria":95}
# print(d['Gloria'])
# d['Adam'] = 90
# print (d['Adam'])
# print(d.get('Tomas'))
# print('Tomas' in d)
# d.pop('Bob')
# print(d)

# s = set([1,1,2,2,4,4,3,3,5,5])
# s.add('p')
# # print(s)
# y = set(['a','b','c','d','c','b','a'])
# y.remove('d')
# y.add(1)
# y.add('p')
# # print(y)
# print(s & y)
# print(s | y)

# a = ['c','b','a']
# a.sort()
# print(a)

# b = 'abc'
# print(b.replace('a','A'))
# print(b)

# d = {(1, 2, 3)}
# e = {(1, [2, 3])}
# print(d)
# print(e)

# 函数
    # 调用函数
# print(abs(-30))
# print(max(1,424,35))
# print(int('123'))
# print(str(123))
# print(bool(''))
# print(float(8))
# n1 = 225
# n2 = 1000
# print(hex(n1))
# print(hex(n2))

    # 定义函数
# def my_abs(x):
#     if isinstance(x,(int,float)):
#         raise TypeError('bad operand type')
#     if x >= 0:
#         return x
#     else:
#         return -x
# print(my_abs(-10))

# def nop():
#     pass
# age = 18
# if age > 18:
#     pass

# print(abs('a'))
# print(my_abs('a'))

# import math
# def move(x,y,step,angle=0):
#     nx = x + step * math.cos(angle)
#     ny = y + step * math.sin(angle)
#     return nx,ny

# r = move(100,100,60,math.pi/6)
# print(r)

# import math
# def quadratic(a, b, c):
#     s = b**2-4*a*c
#     if a==0 or s<0 :
#         print('无解')
#     else:
#         x1 = (-b + math.sqrt(s))/(2*a)
#         x2 = (-b - math.sqrt(s))/(2*a)
#         return x1,x2
# print(quadratic(1,7,4))

    # 函数的参数
# def power(x, n=2):
#     s = 1
#     while n > 0:
#         n = n - 1
#         s = s * x
#     return s
# print(power(5))

# def add_end(L = None):
    # if L is None:
        # L = []
    # L.append('END')
    # return L
# print(add_end([1,2,3]))
# print(add_end([]))
# print(add_end)

# def calc(*numbers):
#     sum = 0
#     for n in numbers:
#         sum = sum + n*n
#     return sum 
# print(calc(1,2,3))

# nums = [1,2,3]
# print(calc(*nums))

# def person(name,age,**kw):
#     print('name:',name,'age:',age,'other:',kw)
# extra = {'city':'bj','weight':'120'}
# print(person('Bob',40,**extra))

# def person1(name, age, **kw):
#     if 'city' in kw:
#         pass
#     if 'job' in kw:
#         pass
# #     if 'height' in kw:
# #         pass
#     print('name:', name, 'age:', age, 'other:', kw)
# extra = {'city': 'Beijing', 'job': 'Engineer'}
# print(person1('Jack', 24, **extra))

# def person(name, age, *, city, job):
#     # 这种方法似乎不适合做文本的注释，如'city:'
#     print(name,age,city,job)
# print(person('Bob', 24, city='bj',job='writer'))


# def person(name, age, *, city, job):
    # print(name, age, city, job)
# print(person('Jack', 24, city='Beijing', job='Engineer'))
# print(person('Jack', 24))
# 这个函数限制了必须输入定量的参数？——命名关键字参数
# 那这样和直接规定有什么区别呢？根本就不变化了啊
# print(person('Jack', 24, city='Beijing', job='Engineer'))

# 寻求更多种解决方法
# def person(name, age, *, city, job):
#     print(name, age, city, job)
# print(person('Jack', 24, city='Beijing', job=''))

# def person(name, age, *args, city='bj', job):
#     print(name, age, args, city, job)
# print(person('a', 24, job=''))
# 区别在于，如果city给出默认值，输出的时候不输，不会报错，但是name会报错

# def f1(a, b, c=0, *args, **kw):
#     print('a=',a,'b=',b,'c=',c,'args=',args,'kw=',kw)

# def f2(a, b, c=0, *, d, **kw):
#     print('a=',a,'b=',b,'c=',c,'d=',d,'kw=',kw)
# print(f1(1,2))
# print(f1(1,2,3))
# print(f1(1,2,3,'a','b'))
# print(f1(1,2,3,'a','b',x=99))
# print(f2(1,2,d='a',kw='b'))

# args = (1,2,3,4)
# args1 = (1,2,3)
# kw = {'d':88,'x':'#'}
# f1(*args,**kw)
# f2(*args1,**kw)

# def product(x, y):
#     return x * y
# print(product(3, 4))

# 思路1，将输入的函数用list的方式导入，再用for循环相乘，失败
# def product1(m):
#     sum = 0
#     for n in m:
#         sum = sum * n
#     return sum 
# print(product1([1,2,3,4,5]))
# 是不是传入list和引用list的方式不对？
# def product1(*nums):
#     sum = 1
#     for n in nums:
#         sum = sum * n
#     return sum 
# nums = [1,2,3,4]
# print(product1(*nums))
# 绝了，最终原因是我把sum初始值设成0了，乘来乘去什么用

# def calc(*num):
#     sum = 1
#     for n in num:
#         sum = sum * n
#     return sum
# print(calc(1,2,3))

# def product1(x,*nums):
#     sum = 1*x
#     for n in nums:
#         sum = sum * n
#     return sum 

# 测试
# print('product1(5)=', product1(5))
# print('product1(5,6)=', product1(5,6))
# print('product1(5,6,7)=', product1(5,6,7))
# print('product1(5,6,7,9)=', product1(5,6,7,9))
# print('product1(a)=',product1('a'))
# if product1(5) != 5:
#     print('测试失败！')
# elif product1(5,6) != 30:
#     print('测试失败！')
# elif product1(5,6,7) != 210:
#     print('测试失败！')
# elif product1(5,6,7,9) != 1890:
#     print('测试失败！')
# else:
#     try:
#         product1()
#         print('测试失败！')
#     except TypeError:
#         print('测试成功！') 

# def fun(n):
#     if n == 1:
#         return 1
#     return n*fun(n-1)

# print(fun(3))

    # 递归函数
# def fact(n):
#     return fact_iter(n, 1)
# def fact_iter(num, product):
#     if num == 1:
#         return product
#     return fact_iter(num - 1, num * product)

# print(fact(10))

# def move(n, a, b, c):
#     if n == 1:
#         print(a, '-->', c)
        
#     else:
#         move(n-1,a,c,b)
#         move(1,a,b,c)
#         move(n-1,b,a,c)
# print(move(64, 'a', 'b', 'c'))

# 高级特性
    # 切片
# L = ['Michael','Sarah','Tracy','Bob','Jack']
# r = []
# for i in range(3):
#     r.append(L[i])
# print(r)
# print(L[0:3])
# print(L[-2:])

# L = list(range(100))
# print(L)
# print(L[-10:-5])
# print(L[:10:2])
# print(L[::5])
# T = (0,1,2,3,4,5)
# print(T[:3])
# W = 'abcdefg'
# print(W[::2])

# def trim(s):
#     if s == '':
#         return s
#     else:
#         i,j = 0,len(s)-1
#         while i < len(s):
#             if s[i] == ' ':
#                 i += 1
#             else:
#                 break
#         while j > 0:
#             if s[j] == ' ':
#                 j -= 1
#             else:
#                 break
#         return s[i:j+1]

# def trim(s):
#     while s[:1] == ' ':
#         s = s[1:]
#     while s[-1:] == ' ':
#         s = s[:-1]
#     return s

# 测试
# if trim('hello  ') != 'hello':
#     print('测试失败1')
# elif trim('  hello') != 'hello':
#     print('测试失败2')
# elif trim('  hello  ') != 'hello':
#     print('测试失败3')
# elif trim('  hello  world  ') != 'hello  world':
#     print('测试失败4')
# elif trim('') != '':
#     print('测试失败5')
# elif trim('    ') != '':
#     print('测试失败6')
# else:
#     print('测试成功！')
    
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

    # 列表生成器
# print(list(range(1,11)))

# L = []
# for x in range(1,11):
#     L.append(x * x)
# print(L)

# print([x*x for x in range(1,11)])
# print([x*x for x in range(1,11) if x%2 == 0])
# print([m + n for m in 'ABC' for n in 'XYZ'])

# import os
# print([d for d in os.listdir(.)])
# 你忘记加‘’了大傻蛋！！！
# print([d for d in os.listdir('.')])

# d = {'x':'A','y':'B','z':'C'}
# for k, v in d.items():
#     print(k,'=',v)

# print([k+'='+v for k,v in d.items()])

# L = ['Hello','World','IBM','Apple']
# print([s.lower() for s in L])

# L1 = ['Hello','World',18,'Apple',None]
# # L = []
# # for x in L1:
# #     if isinstance(x,str) == True:
# #         L.append(x)
# # L2 = [s.lower() for s in L]

# L2 = [s.lower() for s in L1 if isinstance(s,str)== True]

# # 测试
# print(L2)
# if L2 == ['hello','world','apple'] :
#     print('测试通过')
# else:
#     print('测试失败')

    # 生成器
# L = [x * x for x in range(10)]
# g = (x * x for x in range(10))
# # print(L,g)
# # while True:
# #     print(next(g))
# for n in g:
#     print(n)

def fib(max):
    n,a,b=0,0,1
    while n < max:
        # print (b)
        yield b
        n = n+1
        a,b = b,a+b
    return 'done'

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

def triangless():


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
n = 0
results = []
for t in triangless():
    results.append(t)
    n = n + 1
    if n == 10:
        break
for t in results:
    print(t)

if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过')
else:
    print('测试失败')