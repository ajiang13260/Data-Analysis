# test 1
# poem_EN = 'Life can be good, Life can be sad, Life is mostly cheerful, But sometimes sad.'
# poem_list = poem_EN.split()
# print(poem_list)
# p_dict = {}
# for item in poem_list:
#     if item[-1] in ',./"?':
#         item = item[:-1]
#     # if item not in p_dict:
#     #     p_dict[item] = 1
#     # else:
#     #     p_dict[item] += 1
#     p_dict[item] = p_dict.get(item,0)+1

# print(p_dict)

# test 2
# def fuc(stu_list):
#     d = {}
#     for item in stu_list:
#         r = item.split('_')
#         a,b = r[0], r[1].strip()
#         if a not in d:
#             d[a] = [b]
#         else:
#             d[a] += [b]
#     lst = sorted(d.items(),key=lambda d: len(d[1]),reverse=True)
#     return lst

# if __name__ == "__main__":
#     try:
#         with open('file.txt') as f:
#             stu_list = f.readlines()
#     except FileNotFoundError:
#         print('The file is not found.')
#     else:
#         result = fuc(stu_list)
#         for item in result:
#             print(item[0],'-->',item[1])


# test 3
import random
def func(data):
    cla_no = random.choice(list(data.keys()))
    stu_no = random.randint(1,data[cla_no])
    return '{}{:02}'.format(cla_no,stu_no)
    
if __name__ == '__main__':
    data = {'A001':32,'A002':47,'B001':39,'B002':42}
    result = set()
    while len(result)<10:
        result.add(func(data))
    print(result)