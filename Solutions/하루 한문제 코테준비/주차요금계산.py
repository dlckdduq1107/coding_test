from collections import defaultdict
import math

def sub(start,end):
    atime,amin = start.split(":")
    btime,bmin = end.split(":")
    st,et = int(atime)*60+int(amin),int(btime)*60+int(bmin)
    return et-st
def cal(time, basic_time, basic_cost, per_time, per_cost):
    if(time<=basic_time):
        return basic_cost
    else:
        return basic_cost + math.ceil((time-basic_time)/per_time)*per_cost
    
def solution(fees, records):
    answer = []
    start = defaultdict(str)
    end = defaultdict(str)
    result = defaultdict(int)
    total = defaultdict(int)
    basic_time, basic_cost, per_time, per_cost = fees
    for i in records:
        time, car_num, state = i.split(" ")
        if(state == "IN"):
            start[car_num] = time
            end[car_num] = "NOT"
        else:
            end[car_num] = time
            total[car_num] += sub(start[car_num],time)
    for num in sorted(start.keys()):
        if(end[num] == "NOT"):
            end_time = '23:59'
            total[num] += sub(start[num],end_time)
    for i in sorted(total.keys()):
        t = cal(total[i], basic_time, basic_cost, per_time, per_cost)
        answer.append(t)
    return answer
    
print(solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))