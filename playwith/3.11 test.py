# 1st
# Methods 1
# n = eval(input('Enter the number: '))
# num = 0
# for i in range(1,101):
#     j = str(i)
#     m = str(n)
#     if m not in j:
#         if i % n != 0:
#             num += 1
#             if num % 10 == 0:
#                 print(i)
#             else:
#                 print(i,end=",")

# Methods 2
# n = int(input('Enter the number:'))
# count = 0
# new_str = ''
# print('The result string:')
# for i in range(101):
#     s = str(i)
#     if i%n != 0 and s.find(str(n)) == -1:
#         new_str = new_str+s+','
#         count += 1
#         if count % 10 == 0:
#             print(new_str[:-1])
#             new_str = ''
# if len(new_str) > 0:
#     print(new_str[:-1])

# Method 3
# s = input('Enter the number:')
# i = int(s)
# num = list(map(str,filter(lambda x: x%i and s not in str(x),range(101))))
# for i in range(0,len(num),10):
#     print(','.join(num[i:i+10]))

# 2nd
# import random
# with open('random.txt','w+') as f:
#     for j in range(500):
#         j = random.randint(1,100)
#         f.writelines(str(j))
#         f.writelines('\n')
#     f.seek(0)
#     nums = f.readlines()

# nums = [num.strip() for num in nums]

# # 这个地方不太明白，是什么函数形式
# 模仿一下
# lst = [1,2,3,4]
# lst1 = [str(i) for i in lst]

# setNums = set(nums)
# print(setNums)
# lst = [0] * 101
# # print(lst)
# for num in setNums:
#     c = nums.count(num)
#     lst[int(num)] = c
# print(lst)

# for i in range(len(lst)):
#     if lst[i] == max(lst):
#         print(i)

# 3rd
# 出现问题
# UnicodeDecodeError: 'gbk' codec can't decode byte 0x9d in position 610: incomplete multibyte sequence

# 行不通，NameError: name 'reload' is not defined
# import sys
# reload(sys)
# sys.setdefaultencoding('utf8')

# 解决方案：在with open()内加上enconding='UTF-8'
# _*_ coding:utf-8 _*_
# with open('article.txt',encoding='UTF-8') as f:
#     data = f.read()
# words = data.split()
# lst = []
# for word in words:
#     if word[-3:] == '...':
#         # print(word)
#         word = word[:-3]
#         # print(word)
#         lst.append(word)
#     if word[-1] in ',.?!':
#         word = word[:-1]
#         lst.append(word)
#     # 为什么对结果没有影响啊
#     # if word[0] == '@':
#     #     word = word[1:]
#     #     lst.append(word)
# result = sorted(lst,key = len,reverse= True)
# maxlen = len(result[0])
# for word in set(result):
#     n = len(word)
#     if n == maxlen:
#         print(word)    
                

# 帮一位网友测试了一下jieba模块
# import jieba
# text = 'I have a dream.'
# print('/'.join(jieba.lcut(text)))

# import math
# print((0,2)  in zip(range(4), range(2,6)))
# print(list('Life is short, you need Python.').count('is'))
# print('{:10.3f}'.format(math.pi))