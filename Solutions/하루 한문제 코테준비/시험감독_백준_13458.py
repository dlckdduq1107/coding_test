import math
n = int(input())
members = list(map(int,input().split(" ")))
master, sub = map(int,input().split(" "))
result = n

for i in members:
    cur = i - master
    if(cur > 0):
        result += math.ceil(cur/sub)
print(result)
