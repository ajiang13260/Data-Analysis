# with open('logric.txt','w+') as f:
#     f.write('Believer')

# with open('logric.txt') as f:
#     p1 = f.readlines()
# for i in range(0,len(p1)):
#     p1[i] = str(i+1) +' '+ p1[i]
# with open('logric1.txt','w') as f1:
#     f1.writelines(p1)

s = 'hello everyone, I am here.'
with open('logric.txt','a+') as f:
    f.writelines('\n')
    f.writelines(s)
    f.seek(0)
    cNames = f.readlines()
print(cNames)