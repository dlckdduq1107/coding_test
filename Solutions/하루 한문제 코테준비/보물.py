n = int(input())
A = list(map(int,input().split(" ")))
B = list(map(int,input().split(" ")))
B.sort()
A.sort(reverse=True)
result = 0
for i in range(n):
    result += A[i]*B[i]
print(result)