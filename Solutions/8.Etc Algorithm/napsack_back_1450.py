n,k = map(int, input().split(" "))
cost_val = [0]+list(map(int,input().split(" ")))

prefix = [0]
sum_value = 0 # 부분합 넣어주기 위한 변수
for i in range(1,n+1): # 입력된 숫자까지 반복
    sum_value += cost_val[i]
    prefix.append(sum_value)


count = 0
for start in range(1,n+1):
    end = n
    while end >= start:
        sum_cost = prefix[end]-prefix[start-1]
        if sum_cost <= k:
            count += 1
            print(start,end)
        end -= 1
print(prefix)
print(count+1)


##실패##
