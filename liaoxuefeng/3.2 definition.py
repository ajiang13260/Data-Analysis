   # 定义函数	
# def my_abs(x):	
#     if isinstance(x,(int,float)):	
#         raise TypeError('bad operand type')	
#     if x >= 0:	
#         return x	
#     else:	
#         return -x	
# print(my_abs(-10))	

# def nop():	
#     pass	
# age = 18	
# if age > 18:	
#     pass	

# print(abs('a'))	
# print(my_abs('a'))	

# import math	
# def move(x,y,step,angle=0):	
#     nx = x + step * math.cos(angle)	
#     ny = y + step * math.sin(angle)	
#     return nx,ny	

# r = move(100,100,60,math.pi/6)	
# print(r)	

# import math	
# def quadratic(a, b, c):	
#     s = b**2-4*a*c	
#     if a==0 or s<0 :	
#         print('无解')	
#     else:	
#         x1 = (-b + math.sqrt(s))/(2*a)	
#         x2 = (-b - math.sqrt(s))/(2*a)	
#         return x1,x2	
# print(quadratic(1,7,4))	