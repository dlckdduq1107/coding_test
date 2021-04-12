n = int(input())
num = list(map(int,input().split(" ")))

for i in range(1,n):# 현재노드의 연속합은 = MAX(이전꺼 +자기꺼, 자기꺼)이다
    num[i] = max(num[i-1]+num[i],num[i])

print(max(num))

