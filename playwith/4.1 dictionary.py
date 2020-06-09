# pList = [(1,'first','yi'),(2,'second','er'),
#         (3,'third','san'),(4,'forth','si'),(5,'fifth','wu')]
# d = {}
# for item in pList:
#     # 用()不可以，用[]可以，是为什么呢？
#     d[item[0]] = item[2]
# print(d)

# 4.2 测验题1
# system = {'ajiang':'0546'}
# def newusers():
#     userName = input('Enter a name:')
#     if userName in system:
#         userName = input('Enter a name:')
#     else:
#         system[userName] = input('password:')

# def oldusers():
#     userName = input('Enter your username:')
#     passWord = input('Enter your password:')
#     if passWord == system[userName]:  
#         print(userName, 'welcome back ')  
#     else:  
#         print('login incorrect')  
 
# def login():
#     option = '''
#         (N)ew User Login 
#         (O)ld User Login
#         (E)xit
#             """
#      Enter the option
#      '''
#     print(option)
#     order = input()
#     if order == 'N':
#         newusers()
#     elif order == 'O':
#         oldusers()
#     elif order == 'E':
#         quit
#     else:
#         print('Please enter a right letter.')
 
# if __name__ == '__main__':  
#      login()



def newusers():
    userName = input('Enter your username:')

    if userName in system:
        userName = input('The name is used, try again:')
    else:
        passWord = input('Enter your password:')
        print('Account created!')
        system[userName] = passWord
        print('Now try to load.')
        oldusers()
        
 
def oldusers():
    userName = input('Enter your username:')
    passWord = input('Enter your password:')
    if system[userName] == passWord:  
        print(userName, 'welcome back ')  
    else:  
        print('login incorrect')  
 
def login():
    option = '''
            (N)ew User Login 
            (O)ld User Login
            (E)xit
            """
     Enter the option
     '''
    print(option)
    userType = input()
    if userType == 'N':
        newusers()
    elif userType == 'O':
        oldusers()
    elif userType == 'E':
        quit
    else:
        print('Please enter the right letter:')

 
if __name__ == '__main__':  
    system = {}
    login()