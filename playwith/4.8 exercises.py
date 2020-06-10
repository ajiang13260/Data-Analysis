poem_EN = 'Life can be good, Life can be sad, Life is mostly cheerful, But sometimes sad.'
poem_list = poem_EN.split()
p_dict = {}
for item in poem_list:
    if item[-1] in ',./"?':
        item = item[:-1]
    if item not in p_dict:
        p_dict[item] = 1
    else:
        p_dict[item] += 1
print(p_dict)