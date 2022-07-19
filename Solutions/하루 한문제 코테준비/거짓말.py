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

truth = set(truth)
result = 0
for each in total_party:
    result += 1
    for j in each:
        if(j in truth):
            result -=1
            break
print(result)