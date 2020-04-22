# 寻找n以内的亲密数对。
# 是自己写的失败的版本，经过更改成功了
# def fac(n):
#     for x in range(2,n):
#         y = 0  
#         for i in range(1,x):
#             if x % i == 0:
#                 y += i
#         sumy = 0
#         for k in range(1,y):
#             if y % k == 0:
#                 sumy += k
#         if sumy == x & x < y:
#             print("{}-{}".format(x, y))
# n = int(input('input:'))
# fac(n)

# 网上找的成功版本
# def fac(x):
#     for a in range(2,x): #1肯定不是亲密数，所以不取
#         b = 0
#         for i in range(1,a):
#             if a % i == 0:
#                 b += i
        
#         r = 0
#         for j in range(1,b):
#             if b % j == 0:
#                 r += j
#         if r == a and a < b:
#             print("{}-{}".format(a, b))

# n = int(input())
# fac(n)

# 寻找第n个默尼森数。
# def prime(num):
#     if num == 1:
#         return False
#     for i in range(2,num):
#         if num % i == 0:
#             return False
#     return True

# def monisen(no):
#     count = 0
#     p_num = 1
#     while count < no:
#         p_num += 1
#         if prime(p_num):
#             if prime(2**p_num-1):
#                 count += 1
#                 if count == no:
#                     return 2**p_num-1
# no = int(input('input:'))                        
# print('the {:d} monisen is {:d}'.format(no,monisen(no)))


# 1st
# from math import pow
# h = eval(input('your height:'))
# w = eval(input('your weight:'))
# BMI = w/pow(h,2)
# if BMI>0:
#     if BMI > 28:
#         level = 'fat'
#     elif BMI >=24:
#         level = 'overweight'
#     elif BMI >= 18.5:
#         level = 'normal'
#     else:
#         level = 'too thin'
# else:
#     print('You must input wrong number.')
# print('Your BMI is {:.1f}'.format(BMI))
# print(level)

# 2nd
# for f in range(0,301,20):
#     c = 5/9*(f-32)
#     print('f={},c={:.1f}'.format(f,c))

# 3rd
# n = eval(input('n='))
# while n != 1:
#     if n % 2 == 0:
#         i = n
#         n /= 2
#         print('{:.0f}/2={:.0f}'.format(i,n))
#     else:
#         i = n
#         n = n*3+1
#         print('{:.0f}*3+1={:.0f}'.format(i,n))

# 4th
# 函数不行，函数为啥不行啊？
# 当采用d(f(n))的时候，d()的x值是f(n)的值，计算方式不对
# def f(n):
#     if n == 1 or n == 0:
#         return n
#     else:
#         return n * f(n-1)

# def d(x):
#     if x == 1 or x == 0:
#         return x
#     else:
#         return x + d(x-1)

# n = eval(input('n = '))
# print(d(f(n)))

# 那我就只好用循环了

# n = eval(input('n = '))
# s = term = 1
# for i in range(2,n+1):
#     term *= i
#     print('term=',term)
#     s += term
#     print('s=',s)
# s和term都在累加

# 5th
# x = 0
# for i in {1,2,3,4}:
#     for j in {1,2,3,4}:
#         for k in {1,2,3,4}:
#             if i != j and i != k and j!= k:
#                 n = i*100+j*10+k
#                 print(n)
#                 x += 1
# print(x)

# for i in range(1,5):
#     for j in range(1,5):
#         for k in range(1,5):
#             if i != k and i != j and j != k:
#                 print(i*100+j*10+k)
#                 x += 1
# print(x)

# 6th
flag = 1
for i in range(111,10000,37):
    j = i//10
    