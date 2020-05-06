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
# averange = sum(jSores)/len(jSores)
# print(averange)



# Filename:week.py
# week = ['Monday','Tuesday','Wednesday','Thursday','Friday']
# weekend = ['Saturday','Sunday']
# week.extend(weekend)
# for i,j in enumerate(week):
#     print(i+1,j)


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
#                 item = item.replace(c,'') 
#         cleaned_list.append(item)
#     return cleaned_list

# coffee_list = ['32Latte','_Americano30','/34Cappuccino','Mocha35']
# cleaned_list = clean_list(coffee_list)
# # for k,v in enumerate(cleaned_list):
# for k,v in zip(range(1,len(cleaned_list)+1),cleaned_list):
#     print(k,v)


# import os
# with open('Blowing in the wind.txt','r+') as f1:
#     f1.write("Blowin'in the wind")

# with open('Blowing in the wind.txt','r+') as f2:
#     f2.write('Bob Dylan')

# with open('Blowing in the wind.txt','a+') as f3:
#     f3.write('1962 by Warner Bros.lnc.')

# with open('Blowing in the wind.txt','r') as f4:
#     f4.read()


# def insert_line(lines):
#     lines.insert(0,"Blowin'in the wind\n")
#     lines.insert(1,'Bob Dylan\n')
#     lines.append('\n1962 by Warner Bros.lnc.')
#     return ''.join(lines)

# with open('Blowing in the wind.txt','r+') as f:
#     lines = f.readlines()
#     # string = insert_line(lines)
#     lines.insert(0,"Blowin'in the wind\n")
#     lines.insert(1,'Bob Dylan\n')
#     lines.append('\n1962 by Warner Bros.lnc.')
#     # print(string)
#     print(lines)
#     f.seek(0)
#     # f.write(string)
#     f.write(''.join(lines))

# help(''.join)
# with open('test.txt','r+') as f:
#     content = f.readlines()
#     content.append('what?')
#     print(content)
#     f.seek(0)
#     f.write(''.join(content))
# join的作用：write()内只能是字符，不能是数列，所以转换成字符

# 1st
# aString = input('input a string:')
# bString = aString.split(' ')
# # cString = bString[::-1]
# cString = reversed(bString)
# print('the new string is:{}'.format(' '.join(cString)))

# 2nd
# def move_substr(s,flag,n):
#     if int(n) <= len(s):
#         if flag == 1:
#             # s.replace(s[0,int(n)-1],'')
#             # s.append(s[0,int(n)-1])
#             return s[n:] + s[:n]
#         if flag == 2:
#             # s.replace(s[-int(n),-1],'')
#             # s.append(s[-int(n),-1])
#             return s[-n:] + s[:-n]
#         return s
#     else:
#         return -1

# if __name__ == '__main__':
# main模块仅起到未雨绸缪的作用，如果其他函数引用这个.py文件，则main模块中的结果不输出，仅作为数据使用
# s,flag,n = input().split(',')
# result = move_substr(s,int(flag),int(n))
# if result != -1:
#     print(result)
# else:
#     print('the n is too large')

# help(__name__)



def move_substr(s,flag,n):
    if n <= len(s):
        if flag == 1:
            s = s[n:] + s[0:n]
            return s
        if flag == 2:
            s = s[-n:] + s[:-n]
            return s
    else:
        return -1

if __name__ == "__main__":
    s,flag,n = input().split(',')
    result = move_substr(s,int(flag),int(n))
    if result == -1:
        print('the n is too large')
    else:
        print(result)
