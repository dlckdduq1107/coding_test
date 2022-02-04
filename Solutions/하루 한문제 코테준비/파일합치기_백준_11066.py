

n = int(input())

for i in range(n):
    num = int(input())
    files = list(map(int,input().split()))
    sums = [0 for j in range(num+1)]
    for j in range(1,num+1):
        sums[j] = sums[j-1]+files[j-1]

    # print(sums)
    dp = [[0 for w in range(num+1)] for q in range(num+1)]
    for j in range(2,num+1):
        for q in range(1,num+2-j):
            dp[q][q+j-1] = min([dp[q][q+p]+dp[q+p+1][q+j-1] for p in range(j-1)]) + (sums[q+j-1]-sums[q-1])

    print(dp[1][num])


