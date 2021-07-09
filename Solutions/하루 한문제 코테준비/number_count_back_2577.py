a = 1
for i in range(3):
    a *= int(input())

a_list = list(map(int,list(str(a))))


a_dic = {}
for i in a_list:
    if i not in a_dic:
        a_dic[i] = 1
    else:
        a_dic[i] += 1

for i in range(10):
    if i in a_dic:
        print(a_dic[i])
    else:
        print(0)


