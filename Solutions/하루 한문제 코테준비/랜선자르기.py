

k,n = map(int, input().split(' '))

lines = []
for i in range(k):
    lines.append(int(input()))

start,end = 1, max(lines)
while start<=end:
    count = 0
    mid = (start+end)//2

    for each in lines:
        count += each//mid

    if count<n:
        end = mid-1
    else:
        start = mid+1
print(end)
