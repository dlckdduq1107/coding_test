function solution(genres, plays) {
    var answer = [];
    const total = new Map();
    const count = new Map();

    genres.forEach((e,idx) => {
        if(total.has(e)){
            total.set(e,total.get(e)+plays[idx]);
        }else{
            total.set(e,plays[idx]);
        }

        if(count.has(e)){
            count.set(e,[...count.get(e),[idx,plays[idx]]]);
        }else{
            count.set(e,[[idx,plays[idx]]]);
        }
    });
    const totalArr = Array.from(total);
    totalArr.sort((a,b)=>{
        return b[1]-a[1];
    });
    totalArr.forEach(element => {
        const gen = element[0];
        const temp = count.get(gen);
        temp.sort((a,b)=>a[0]-b[0]);
        temp.sort((a,b)=>b[1]-a[1]);
        for(let i=0; i<2; i++){
            if(i>=temp.length){
                break;
            }
            answer.push(temp[i][0]);
        }
    });
    // for(let i=0;i<2;i++){
    //     const gen = totalArr[i][0];
    //     const temp = count.get(gen);
    //     temp.sort((a,b)=>a[0]-b[0]);
    //     temp.sort((a,b)=>b[1]-a[1]);
    //     temp.forEach(e=>{
    //         answer.push(e[0]);
    //     });
    //     // answer.push()
    // }
    // console.log(totalArr,count)
    return answer;
}

console.log(solution(["classic", "pop", "classic", "classic", "pop"],[500, 600, 150, 800, 2500]))