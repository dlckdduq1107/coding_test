def dfs(value, count, add, minus, mul, div): # 값, 몇번사용했는지, 더하기 개수,빼기개수,곱하기개수,나누기개수
    global max_num,min_num,n

    if count == n: # 사용했던 개수가 n과 같아지면(모든 부호를 사용했을때)
        max_num = max(max_num, value)
        min_num = min(min_num, value)

    else: # 아직 사용할 부호가 남았을때
        if add > 0:
            dfs(value+num[count], count+1, add-1,minus, mul, div) # 값계산, 개수+1, 더하기개수-1...
        if minus > 0:
            dfs(value - num[count], count + 1, add, minus-1, mul, div)
        if mul > 0:
            dfs(value * num[count ], count + 1, add, minus, mul-1, div)
        if div > 0:
            dfs(int(value/num[count]), count + 1, add, minus, mul, div-1)

n = int(input())

num = list(map(int, input().split(" ")))
operator = list(map(int, input().split(" ")))
max_num = int(-1e9)
min_num = int(1e9)

dfs(num[0], 1, operator[0],operator[1],operator[2],operator[3])

print(max_num)
print(min_num)