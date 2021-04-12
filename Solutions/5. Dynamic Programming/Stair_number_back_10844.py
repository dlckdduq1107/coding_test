
n = int(input())
f = []
for i in range(n+1):
    f.append([1,1,1,1,1,1,1,1,1,1])

for i in range(1,n):
    for j in range(10):
        if j == 0:
            f[i][j] = f[i-1][j+1]
            continue
        if j == 9:
            f[i][j] = f[i - 1][j - 1]
            continue
        f[i][j] = f[i-1][j-1]+f[i-1][j+1]
for i in f:
    print(i)
print((sum(f[n-1])-f[n-1][0])%1000000000)