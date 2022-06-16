n = int(input())
times = []
for i in range(n):
    times.append(list(map(int,input().split(' '))))
times.sort(key=lambda x:x[0])
times.sort(key=lambda x:x[1])
pivot = 0
result = 0
for start,end in times:
    if(pivot<=start):
        result += 1
        pivot = end
print(result)
