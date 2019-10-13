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

print('hello, %s world.' % ('the fucking'))

print('Hi, %s, you have $%d.' % ('Michael',100000))

# print('%2d-%02d' % (3,1))
# print('%2d-%20d' % (3,1))
# %和d之间的数字表示什么？虽然能通过改变数字感觉出来，但是不确切
# print('%.2f' % 3.1415926)

# print('age:%s. gender:%s' % (25, True))

# print('grouth rate: %d %%' % 7)

# print('hello,{0},成绩提升了{1:.1f}%'.format('小明',17.125))
s1 = 72
s2 = 85
r = (s2-s1)/s1
print('%s, 成绩提升了%f%%' % ('小明', r))