# def trim(s):
#     while s[:1]==' ':
#       s=s[1:]
#     while s[-1:]==' ':
#       s=s[:-1]
#     return s

# 递归解决
def trim(s):
    if s[:1] == ' ':
        s = trim(s[1:])
    if s[-1:] == ' ':
        s = trim(s[:-1])
    return s

# 测试:
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')