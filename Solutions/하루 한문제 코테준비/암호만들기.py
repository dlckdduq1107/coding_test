from itertools import combinations
L,C = map(int,input().split(" "))
alpha_list = list(map(str, input().split(" ")))

moum = ['a', 'e', 'i', 'o', 'u']
result = set()
res = []
# print(*combinations(alpha_list,L))
for i in combinations(alpha_list, L):
    a = list(i)
    mo_count = 0
    for j in a:
        if(j in moum):
            mo_count += 1
    if(not (mo_count >0 and len(a)-mo_count > 1)):
        continue
    a.sort()
    temp = ''.join(a)
    if(set(temp) & result):
        pass
    else:
        result.add(temp)

b = list(result)
b.sort()
for i in b:
    print(i)
