import collections

n = int(input())
nums = list(map(int,input().split()))
dic = collections.defaultdict(int)

for i in nums:
    dic[i] += 1
m = int(input())
target = list(map(int,input().split()))

for i in target:
    if(i in dic):
        print(dic[i],end=' ')
    else:
        print(0,end=' ')