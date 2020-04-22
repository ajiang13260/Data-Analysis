# try:
#     f = open('data.txt')
#     for line in f:
#         print(line, end='')
# except IOError:
#     print('Can not open the file!')
# finally:
#     f.close()
# 由于f没有被赋值，所以f.close报错

# with open('data.txt') as f:
#     for line in f:
#         print(line, end='')


# if y != 0:
#     print(x/y)
# else:
#     print('division by zero')
while True:
    try:
        x = int(input('first number:'))
        y = int(input('second number:'))
        print(x/y)
    # except ValueError:
    #     print('Please input a digit!')
    # except ZeroDivisionError:
    #     print("The second number can't be zero!")
    # except(ValueError,ZeroDivisionError):
    #     print('Invalid input!')
    # except:
    #     print('Something went wrong!')
    except Exception as err:
        print('Something went wrong!')
        print(err)
    else:
        print('The code is alright.' )
        break
    finally:
        print('Like I care~')