n,m = map(int, input().split(" "))
first = set(list(map(int, input().split(" "))))
second = set(list(map(int, input().split(" "))))

print(n+m-2*len(first&second))

