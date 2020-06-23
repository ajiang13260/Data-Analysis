import math

def prime(x):
    if x ==  1:
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
            return k, t
        k += 2

n = eval(input())
if n > 4:
    a, b = GC(n)
    print('{} = {} + {}'.format(n, a, b))
elif n == 4:
    print('{} = {} + {}'.format(4,2,2))