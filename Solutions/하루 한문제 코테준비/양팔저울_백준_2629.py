def cal(num,weight):
    if(num>n):
        return
    if(dp[num][weight]==1):
        return

    dp[num][weight] = 1
    cal(num+1,weight)
    cal(num+1,weight+chu[num-1])
    cal(num+1,abs(weight-chu[num-1]))

n = int(input())
chu = list(map(int,input().split()))

dp = [[0 for i in range(500*n+1)] for j in range(n+1)]
cal(0,0)

c = int(input())
for i in list(map(int,input().split())):
    if(i>30*500):
        print('N',end=' ')
        continue
    if(dp[n][i]==1):
        print('Y',end=' ')
    else:
        print('N',end=' ')

