
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
    for num in nums:
        lnum = list(num)
        intNum = []
        lst = []
        for string in lnum:
            intNum.append(int(string))
        intNum1 = []
        for i in range(len(nums)-1):
            intNum1.append(i+1)
        # intNum2 =sorted(intNum)
        if sorted(intNum) == intNum1:
            lst.append(num)
    return lst
 
if __name__ == "__main__":
    lst = pandigital(input().split(','))
    print(lst)