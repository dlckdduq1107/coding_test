n,m = map(int,input().split(" "))
first = set()
second = set()

for i in range(n):
    first.add(input())

for i in range(m):
    second.add(input())

result = list(first & second)
result.sort()
print(len(result))
for i in result:
    print(i)