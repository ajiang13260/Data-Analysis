# first question
# -*-coding:utf-8-*-
# weight, height = eval(input())
# BMI = weight / height ** 2
# print('Your BMI is {0:.1f}'.format(BMI))
# if BMI >= 28:
#     print('fat')
# elif BMI >= 24:
#     print('overweight')
# elif BMI >=18.5:
#     print('normal')
# elif BMI > 0:
#     print('too thin')
# else:
#     print('please enter right number')

# second question
# -*-coding:utf-8-*-
# for c in range(0,301,20):
#     f = c * 9 / 5 + 32
#     print('c = ', c, 'f = ', f)
# 华氏度摄氏度理解反了，不愧是你

# for f in range(0, 301, 20):
#     c = 5 / 9 * (f - 32)
#     print('{} f = {:.0f} c'.format(f,c))

# third question
# x = int(input('please enter a number:'))
# while x != 1:
#     if x % 2 == 0:
#         print(x,'/ 2 =',end=' ')
#         x = x // 2
#         print(x)
#     else:
#         print(x, '* 3 + 1 =', end=' ')
#         x = x * 3 + 1
#         print(x)

# -*-coding:utf-8-*-
# n = int(input())
# while n != 1:
#     if n % 2 == 0:
#         print('{} / 2 = {}'.format(n, n//2))
#         n //= 2
#     else:
#         print('{} * 3 + 1 = {}'.format(n, 3 * n + 1))
#         n = 3 * n + 1



# fourth question 这道题不会
# n = eval(input('enter a number as n:'))
# s = term = 1
# for i in range(2, n+1):
#     term *= i
#     s += term
#     # print(s)
# print(s)
    

# fifth question
# for i in range(1,5):
#     for j in range(1,5):
#         for k in range(1,5):
#             if i == j or i == k or k == i:
#                 continue
#             else:
#                 s = i * 100 + j * 10 + k
#                 print(s)


# sixth question
# sum = []
# for s in range(1,11):
#     sum.append(37 * s)
# for i in sum:
#     if i % 37 == 0:
#         i = i % 10 * 100 + i // 10
#         if i % 37 == 0:
#             print(True) 
#         else:
#             print(False) 

# for num in range(100, 1000):
#     if num % 37 == 0:
#         num1 = num % 100 * 10 + num // 100
#         num2 = num % 10 * 100 + num // 10
#         if num1 % 37 != 0 or num2 % 37 != 0:
#             print("It's a false proposition.")
#             break
# else:
#     print("It's a ture proposition.")


# seventh question
# for i in range(1,1001):
#     s = 0
#     for n in range(1, i):
#         if i % n == 0:
#             s = s + n
#     if i == s:
#         print(i)

# for i in range(1, 1001):
#     s = 0 # 注意s初值的位置，根据需求而定
#     # 求非自身的所有因子和
#     for j in range(1,i):
#         if i % j == 0:
#             s += j
#     if s == i:
#         print("\n", i, " ", end=' ')
#         print('Its factors are ', end=' ')
#         for j in range(1, i):
#             if i % j == 0:
#                 print(j, end=' ')

# eight question
# for i in range(4, 2000, 2):
#     s = []

#         for z in range(4, 2000):
#             if z 

import math

def prime(x):
    if x == 1:
        return False
    n = int(math.sqrt(x))
    for i in range(2, n+1):
        if x % i == 0:
            return False
    return True

def GC(n):
    k = 3
    while k < n:
        t = n - k
        if t < k:
            break
        if prime(k) and prime(t):
            return k,t
        k += 2

n = int(input())
if n > 4:
    a,b = GC(n)
    print('{}={}+{}'.format(n, a, b))
elif n == 4:
    print('{}={}+{}'.format(4, 2, 2))