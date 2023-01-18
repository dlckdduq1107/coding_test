n = int(input())
k = int(input())

start, end = 1, n**2
while start <= end:
    mid = (start+end)//2

    num = 0
    for i in range(1,n+1):
        num += min(n, mid//i)
    # print(num,"NUM")
    if(num>=k):
        res = mid
        end = mid-1
    else:
        start =mid+1
    # print(mid,"MID")
print(res)