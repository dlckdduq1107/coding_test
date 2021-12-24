T = int(input())
for i in range(T):
    n = int(input())
    sticker = []
    sticker.append(list(map(int,input().split(" "))))
    sticker.append(list(map(int,input().split(" "))))
    result = 0
    if(n==1):
        for i in sticker:
            result = max(result,max(i))
        print(result)
    elif(n==2):
        result = max(sticker[0][0],sticker[1][0],sticker[1][0]+sticker[0][1],sticker[0][0]+sticker[1][1])
        print(result)
    else:
        dp = [[0 for i in range(n)] for j in range(2)]

        dp[0][0] = sticker[0][0]
        dp[1][0] = sticker[1][0]
        dp[0][1] = sticker[1][0]+sticker[0][1]
        dp[1][1] = sticker[0][0]+sticker[1][1]
        for j in range(2,n):
            for i in range(2):
                if(i==0):
                    dp[i][j] = sticker[i][j]+max(dp[i+1][j-1], max(dp[i][j-2],dp[i+1][j-2]) )

                else:
                    dp[i][j] = sticker[i][j]+max(dp[i-1][j-1], max(dp[i-1][j-2],dp[i][j-2]) )
                result = max(result,dp[i][j])
        print(result)