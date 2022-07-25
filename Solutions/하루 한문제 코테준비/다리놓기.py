from itertools import combinations
import math
case = int(input())
for i in range(case):
    n,m = map(int, input().split(" "))
    target = m-n if n>m-n else n
    # print(len(list(combinations(range(m),target))))
    print(int(math.factorial(m)/(math.factorial(m-n)*math.factorial(n))))