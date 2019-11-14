# def foo(num,base):
#     if num >= base:
#       foo(num // base, base)
#     print(num % base, end = ' ')
      
# numA = int(input())
# numB = int(input())
# foo(numA,numB)

# def proc(n):
#     if n < 0:
#         print('-', end = '')
#         n = -n
#     if n // 10:
#         proc(n // 10 )
#     print(n % 10, end = '')
     
# proc(-345)

# print(3 // 10)

# 汉诺塔函数
def move(a, b, c, n):
    if n == 1:
        print(a, '-->', c)
    else:
        move(a, c, b, n-1)
        move(a, b, c, 1)
        move(b, a, c, n-1)
print(move('a', 'b', 'c', 3))