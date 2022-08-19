
def union(a,b):
    root_a = find(a)
    root_b = find(b)
    if(root_a>root_b):
        parents[root_a] = root_b
    else:
        parents[root_b] = root_a
        
def find(x):
    if(parents[x]!=x):
        parents[x] = find(parents[x])
    return parents[x]

people, party = map(int, input().split(" "))
parents = [i for i in range(people+1)]
truth = list(map(int,input().split(' ')))
if(len(truth)>1):
    truth = truth[1:]

for i in truth:
    parents[i] = 0

total_party = []
for i in range(party):
    each_party = list(map(int,input().split(" ")))[1:]#
    total_party.append(each_party)
    for j in range(len(each_party)-1):
        union(each_party[j],each_party[j+1])

# print(parents)
# print(total_party)
result = 0
for each in total_party:
    print(each)
    flag = True
    for i in each:
        if(find(i)==0):
            flag = False
            break
    if(flag):
        result += 1
            # print(each)
print(result)
# 예외처리 잘해야 할듯(에지 케이스)
# 유니온 파인드로 풀어도 되고 집합으로 풀어도 된다.