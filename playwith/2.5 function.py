# def addMe2Me(x):
#     'apply operation + to argument'
#     return (x + x)

# print(addMe2Me.__doc__)

# Filename:prime.py
# from math import sqrt
# def isprime(x):
#     if x == 1:
#         return False
#     k = int(sqrt(x))
#     for j in range(2,k+1):
#         if x % j == 0:
#             return False
#     return True

# for i in range(2,101):
#     if isprime(i):
#         print(i, end=' ')

# def f(x = True):
#     'whether x is a correct word or not'
#     if x:
#         print('x is a correct word')
#     print('OK')
# print(f())

# def f(x, y):
#     'x and y both correct word or not'
#     if y:
#         print(x, 'and y both correct')
#     print('x is OK')

# print(f(68, False))

# def addMe2Me(x):
#     return x+x

# def self(f, y):
#     return f(y)

# print(self(addMe2Me, 2.3))

r = lambda x:x+x
print(r(5))