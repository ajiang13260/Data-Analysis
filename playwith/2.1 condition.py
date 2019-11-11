
# x = int(input('输入成绩：'))
# score = eval(input("enter the score: "))
# if  0 <= score <= 100:
    # if x >= 90:
    #     print('A')
    # elif x >= 70:
    #     print('B')
    # elif x >= 60:
    #     print('C')
    # elif x >= 0:
    #     print('D')
    # print("The grade of {} is {}.".format(score, grade)) 
# else:
#     print('Invalid score')

# from math import sqrt
# a = int(input('a ='))
# b = int(input('b ='))
# c = int(input('c ='))
# a, b, c = eval(input())
# print(a,c,b)
# d = b**2-4*a*c
# if d >= 0:
#     if d == 0:
#         x = round(-b/(2*a), 1)
#         print('x=', x)
#     else:
#         x1 = round((-b + d**(1/2))/(2*a), 1)
#         x2 = round((-b - d**(1/2))/(2*a), 1)
#         print('x1=', x1,'x2=', x2)
        # print('x1 = {:.1f}, x2 = {:.1f}'.format(x1, x2))
# else:
#     print('no real solution')

x = int(input('x = '))
# if x < 0:
#     y = -1
# elif x == 0:
#     y = 0
# else:
#     y = 1
# print('y =', y)

if x != 0:
    if x < 0:
        y = -1
    else:
        y = 1
else:
    y = 0

# print('y =', y)
print('y = {:}'.format(y))

# help(eval)