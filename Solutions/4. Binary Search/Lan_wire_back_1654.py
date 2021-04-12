def check(lan_num,length):
    count = 0
    for i in lan_num:
        count += (i//length)
    return count


k,n = map(int,input().split(" "))
lan_num = []
for i in range(k):
    lan_num.append(int(input()))

start, end = 1,max(lan_num)

while start <= end:
    count = 0
    mid = (start+end)//2

    for i in lan_num:
        count += i//mid

    if count >= n:
        start = mid + 1
    else:
        end = mid-1

print(end)


