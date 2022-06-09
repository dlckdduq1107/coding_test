from collections import defaultdict
def solution(record):
    answer = []
    mapped_id = defaultdict(str)
    result = ''
    for i in record:
        state = i.split(" ")[0]
        if(state == 'Enter'):
            _, uid, nick = i.split(' ')
            mapped_id[uid] = nick
            # result += '%s님이 들어왔습니다.,' %uid
        elif(state == 'Change'):
            _, uid, nick = i.split(' ')
            mapped_id[uid] = nick
        # else:
        #     _, uid = i.split(" ")
        #     # result += '%s님이 나갔습니다.,' %uid
    for i in record:
        state = i.split(" ")
        if(state[0]=='Enter'):
            answer.append('%s님이 들어왔습니다.'%mapped_id[state[1]])
        elif(state[0]=='Leave'):
            answer.append('%s님이 나갔습니다.'%mapped_id[state[1]])
    # print(mapped_id)
    # for i in mapped_id:
        # print(i)
        # result = result.replace(i,mapped_id[i])
    # print(result)
    return answer
print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))