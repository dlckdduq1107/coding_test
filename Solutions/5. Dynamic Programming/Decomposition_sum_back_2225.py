n,k = map(int,input().split(" "))

d = [[0 for i in range(n+1)] for j in range(k+1)]
if k == 1:
    print(1)
    exit(0)
for i in range(n+1):
    d[1][i] = 1
    d[2][i] = i+1
for i in range(k+1):
    d[i][0] = 1

for i in range(3,k+1):
    for j in range(1,n+1):
        d[i][j] = d[i-1][j] + d[i][j-1]



# print(d)
print(d[k][n]%1000000000)