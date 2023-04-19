n = int(input())

res = 1
for i in range(2,n+1,):
    if(i*i<n):
        res += 1
    

print(res)