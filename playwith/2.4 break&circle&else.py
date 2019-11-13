# i = 1
# while i % 3 != 0: 
#     print(i, end = ' ')
#     if i >= 10:
#         break
#     i += 1

# 输出2-100之间的素数
# from math import sqrt
# j = 2
# # print(2, 3, end=' ')
# while j <= 100:
#     i = 2
#     k = sqrt(j)
#     while i <= k:
#         if j % i == 0: break
#         i += 1
#         if i > k:
#             print(j, end=' ')
#     j += 1

# from math import sqrt
# for j in range(2,101):
#     flag = 1
#     k = int(sqrt(j))
#     for i in range(2,k+1):
#         if j % i == 0: 
#             flag = 0
#             break
#     if flag:
#         print(j, end=' ')

# for i in range(1, 10, 2):
#     if i % 5 == 0:
#        print("Bingo!")
#        break
# else:
#     print(i)

print((3 is 4) == 0)
print('abc' < 'ABC')
print('''hello 
world''')