# 亲密数
# def fac(x):
#     s = 0
#     for i in range(1,x):
#         if x % i == 0:
#             s += i
#     return s

# n = int(input())
# for j in range(1,n):
#     k = fac(j)
#     if fac(k) == j and k>j:
#         print("{}-{}".format(j, k))

# 默尼森数
from math import pow,sqrt
def prime(num):
    if num == 1:
        return False
    for i in range(2,int(sqrt(num))+1):
        if num % i == 0:
            return False
    return True
def monisen(no):
    p = 2
    while no > 0:  
        if prime(p):
            m = pow(2,p)-1
            if prime(m):
                no -= 1
        p += 1
    return int(m)   

print(monisen(int(input())))