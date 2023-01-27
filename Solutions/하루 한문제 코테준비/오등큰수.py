from collections import defaultdict
n = int(input())
arr = list(map(int,input().split(" ")))

stack = [0]
result = [-1 for i in range(n)]

count = defaultdict(int)
for i in arr:
    count[i] += 1

for i in range(1,n):
    while stack and count[arr[stack[-1]]] < count[arr[i]]:
        result[stack.pop()] = arr[i]
    stack.append(i)
print(*result)