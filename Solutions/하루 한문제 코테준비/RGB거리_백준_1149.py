n = int(input())

home = []
for i in range(n):
    home.append(list(map(int,input().split(" "))))

result = [[0,0,0]for i in range(n)]
result[0] = home[0]
for i in range(1,n):
    result[i][0] = min(result[i-1][1],result[i-1][2])+home[i][0]
    result[i][1] = min(result[i-1][0],result[i-1][2])+home[i][1]
    result[i][2] = min(result[i-1][0],result[i-1][1])+home[i][2]

print(min(result[-1]))
