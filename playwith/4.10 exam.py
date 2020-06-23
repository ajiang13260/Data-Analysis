# test 1
# def find_person(dict_users, strU):
#     # print(dict_users.values())
#     if strU in dict_users.keys():
#         return dict_users[strU]
#     else:
#         return 'Not Found'
# if __name__ == "__main__":
#     name = ['xiaoyun','xiaohong','xiaoteng','xiaoyi','xiaoyang']
#     QQ_num = ['88888','5555555','11111','12341234','1212121']
#     dict_users = dict(zip(name,QQ_num))
#     print(dict_users)
#     strU =  input()
#     print(find_person(dict_users, strU))

# test 2 用字典解决以下问题
# import collections
# import copy
# s = "我/是/一个/测试/句子/，/大家/赶快/来/统计/我/吧/，/大家/赶快/来/统计/我/吧/，/大家/赶快/来/统计/我/吧/，/重要/事情/说/三遍/！/"
# s_list = s.split('/') 
# # 为避免迭代时修改迭代对象本身，创建一个列表的深拷贝，也可用浅拷贝s_list_backup = s_list[:]
# s_list_backup = s_list[:]
# [s_list.remove(item) for item in s_list_backup if item in '，。！”“']
# print(collections.Counter(s_list))

def countfeq(s):
    s_list = s.split()
    s_list_backup = s_list[:]
    [s_list.remove(item) for item in s_list_backup if item in ',.']
    d = {}
    for i in s_list:
        d[i] = d.get(i,0)+1
    return d
    
if __name__ == "__main__":
    s = "Not clumsy person in this world, only lazy people, only people can not hold out until the last."
    s_dict = countfeq(s.lower())
    print(s_dict)
    try:
        word = input()
        print(s_dict[word])
    except KeyError:
        print(0)
#    基于s_dict判断word的词频并输出（可能是0次）