n = int(input())
length = list(map(int,input().split(' ')))
cost = list(map(int,input().split(' ')))

result=1
pivot = int(1e9)

for i in range(n-1):
    if(i==0):
        pivot = cost[i]
        result = pivot*length[i]
    else:
        pivot = min(pivot,cost[i])
        result += pivot*length[i]

print(result)