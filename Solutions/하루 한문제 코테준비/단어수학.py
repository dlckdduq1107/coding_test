from collections import defaultdict


n = int(input())
each_alpha = []
for i in range(n):
    each_alpha.append(input())

score = defaultdict(int)
for alphas in each_alpha:
    length = len(alphas)
    for i in range(length, 0,-1):
        score[alphas[length-i]] += 10**i
# print(score)
temp = []
for i in score:
    temp.append([i,score[i]])
temp.sort(key=lambda x:x[1], reverse=True)
# print(temp)
res = {}
for idx,each in enumerate(temp):
    res[each[0]] = 9-idx
# print(res)
answer = 0
for i in each_alpha:
    temp = ''
    for j in i:
        temp  += str(res[j])
    answer += int(temp)
print(answer)