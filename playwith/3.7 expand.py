# 拓展一：正则表达式


# 拓展二：输入/输出&函数式编程
# x,y = input('input:').split()

# help(map)
# lst = [3,2,5,8,1]
# lst_ = list(map(lambda x: x*2,lst))
# print(lst_)
# lst1 = list(filter(lambda x: x%2==0, lst))
# print(lst1)

# from functools import reduce
# lst2 = reduce(lambda x,y:x+y, lst)
# print(lst2)

# lst3 = input('input :').split()
# lst4 = list(map(eval, lst3))
# print(lst4)
# lst5 = list(map(str,lst))
# print(lst5)

# lst6 = ['abc','def']
# lst7 = list(map(lambda word: word.upper(),lst6))
# lst8 = list(map(str.upper, lst6))
# print(lst7,lst8)

# 拓展三：可变可迭代对象的修改问题
# lst = [1,2,4,3,5] #list可变可迭代
# for i in lst[:]:  #创建一个list的浅拷贝
#     if i % 2 == 0:
#         lst.remove(i)
# print(lst)

# s = 'beautiful' #str是不可变可迭代对象
# for x in s:
#     if x in 'aeiou':
#         y = str(x.upper())
#         s = s.replace(x,y)
# print(s)

# 浅拷贝和深拷贝
# x = [1,2,3,4,5]
# y = x
# y[0] = 9
# print(x[0])  #x[0]的值也发生变化，因为x和y都指向了同一个数据
# # 为了防止原始数据被更改，就需要用到拷贝
# z = x[:]
# print(z) #此时输出为[9, 2, 3, 4, 5]
# z[0] = 1
# print(z,x) #z被更改了，x没有
# x = [1,2,[3,4]]
# y = x[:]
# y[0],y[2][0] = 9,9
# print(y,x)  #y两个数值都被更改，x更深一层被更改
# # 浅拷贝没有拷贝更深一层的数值，此时y用的还是x的原始数值
# # 通过深拷贝来彻底防范对原始数值的影响
# import copy
# z = copy.deepcopy(x)
# z[0],z[2][0] = 8,8
# print(z,x) #此时x完全不受影响

# 动态网页数据爬取小例
# 方法一：找到真正的链接
# 开发者工具——network
# ——手动刷新加载出来的文件就是我们需要找的地址
# ——找到并复制request url，用get获取
# ——还可以获得请求头（usr-agent）
import requests
r = requests.get('https://feed.mix.sina.com.cn/api/roll/get?pageid=153&lid=2509&k=&num=50&page=1&r=0.33569806420694337&callback=jQuery111207737366291666399_1578147387085&_=1578147387087')
print(r.status_code)
# print(r.text)
f = r.text.encode('utf-8').decode('unicode-escape')
print(f)

# 方法二：查询字符串参数query string parameters
# ——将数据放到一个字典中，传给get函数的params参数