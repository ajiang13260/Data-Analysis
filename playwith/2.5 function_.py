from math import sqrt
def isprime(x):
    if x == 1:  # 没有考虑到x=1的情况
        return False
    k = int(sqrt(x))  # 没有考虑到k需要时整数
    for j in range(2,k+1):  # 记错range的用法
        if x % j == 0:
            return False  # 对true和false的理解反了
    return True  #如果在这一步骤用if-else做判断，就变成指判断了%2是否为零，判断奇偶性了
for i in range(1,101):
    if isprime(i):
        print(i,end=' ')