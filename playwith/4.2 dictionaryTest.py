# lst = [1,4,5,6,7,8,9,10,11,12,13,15,18,19,20,21,29,34,54,65]
# def twonums_sum(n,lst):
#     flag = -1
#     lst.sort()
#     for i in range(len(lst)):
#         for j in range(len(lst)):
#             if i != j:
#                 if lst[i] + lst[j] == n:
#                     flag = 1
#                     return i,j
#     if flag == -1:
#         return 'not found'
        
# n = eval(input('Enter a number:'))
# print(twonums_sum(n,lst))


# def twonums_sum(n,lst):
#     d = {}
#     for i in range(len(lst)):
#         d[lst[i]] = i
#     for i in range(len(lst)):
#         if n - lst[i] in d:
#             return i,d[n-lst[i]]
#     return -1

# lst = [1,4,5,6,7,8,9,10,11,12,13,15,18,19,20,21,29,34,54,65]
# n = int(input())
# result = twonums_sum(n,lst)
# if result == -1:
#     print('not found')
# else:
#     print(result)


def twonums_sum(n,lst):
    d = {}
    for i in range(len(lst)):
        d[lst[i]] = i
    for j in range(len(lst)):
        if n-lst[j] in d:
            return j,d[n-lst[j]]
    return -1
    

lst = [1,4,5,6,7,8,9,10,11,12,13,15,18,19,20,21,29,34,54,65]
n = eval(input('n='))
result = twonums_sum(n,lst)
if result == -1:
    print('not found')
else:
    print(result)