n = int(input())

arr = list(map(int,input().split(" ")))
dic = {}
for idx,i in enumerate(sorted(set(arr))):
    dic[i] = idx

for i in arr:
    print(dic[i],end=' ')
