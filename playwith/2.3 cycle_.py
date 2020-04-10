# Question One
# situation one 字符串切片
# x = input()
# y = ''
# for i in range(len(x)):
#     y = x[i]+y
# print(y)

# situation two 整数循环
# x = eval(input())
# z = 0
# while x > 0:
#     y = x % 10 
#     z = z *10 + y
#     x = x // 10
# print(z)

n = int(input('Enter a number:'))
m = n
s = 0
while n != 0:
    s = s *10 + n % 10
    n // 10
print('reversed({:d}) = {:d}'.format(m,s))

# n = int(input("Enter a number: "))
# m = n
# s = 0
# while n != 0:
#     s = s * 10 + n % 10    # 例如n=123时，s在每一轮循环的变化为3，3*10+2=32，32*10+1=321        
#     n //= 10     # n不断截尾，例如当n=123时，循环从123变化为12，1，0
# print("reversed({:d}) = {:d}".format(m, s))     # 字符串的format()方法中参数输出的位置和格式等由其前面字符串中的{}位置和格式(d表示十进制整数)决定

# Question Two
# x = eval(input())
# y = []
# i = 2
# print(x,'=',end=' ')
# while i < x/2:
#     if x % i == 0:
#         print(i,'*',end=' ')
#         x = x / i
#     i = i + 1

