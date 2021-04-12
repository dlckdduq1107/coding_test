n = int(input())
time_list = []
count = 0

for i in range(n):
    start, end = map(int, input().split())
    time_list.append((start,end))

time_list.sort(key = lambda x:x[0]) # 시작하자마자 끝나는 경우가 있어서 시작시간으로도 정렬해줘야함
time_list.sort(key = lambda x:x[1]) # 끝나는 시간으로 정렬

current = 0 # 피봇역할
for time in time_list:
    s = time[0]
    e = time[1]
    if(current > s): # 시작시간과 피봇 비교
        continue
    count += 1
    current = e
print(count)