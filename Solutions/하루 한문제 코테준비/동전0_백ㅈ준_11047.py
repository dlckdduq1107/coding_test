n, target = map(int,input().split(" "))

coin = []
for i in range(n):
    coin.append(int(input()))
coin.sort(reverse=True)

result = 0
for i in coin:
    if(i<=target):
        result += target//i
        target %= i

print(result)

