function solution(participant, completion) {
    var answer = '';
    const part = {};
    participant.forEach(e=>{
        if(e in part){
            part[e] += 1;
        }else{
            part[e] = 1;
        }
    });
    completion.forEach(element => {
        part[element] -= 1;
    });
    for(let i in part){
        if(part[i] !== 0){
            answer = i;
        }
    }

    return answer;
}

console.log(solution(["leo", "kiki", "eden"],["eden", "kiki"]));