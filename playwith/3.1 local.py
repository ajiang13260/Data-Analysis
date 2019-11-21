# f1 = open('data.txt')
# f2 = open(r'data.txt', 'w')
# f3 = open('data.txt', 'wb', 0)
# print(f1)
# print(f2)
# print(f3)
# print(f1.close)

# f = open('firstpro.txt', 'w')
# f.write('Hello, world!')
# f.close

# with(open('firstpro.txt', 'w')) as f:
    # f.write('Hello, the end of the fucking world!')

# with(open('firstpro.txt')) as f:
#     p1 = f.read(5)
#     p2 = f.read()
# print(p1, p2)

# with(open('data.txt','r+')) as f:
#     # f.writelines('\n')
#     f.writelines('Winter is coming!')

# with(open('firstpro.txt')) as f:
#     print(f.readlines())

# Filename revcopy.py
# with(open('firstpro.txt')) as f1:
#     cNames = f1.readlines()
# for i in range(0, len(cNames)):
#     cNames[i] = str(i+1)+' '+cNames[i]
# with(open('secpro.txt','w')) as f2:
#     f2.writelines(cNames)

# Filename: companies_b.py
# s = 'Tencent Techonology Company Limited'
# with open('firstpro.txt', 'a+') as f:
#     f.writelines('\n')
#     f.writelines(s)
#     f.seek(0)
#     cNames = f.readlines()
# print(cNames)

# import os
# def countLines(fname):
#     try:
#         with open(fname) as f:
#             data = f.readlines()
#     except FileNotFoundError:
#         print(fname + ' is not exit.')
#     lens = len(data)
#     # print(fname,'has',str(lens),'lines')
#     print(fname.split('\\')[1] ,'has' , str(lens) , 'lines')

# # files = ['lyrics.txt','data.txt','firstpro.txt','secpro.txt']
# # for fname in files:
# #     countLines(fname)

# path = '../Data Analysis'
# for fname in os.listdir(path):
#     if fname.endswith('.txt'):
#         file_path = os.path.join(path, fname)
#         countLines(file_path)
import os
import shutil
if os.path.exists('./output'):
    shutil.rmtree('./output')
os.mkdir('./output')