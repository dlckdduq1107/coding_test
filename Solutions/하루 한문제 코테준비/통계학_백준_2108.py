import math
from collections import Counter

n = int(input())
result = []
for i in range(n):
    result.append(int(input()))

result.sort()
print(round(sum(result)/n))
print(result[n//2])
most = Counter(result).most_common()
if(len(most)>1 and most[0][1]==most[1][1]):
    print(most[1][0])
else:
    print(most[0][0])
# print(Counter(result).most_common()[0][0])
print(result[-1]-result[0])