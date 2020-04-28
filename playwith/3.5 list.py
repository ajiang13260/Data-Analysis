# Filename:scoring.py
# jSores = [9,9,8.5,10,7,8,8,9,8,10]
# aScore = 9
# jSores.sort()
# print(jSores)
# jSores.pop()
# print(jSores)
# jSores.pop(0)
# print(jSores)
# jSores.append(aScore)
# print(jSores)
# aveScore = sum(jSores)/len(jSores)
# print(aveScore)

# Filename:week.py
# week = ['Monday','Tuesday','Wednesday','Thursday','Friday']
# weekend = ['Saturday','Sunday']
# week.extend(weekend)
# for i, j in enumerate(week):
#     print(i+1, j)

# numList = [3,11,5,8,16,1]
# fruitList = ['apple','banana','pear','lemon','avocado']
# numList.sort(reverse=True)
# print(numList)
# fruitList.sort(key=len)
# print(fruitList)

# def clean_list(lst):
#     cleaned_list = []
#     for item in lst:
#         for c in item:
#             if c.isalpha() != True:
#                 item = item.replace(c, '')
#         cleaned_list.append(item)
#     return cleaned_list

# coffee_list = ['32Latte','_Americano30','/34Cappuccino','Mocha35']
# cleaned_list = clean_list(coffee_list)
# print(cleaned_list)
# for v, k in zip(range(1,len(cleaned_list)+1),cleaned_list):
#     print(v,k)

# -*-coding:utf-8-*-
# '""'
# File processing

# @author:Ajiang

# '""'

# file = open('Blowing in the wind'+'.txt', 'w+')
# file.write('''
#     How many roads must a man walk down
#     Before they call him a man
#     How many seas must a white dove sail
#     Before she sleeps in the sand
#     How many times must the cannon balls fly
#     Before they're forever banned
#     The answer my frend is blowing in the wind
# ''')
# file.close


# def insert_line(lines):
#     lines.insert(0,"Blowin'in the wind\n")
#     lines.insert(1,"Bob Dylan\n")
#     lines.append("1962 by Warner Bros.lnc.")
#     return ''.join(lines)

# with open('Blowing in the wind.txt','r+') as f:
#     lines = f.readlines()
#     string = insert_line(lines)
#     print(string)
#     f.seek(0)
#     f.write(string)


# s = input('input a string:')  #字符串,input()以回车作为输入结束
# list_s = s.split() #字符list
# # # list_num = [int(a) for a in list_s]  #数字list

# # list_d = list_s[::-1]
# list_s.reverse()
# list_sd = ' '.join(list_s)
# # print('the new string is:',list_sd)
# print('the new string is:',list_sd)


# def move_substr(s, flag, n):
#     if n > len(s):
#         return -1
#     else:
#         if flag == 1:
#             return s[n:] + s[0:n]
#         elif flag == 2:
#                 return s[-n:] + s[:-n]

# if __name__ == '__mian__':
#     s, flag, n = input("enter the 'string, flag, n':").split(',')
#     result = move_substr(s, int(flag), int(n))
#     if result != 1:
#         print(result)
#     else:
#         print('the n is not too large')

# numList = [3,11,5,8,16,1]
# fruitList = ['apple','banana','pear','lemon','avocado']
# numList.sort(reverse=True)
# print(numList)

# help(sorted)
# fruitList.sort(key=len)
# print(fruitList)
# print(sorted(fruitList,key=len))
# print(fruitList)