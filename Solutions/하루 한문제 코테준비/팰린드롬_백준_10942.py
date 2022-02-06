import sys
input = sys.stdin.readline
n = int(input())
nums = list(map(int,input().split()))

dp = [[0 for i in range(n+1)] for j in range(n+1)]
for i in range(n):
    for start in range(1,n+1-i):
        end = start+i

        if(start==end):
            dp[start][end] = 1
        elif(nums[start-1]==nums[end-1]):
            if(start+1==end):
                dp[start][end] = 1
            elif(dp[start+1][end-1]):
                dp[start][end] = 1


case = int(input())
# for i in dp:
#     print(i)
for i in range(case):
    s,e = map(int,input().split())
    print(dp[s][e])