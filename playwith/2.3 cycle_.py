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

# n = int(input('Enter a number:'))
# m = n
# s = 0
# while n != 0:
#     s = s *10 + n % 10
#     n //= 10  # 这个地方是忘记写“=”，所以造成了死循环
# print('reversed({:d}) = {:d}'.format(m,s))

# n = int(input("Enter a number: "))
# m = n
# s = 0
# while n != 0:
#     s = s * 10 + n % 10    # 例如n=123时，s在每一轮循环的变化为3，3*10+2=32，32*10+1=321        
#     n //= 10     # n不断截尾，例如当n=123时，循环从123变化为12，1，0
# print("reversed({:d}) = {:d}".format(m, s))     # 字符串的format()方法中参数输出的位置和格式等由其前面字符串中的{}位置和格式(d表示十进制整数)决定

# Question Two
# x = eval(input())
# i = 2
# print(x,'=',end='')
# while i < x:
#     if x % i == 0:
#         print(i,'*',end='')
#         x = x / i
#     else:
#         i += 1
# print(x)        

# n = int(input('n='))
# i = 2
# print(n,'=',end=' ')
# while n != 1:
#     if n % i == 0:
#         n //= i
#         if n == 1:
#             print(i)
#         else:
#             print(i,'*',end=' ')
#     else:
#         i += 1

n = int(input('Enter a number: '))
print(n, '=', end = ' ')
i = 2      # i是第一个测试的n可能的因子
while n != 1:      
    if n % i == 0:    # 把n的所有因子i全部处理完，因为因子可能相同例如8有3个相同的因子2
        n //= i       # 如果n%i等于0表示i是n的因子，因此需要用n//i将此因子去掉
        if n == 1:    # 已判断完，输出最后一个因子，因子后不需要再加*
            print('{:d}'.format(i))
        else:         # 仍然可能有因子，因此输出因子和*
            print('{:d} *'.format(i), end = ' ') 
    else:
        i += 1        # 因子i判断并去掉后接着判断下一个数，例如判断完了2接着判断3