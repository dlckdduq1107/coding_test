logs,players = map(int,input().split(" "))

error = []
ban = set()
state = [[i,1,[]] for i in range(players+1)]
for i in range(logs):
    each = list(map(str,input().split(" ")))
    log,player,o = int(each[0]),int(each[1]),each[2]

    if(o == "M"):
        state[player][1] = int(each[3])

    elif(o == "F"):
        if(int(each[3]) != state[player][1]):
            error.append(log)
        state[player][2].append(int(each[3]))

    elif(o == "C"):
        #예외만 처리
        if(int(each[3]) not in state[player][2] or int(each[4]) not in state[player][2]):
            if(int(each[3]) in state[player][2]):
                state[player][2].remove(int(each[3]))
            if(int(each[4]) in state[player][2]):
                state[player][2].remove(int(each[4]))
            error.append(log)
        else:
            state[player][2].remove(int(each[3]))
            state[player][2].remove(int(each[4]))
    elif(o == "A"):
        if(state[player][1] != state[int(each[3])][1]):
            ban.add(player)
            error.append(log)

print(len(error))
for idx,i in enumerate(error):
    if(idx == len(error)-1):
        print(i)
    else:
        print(i,end=" ")
print(len(ban))
for idx,i in enumerate(sorted(ban)):
    if(idx == len(ban)-1):
        print(i)
    else:
        print(i,end=" ")