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
import random
with open('random.txt','w+') as f:
    for j in range(500):
        j = random.randint(1,100)
        f.writelines(str(j))
        f.writelines('\n')
    f.seek(0)
    nums = f.readlines()

nums = [num.strip() for num in nums]
print(nums)
# print(type(nums))
setNums = set(nums)
print(setNums)
# lst = [0] * 101
# for num in setNums:


