from itertools import permutations
n = int(input())

num_list = list(map(int,input().split(' ')))

result = 0
for i in permutations(num_list, n):
    temp = 0
    for j in range(len(i)-1):
        temp += abs(i[j]-i[j+1])
    result = max(result,temp)
print(result)