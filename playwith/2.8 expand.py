# import random
# print(random.choice(['霸道总裁风','高贵冷艳风','扎心了老铁风','人来疯']))


# Filename:exception1.py
# num1 = int(input('Enter the first number:'))
# num2 = int(input('Enter the second number:'))
# print(num1 / num2)

# Filename:exception2.py
# while True:
#     try:
#         num1 = int(input('Enter the first number:'))
#         num2 = int(input('Enter the second number:'))
#         print(num1 / num2)
        # break
    # except ValueError: #as err:
    #     print('please input a digit!')
    #     # print(err)
    # except ZeroDivisionError:
    #     print('The second number can not be zero!')
    # except(ValueError, ZeroDivisionError):
    #     print('Invalid input!')
    # except:
    #     print('Something went wrong!')
    # except Exception as err:
    #     print('Something went wrong!')
    #     print(err)
    #     break
    # else:
    #     print('Everything is OK!')
        # break

# Filename:exception11.py
# aList = [1,2,3,4,5]
# i = 0
# while True:
#     try:
#         print(aList[i])
#     except IndexError:
#         print('index error')
#         break
#     else:
#         i += 1

# Filename:exception12.py
# def finallyTest():
#     try:
#         x = int(input('Enter the first number:'))
#         y = int(input('Enter the second number:'))
#         print(x / y)
#         return 1
#     except Exception as err:
#         print(err)
#         return 0
#     finally:
#         print('It is a finally clause.')
# result = finallyTest()
# print(result)

# Filename:exception13.py
# try:
#     f = open('data.txt')
#     for line in f:
#         print(line, end=' ')
# except IOError:
#     print('Cannot open the file!')
# finally:
#     f.close()

# Filename:exception14.py
# try:
#     with open('data.txt') as f:
#         for line in f:
#             print(line, end=' ')
# except IOError:
#     print('Cannot open the file!')
# finally:
#     f.close()



while True:
    try:
        count = int(input('Enter count:'))
        price = float(input('Enter price for each one:'))
        pay = count * price
        print('The price is', pay)
        break
    except Exception as err:
        print('Error, please enter numeric one.')
    