def solution(bridge_length, weight, truck_weights):
    answer = 0
    time = 1
    first = truck_weights.pop(0)
    total = first
    bridge = [0 for i in range(bridge_length-1)]+[first]
    while truck_weights or sum(bridge)!= 0:
        time += 1
        pop_each = bridge.pop(0)
        if(pop_each != 0):
            total -= pop_each
        
        if(truck_weights != []):
            if(total+truck_weights[0]<=weight):
                each = truck_weights.pop(0)
                total += each
                bridge.append(each)
            else:
                bridge.append(0)
        
        

        print(bridge,time)


    return time

print(solution(2,10,[7,4,5,6]))
print(solution(100,100,[10,10,10,10,10,10,10,10,10,10]))