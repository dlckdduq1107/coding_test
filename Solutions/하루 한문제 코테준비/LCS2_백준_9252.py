str1 = input()
str2 = input()

dp = [[0 for i in range(len(str1)+1)] for j in range(len(str2)+1)]

for i in range(1,len(str2)+1):
    for j in range(1,len(str1)+1):
        if(str2[i-1]==str1[j-1]):
            dp[i][j] = dp[i-1][j-1]+1
        else:
            dp[i][j] = max(dp[i-1][j],dp[i][j-1])


print(dp[-1][-1])
if(dp[-1][-1]==0):
    pass
else:
    result = []
    x,y = len(str2),len(str1)
    while(x>0 and y>0):
        if(dp[x][y]==dp[x-1][y]):
            x-=1
        elif(dp[x][y]==dp[x][y-1]):
            y-=1
        else:
            result.append(str1[y-1])
            x,y = x-1,y-1
        # if(str1[x-1]==str2[y-1]):
        #     result.append(str1[x-1])
        #     x,y = x-1,y-1
        # else:
        #     if(dp[x-1][y]==dp[x][y]):
        #         x,y = x-1,y
        #     else:
        #         x,y = x,y-1
    result.reverse()
    print(''.join(result))