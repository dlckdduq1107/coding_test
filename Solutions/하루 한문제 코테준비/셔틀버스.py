def solution(n, t, m, timetable):
    answer = ''
    convert_timetable = []
    for i in timetable:
        h,minute = map(int,i.split(":"))
        h = h*60
        convert_timetable.append(h+minute)
    convert_timetable.sort()
    start = 540
    res = 0
    for i in range(n-1):
        for j in range(m):
            if(convert_timetable and convert_timetable[0]<=start):
                convert_timetable.pop(0)
        start+=t
    if(len(convert_timetable)>=m):
        if(convert_timetable[m-1]>start):
            res = start
        else:
            res = convert_timetable[m-1]-1
    else:
        res = start

    temp_hour = str(int(res/60))
    res_hour = "0"+temp_hour if(len(temp_hour)==1) else temp_hour
    temp_min = str(res%60)
    res_min = "0"+temp_min if(len(temp_min)==1) else temp_min
    return res_hour+":"+res_min
print(solution(2,10,2,["09:10", "09:09", "08:00"]))