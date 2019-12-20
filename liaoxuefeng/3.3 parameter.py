    # 函数的参数	
# def power(x, n=2):	
#     s = 1	
#     while n > 0:	
#         n = n - 1	
#         s = s * x	
#     return s	
# print(power(5))	

# def add_end(L = None):	
    # if L is None:	
        # L = []	
    # L.append('END')	
    # return L	
# print(add_end([1,2,3]))	
# print(add_end([]))	
# print(add_end)	

# def calc(*numbers):	
#     sum = 0	
#     for n in numbers:	
#         sum = sum + n*n	
#     return sum 	
# print(calc(1,2,3))	

# nums = [1,2,3]	
# print(calc(*nums))	

# def person(name,age,**kw):	
#     print('name:',name,'age:',age,'other:',kw)	
# extra = {'city':'bj','weight':'120'}	
# print(person('Bob',40,**extra))	

# def person1(name, age, **kw):	
#     if 'city' in kw:	
#         pass	
#     if 'job' in kw:	
#         pass	
# #     if 'height' in kw:	
# #         pass	
#     print('name:', name, 'age:', age, 'other:', kw)	
# extra = {'city': 'Beijing', 'job': 'Engineer'}	
# print(person1('Jack', 24, **extra))	

# def person(name, age, *, city, job):	
#     # 这种方法似乎不适合做文本的注释，如'city:'	
#     print(name,age,city,job)	
# print(person('Bob', 24, city='bj',job='writer'))	


# def person(name, age, *, city, job):	
    # print(name, age, city, job)	
# print(person('Jack', 24, city='Beijing', job='Engineer'))	
# print(person('Jack', 24))	
# 这个函数限制了必须输入定量的参数？——命名关键字参数	
# 那这样和直接规定有什么区别呢？根本就不变化了啊	
# print(person('Jack', 24, city='Beijing', job='Engineer'))	

# 寻求更多种解决方法	
# def person(name, age, *, city, job):	
#     print(name, age, city, job)	
# print(person('Jack', 24, city='Beijing', job=''))	

# def person(name, age, *args, city='bj', job):	
#     print(name, age, args, city, job)	
# print(person('a', 24, job=''))	
# 区别在于，如果city给出默认值，输出的时候不输，不会报错，但是name会报错	

# def f1(a, b, c=0, *args, **kw):	
#     print('a=',a,'b=',b,'c=',c,'args=',args,'kw=',kw)	

# def f2(a, b, c=0, *, d, **kw):	
#     print('a=',a,'b=',b,'c=',c,'d=',d,'kw=',kw)	
# print(f1(1,2))	
# print(f1(1,2,3))	
# print(f1(1,2,3,'a','b'))	
# print(f1(1,2,3,'a','b',x=99))	
# print(f2(1,2,d='a',kw='b'))	

# args = (1,2,3,4)	
# args1 = (1,2,3)	
# kw = {'d':88,'x':'#'}	
# f1(*args,**kw)	
# f2(*args1,**kw)	

# def product(x, y):	
#     return x * y	
# print(product(3, 4))	

# 思路1，将输入的函数用list的方式导入，再用for循环相乘，失败	
# def product1(m):	
#     sum = 0	
#     for n in m:	
#         sum = sum * n	
#     return sum 	
# print(product1([1,2,3,4,5]))	
# 是不是传入list和引用list的方式不对？	
# def product1(*nums):	
#     sum = 1	
#     for n in nums:	
#         sum = sum * n	
#     return sum 	
# nums = [1,2,3,4]	
# print(product1(*nums))	
# 绝了，最终原因是我把sum初始值设成0了，乘来乘去什么用	

# def calc(*num):	
#     sum = 1	
#     for n in num:	
#         sum = sum * n	
#     return sum	
# print(calc(1,2,3))	

# def product1(x,*nums):	
#     sum = 1*x	
#     for n in nums:	
#         sum = sum * n	
#     return sum 	

# 测试	
# print('product1(5)=', product1(5))	
# print('product1(5,6)=', product1(5,6))	
# print('product1(5,6,7)=', product1(5,6,7))	
# print('product1(5,6,7,9)=', product1(5,6,7,9))	
# print('product1(a)=',product1('a'))	
# if product1(5) != 5:	
#     print('测试失败！')	
# elif product1(5,6) != 30:	
#     print('测试失败！')	
# elif product1(5,6,7) != 210:	
#     print('测试失败！')	
# elif product1(5,6,7,9) != 1890:	
#     print('测试失败！')	
# else:	
#     try:	
#         product1()	
#         print('测试失败！')	
#     except TypeError:	
#         print('测试成功！') 	

# def fun(n):	
#     if n == 1:	
#         return 1	
#     return n*fun(n-1)	

# print(fun(3))	