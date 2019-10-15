#!/usr/bin/env python3
#-*- coding:utf-8 -*-

# name = 'Pheobe'
# print('hello,',name)
# name2 = input('enter your name:')
# print('hello',name2)
# print('1024 * 768 =',1024 * 768)

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

d = {(1, 2, 3)}
# e = {(1, [2, 3])}
print(d)
# print(e)