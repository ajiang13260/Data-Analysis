from random import randint
x = randint(0,300)
go = 'y'
while go == 'y':
    n = int(input('please input a number between 0-300:'))
    if n == x:
        print('You are right!')
        break
    elif n < x:
        print('Too small, guess again.')
    else:
        print('Too large, guess again.')
    go = input('Input y if you want to continue:')
    print(go)
else:
    print('Goodbye~')
print('x=',x)