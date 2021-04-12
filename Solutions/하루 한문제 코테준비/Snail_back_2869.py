import math
u,d,t = map(int,input().split(" "))
print(math.ceil((t-u)/(u-d)) +1)
