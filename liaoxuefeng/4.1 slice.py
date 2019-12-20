# 高级特性	
    # 切片	
# L = ['Michael','Sarah','Tracy','Bob','Jack']	
# r = []	
# for i in range(3):	
#     r.append(L[i])	
# print(r)	
# print(L[0:3])	
# print(L[-2:])	

# L = list(range(100))	
# print(L)	
# print(L[-10:-5])	
# print(L[:10:2])	
# print(L[::5])	
# T = (0,1,2,3,4,5)	
# print(T[:3])	
# W = 'abcdefg'	
# print(W[::2])	

# def trim(s):	
#     if s == '':	
#         return s	
#     else:	
#         i,j = 0,len(s)-1	
#         while i < len(s):	
#             if s[i] == ' ':	
#                 i += 1	
#             else:	
#                 break	
#         while j > 0:	
#             if s[j] == ' ':	
#                 j -= 1	
#             else:	
#                 break	
#         return s[i:j+1]	

# def trim(s):	
#     while s[:1] == ' ':	
#         s = s[1:]	
#     while s[-1:] == ' ':	
#         s = s[:-1]	
#     return s	

# 测试	
# if trim('hello  ') != 'hello':	
#     print('测试失败1')	
# elif trim('  hello') != 'hello':	
#     print('测试失败2')	
# elif trim('  hello  ') != 'hello':	
#     print('测试失败3')	
# elif trim('  hello  world  ') != 'hello  world':	
#     print('测试失败4')	
# elif trim('') != '':	
#     print('测试失败5')	
# elif trim('    ') != '':	
#     print('测试失败6')	
# else:	
#     print('测试成功！')	