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