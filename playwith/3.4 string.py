# a = 'Hello, World!'
# # b = a[0:7] + 'Python!'
# b = a.replace('World','Python')
# print(b)
# count = 0
# for ch in b[:]:
#     if ch in ',.?!':
#         count += 1
# print(count)
# print('There are %d punctuation marks.'%(count))
# print('There are {:d} punctuation marks.'.format(count))

# age, height = 21, 1.758
# print('Age:{0:<5d}, Height:{1:5.2f}'.format(age, height))

# cCode = ['AXP','BA','CAT','CSCO','CVX']
# cPrice = ['78.51','184.76','96.39','33.71','106.09']
# for i in range(5):
#     print('{:<8d}{:8s}{:8s}'.format(i, cCode[i], cPrice[i]))

# print('I get {:3d} {{}}!'.format(32))

# sStr = 'acdhdca'
# if (sStr == ''.join(reversed(sStr))):
#     print('Yes')
# else:
#     print('No')

# import operator
# sStr = 'acdhdca'
# if operator.eq(sStr, ''.join(reversed(sStr))) == 0:
#     print('Yes')
# else:
#     print('No')

# sStr = 'acdhdca'
# if sStr == sStr[::-1]:
#     print('Yes')
# else:
#     print('No')   

# print(dir(str))
# dir(str)

# song = 'Blowing in the wind~'
# print(song.find('the'))
# print(song.find('the',8,12))
# print(song.lower())
# print(song.split(' '))
# print(song.replace('~',''))
# aList = ['Hello','World']
# print(','.join(aList))
# y = '你好'
# z = y.encode('utf-8')
# print(z)
# t = z.decode()
# print(t)
# x = b'\xe6\x89\x8e\xe5\xbf\x83\xe4\xba\x86\xef\xbc\x8c\xe8\x80\x81\xe9\x93\x81'
# y = x.decode()
# print(y)

# Filename:totitle.py
# aStr = 'What do you think of saying "No pain, No gain"?'
# # lindex = aStr.index('\"', 0, len(aStr))
# # rlindex = aStr.rindex('\"', 0, len(aStr))
# # tempStr = aStr[lindex+1:rlindex]
# tempStr = aStr.split('\"')[1]
# if tempStr.istitle():
#     print('It is title format.')
# else:
#     print('It is not title format.')
# print(tempStr.title())

# string = 'My moral standing is: 0.98765'
# ans = string.split(' ')[4]
# print(float(ans))
# print('my'.split())

# f = ['HELLO', 'PH', 'Hi', 'read', 'tmp123', 'Our', 'vmr']
# for a in f:
#     a_temp = a.lower()
#     for ch in a_temp:
#         print(ch)
#         if ch in 'aeiou' or ch in '0123456789':
#             break
#     else:
#         print(a)

# i = '5' * 2000
# print(int(i)%84) 

# aStr = b'\xe6\x89\x8e\xe5\xbf\x83\xe4\xba\x86\xef\xbc\x8c\xe8\x80\x81\xe9\x93\x81'
# bStr = aStr.decode()
# print(bStr)

# test 1
# string = 'My moral standing  is: 0.98765'
# # help(string.find)
# a = string.find('0')
# b = string[a:]
# print(float(b))

# c = string.split(' ')
# d = float(c[5])
# print(d)

# e = string.split(':')
# f = e[1]
# print(float(f))

# test 2
# x =  ['HELLO', 'PH', 'Hi', 'read', 'tmp123', 'Our', 'vmr']
# for i in x:
#     i_temp = i.lower()
#     for j in i_temp:
#         if j in 'aeiou' or j in '0123456789':
#             break
#     else:
#         print(i)

# test 3
i = 1
s = 0
j = 1
while j <= 2000:
    s = s + i*5
    i = i*10
    j += 1
print(s%84)

print(int('5'*2000)%84)