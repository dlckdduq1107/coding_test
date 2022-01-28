n = int(input())

result = []
result.append(1)
if(n>1):
    result.append(2)
    for i in range(2,n):
        result.append((result[i-1]+result[i-2])%15746)
print(result[n-1])

