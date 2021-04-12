
n = int(input())
cost_list = list(map(int,input().split(" ")))
cost_list.insert(0,0)
res_list = [0]*(n+1)

for i in range(1,n+1):
    for j in range(i+1):
        res_list[i] = max(res_list[i],res_list[i-j]+cost_list[j])#D[n] = D[n-1]+i(1<=i<=n)중에서 제일 큰거

print(res_list[n])

