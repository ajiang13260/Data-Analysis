
# Question One
# score = eval(input('Enter your score:'))
# if score >= 0 and score <= 100:
#     if score >=90:
#         grade = 'A'
#     elif score >= 70:
#         grade = 'B'
#     elif score >= 60:
#         grade = 'C'
#     else:
#         grade = 'D'
#     print('The grade of {} is {}'.format(score, grade))
# else:
#     grade = 'Invalid score'
#     print(grade)

# Question Two
# from math import sqrt
# a, b, c = eval(input())
# t = b**2 - 4*a*c
# if t >= 0:
#     if t > 0:
#         x1 = (-b + sqrt(t)) / 2 / a
#         x2 = (-b - sqrt(t)) / 2 / a 
#         print('x1=',x1,' x2=',x2)
#     else:
#         x =-b /2 /a
#         print('x={}'.format(x))
# else:
#     print('no real solution')

# Question Three
x = eval(input())
if x < 0:
    sgn = -1
elif x == 0:
    sgn = 0
else:
    sgn = 1

if x >= 0:
    if x == 0:
        sgn = 0
    else:
        sgn = -1
else:
    x = 1
    