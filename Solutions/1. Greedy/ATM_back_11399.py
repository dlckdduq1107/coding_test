n = int(input())
minute_list = list(map(int, input().split()))

time = 0
add_time = 0
for i in range(n):
    min_value = min(minute_list) # 가장 작은 값 찾아서
    time += min_value + add_time # 최종시간 갱신
    add_time += min_value # 이전값을 모두 더한 값 갱신
    minute_list.remove(min_value) # 쓴 요소는 지워줌

print(time)