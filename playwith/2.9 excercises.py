# first question

# weight, height = eval(input())
# BMI = weight / height ** 2
# print('Your BMI is {:.1f}'.format(BMI))
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
# for c in range(0,301,20):
#     f = c * 9 / 5 + 32
#     print('c = ', c, 'f = ', f)

# third question
# x = int(input('please enter a number:'))
# while x != 1:
#     if x % 2 == 0:
#         print(x,'/ 2 =',end=' ')
#         x = x / 2
#         print(x)
#     else:
#         print(x, '* 3 + 1 =', end=' ')
#         x = x * 3 + 1
#         print(x)

# fourth question
# n = eval(input('enter a number as n:'))
# def 

# fifth question
# for i in [1,2,3,4]:
#     for j in [1,2,3,4]:
#         for k in [1,2,3,4]:
#             if i == j or i == k or k == i:
#                 continue
#             else:
#                 s = i * 100 + j * 10 + k
#                 print(s)


# sixth question
# y = eval(input('enter a number:'))
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

# seventh question
s = 0
n = 0
for i in range(1,1001):
    for n in range(1, i-1):
        while i % n == 0:
            s = s + n
    if i == n:
        print(i)

# 