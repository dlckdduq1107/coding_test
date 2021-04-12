n,c = map(int,input().split(" "))
a = []
for i in range(n):
    a.append(int(input()))

a.sort()

start = 1 # 시작을 1로 해야 안 틀림
end = a[n-1]-a[0]
res = 0
while start <= end:
    mid = (start+end)//2
    count = 1

    q = a[0]
    for i in a:
        if i-q >=mid:
            count += 1
            q = i

    if count >= c:
        res = mid
        start = mid + 1
    else:
        end = mid - 1

print(res)