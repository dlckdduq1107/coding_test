def total_per_sec(log,start,end):
    res = 0
    for s,e in log:
        if(s<end and e>=start):
            res +=1
    # print(res,start)
    return res

def solution(lines):
    answer = 0
    logs = []
    for i in lines:
        first,second,third = i.split(" ")
        time = float(third[:-1])*1000
        h,m,s = second.split(":")
        
        hour = int(h)*60*60*1000
        minute = int(m)*60*1000
        sec = float(s)*1000
        end = hour+minute+sec
        start = end-time+1
        logs.append([start,end])
    # print(logs)
    for s,e in logs:
        answer = max(answer, total_per_sec(logs,s,s+1000), total_per_sec(logs,e,e+1000))
        # print(answer)  
    return answer
print(solution([
"2016-09-15 20:59:57.421 0.351s",
"2016-09-15 20:59:58.233 1.181s",
"2016-09-15 20:59:58.299 0.8s",
"2016-09-15 20:59:58.688 1.041s",
"2016-09-15 20:59:59.591 1.412s",
"2016-09-15 21:00:00.464 1.466s",
"2016-09-15 21:00:00.741 1.581s",
"2016-09-15 21:00:00.748 2.31s",
"2016-09-15 21:00:00.966 0.381s",
"2016-09-15 21:00:02.066 2.62s"
]))