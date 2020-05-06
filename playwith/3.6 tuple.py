# aList = [2,4,1,6,3]
# aTuple = (2,4,1,6,3)
# print(sorted(aList))
# aList.sort()
# print(aList)
# print(sorted(aTuple))
# print(aTuple.sort())
# print(enumerate(aList))
# print(enumerate(aTuple))
# for i,j in enumerate(aList):
#     print(i,j)
# for i,j in enumerate(aTuple):
#     print(i,j)
# help(enumerate)
# print(reversed(aList))
# aList.reverse()
# print(aList)
# print(reversed(aTuple))
# print(aList.reverse())
# print(sum(aList))
# print(sum(aTuple))
# print(zip(aList))
# aList.zip()
# print(aList)
# print(zip(aTuple))
# aTuple.zip()
# print(aTuple)
# print(format(aList))
# print(format(aTuple))
# print('hello'.isalpha())
# bList = []
# bTuple = []
# for i in aList:
#     bList.append(str(i))
# for j in aTuple:
#     print(j)
#     bTuple.append(str(j))
# # print(''.join(bList))
# print(''.join(bTuple))

# x, y = input('input:').split()
string = 'I love you.'
aList = ['I','Love','you','.']
# print(string.find('y'))
# print(''.join(aList))
# print(string.strip('0'))
# print(string.replace('you','myself'))
# print(string.split(' '))
# print(string.startswith('i'))
# bList = []
# for i in aList:
#     bList.append(i.upper())
#     cList = ''.join(bList)
# print(cList)
dList = aList.copy()
# # print(dList)
# # aList.append('fuck you')
# # print(aList,dList)
# import copy
# eList = copy.deepcopy(aList)
# aList.append('fuck')
# print(aList,dList,eList)
# print(aList.count('you'))
# aList.extend(dList)
# print(aList)
# aList.insert(0,'hello,')
# aList.pop()
aList.sort()
print(aList)