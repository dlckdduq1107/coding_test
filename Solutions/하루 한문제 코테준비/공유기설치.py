n,c = map(int,input().split(" "))
home = []
for i in range(n):
    home.append(int(input()))
home.sort()

start = 1
end = home[-1]-home[0]
result = 0

while start <= end:
    mid = (start+end)//2
    count = 1
    pivot = home[0]
    for i in home:
        if i-pivot>=mid:
            count += 1
            pivot = i
    if count >= c:
        result = mid
        start = mid+1
    else:
        end = mid-1
print(result)