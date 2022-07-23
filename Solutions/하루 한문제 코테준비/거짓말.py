people, party = map(int, input().split(" "))
truth = list(map(int,input().split(' ')))
if(len(truth)>1):
    truth = truth[1:]

total_party = []
for i in range(party):
    each_party = list(map(int,input().split(" ")))[1:]
    total_party.append(each_party)
    for j in each_party:
        if(j in truth):
            truth.extend(each_party)
            break

for i in range(party-1,-1,-1):
    for j in total_party[i]:
        if(j in truth):
            truth.extend(total_party[i])
            break

truth = set(truth)
result = 0
for each in total_party:
    result += 1
    for j in each:
        if(j in truth):
            result -=1
            break
print(result)
# 예외처리 잘해야 할듯(에지 케이스)
# 유니온 파인드로 풀어도 되고 집합으로 풀어도 된다.