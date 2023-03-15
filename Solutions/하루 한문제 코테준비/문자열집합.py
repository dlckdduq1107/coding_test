n,m = map(int,input().split(" "))

S = set()
# scanS = set()


for i in range(n):
    S.add(input())

result = 0
for i in range(m):
    each = input()
    if(each in S):
        result += 1
    

print(result)