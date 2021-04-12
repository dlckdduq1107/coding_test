n,m,k = map(int,input().split())

team = 0
while n-2 >= 0 and m-1 >= 0:
    n -= 2
    m -= 1
    team += 1

if n > 0 or m > 0:
    k -= n+m

if k > 0:
    if k % 3 == 0:
        k = k//3
    else:
        k = (k//3)+1
else:
    k = 0

print(team-k)