# def foo(num,base):
#     if num >= base:
#       foo(num // base, base)
#     print(num % base, end = ' ')
      
# numA = int(input())
# numB = int(input())
# foo(numA,numB)

# def hanoi(a,b,c,n):
#     if n == 1:
#         print(a,'->',c)
#     else:
#         hanoi(a,c,b,n-1)
#         print(a,'->',c)
#         hanoi(b,a,c,n-1)

# hanoi('a','b','c',3)

def proc(n):
    if n < 0:
        print('-', end = '')
        n = -n
    if n // 10:
        proc(n // 10 )
    print(n % 10, end = '')
     
proc(-345)