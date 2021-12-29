n = int(input())
box = list(map(int,input().split(" ")))

dp = [0 for i in range(len(box))]
dp[0] = 1
for i in range(1,len(box)):
    temp = -1
    for j in range(i):
        if(box[j]<box[i]):
            temp = max(temp,dp[j])
    if(temp==-1):
        dp[i] = 1
    else:
        dp[i] = temp+1

print(max(dp))
