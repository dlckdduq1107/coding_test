import math
n = int(input())

a = {}

for i in range(n):
    q = int(input())
    if q in a:
        a[q] += 1
    else:
        a[q] = 0
a = dict(sorted(a.items(), key=lambda x: x[0],reverse=True))

a = dict(sorted(a.items(), key=lambda x: x[1],reverse=True))

w = max(a.values())

a = {v:k for k,v in a.items()}


print(int(a.get(w)))