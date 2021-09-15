def int_to_str(time):
    h = time // 3600
    h = '0' + str(h) if h < 10 else str(h)
    time = time % 3600
    m = time // 60
    m = '0' + str(m) if m < 10 else str(m)
    time = time % 60
    s = '0' + str(time) if time < 10 else str(time)
    return h + ':' + m + ':' + s

def change(time):
    h,m,s = map(int,time.split(":"))
    total = h*3600+m*60+s
    return total

def solution(play_time, adv_time, logs):
    answer = ''
    playCount = [0 for i in range(change(play_time)+1)]
    adCount = change(adv_time)

    for i in logs:
        start,end = i.split("-")
        start = change(start)
        end = change(end)
        playCount[start]+=1
        playCount[end]-=1

    for i in range(1,len(playCount)):
        playCount[i] = playCount[i]+playCount[i-1]

    for i in range(1,len(playCount)):
        playCount[i] = playCount[i]+playCount[i-1]

    # print(playCount)
    maxCount=-1
    result = 0
    for i in range(adCount-1,change(play_time)):
        if(i==adCount-1):
            maxCount = playCount[i]
            result = 0
            continue
        differ = playCount[i]-playCount[i-adCount]
        if(differ>maxCount):
            result = i-adCount+1
            maxCount = differ


    answer = int_to_str(result)
    # print(result)
    return answer

print(solution("02:03:55","00:14:15",["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]))
# print(solution("02:03:55","00:14:15",["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]))
print(solution("99:59:59","25:00:00",["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]))