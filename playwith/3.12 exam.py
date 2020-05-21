
# 1st
# 可以运行但无法得到正确答案
# def countchar(string):
#     lst = [chr(ord('a')+i) for i in range(0,26)]
#     result = [0] * 26
#     # k = 0
#     # for a in range(len(string)):
#     #     # k = 0
#     #     for j in range(len(lst)):
#     #         if string[a] == lst[j] or string[a].lower() == lst[j]:
#     #             # k += 1
#     #             # result[j] = k
#     #             result[j] += 1    
#     string = string.lower()
#     for a in range(len(string)):
#         for j in range(len(lst)):
#             if string[a] == lst[j]:
#                 result[j] += 1
#     return result
# if __name__ == "__main__":
#      string = input()
#      print(countchar(string))

# 2nd
def pandigital(nums): 
    lst = []
    for num in nums:
        lnum = list(num)
        intNum = []
        for string in lnum:
            intNum.append(int(string))
        intNum1 = []
        for i in range(len(intNum)):
            intNum1.append(i+1)
        # intNum2 =sorted(intNum)
        if sorted(intNum) == intNum1:
            lst.append(num)
    return lst
    
if __name__ == "__main__":
    lst = pandigital(input().split(','))
    for l in lst:
        print(int(l))

# def pandigital(nums):
#     flag = False
#     for num in nums:
#         num = str(num)
#         all_number_list = [str(i) for i in range(1, len(num) + 1)]
#         all_number_in_num_list = [j for j in all_number_list if j in num]
#         if len(all_number_list) == len(all_number_in_num_list):
#             print(num)
#             flag = True
#     if flag == 0:
#         print('not found')
# if __name__ == "__main__":
#     lst = pandigital(eval(input()))