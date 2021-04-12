import sys
n = int(input())

a = [0]*10001
for i in range(n):
    s = int(sys.stdin.readline())
    a[s] += 1

for i in range(10001):
    if a[i] != 0:
        for j in range(a[i]):
            print(i)