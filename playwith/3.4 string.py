# a = 'Hello, World!'
# b = a[0:7] + 'Python!'
# print(b)
# count = 0
# for ch in b[:]:
#     if ch in ',.?!':
#         count += 1
# print(count)

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
x = b'\xe6\x89\x8e\xe5\xbf\x83\xe4\xba\x86\xef\xbc\x8c\xe8\x80\x81\xe9\x93\x81'
y = x.decode()
print(y)