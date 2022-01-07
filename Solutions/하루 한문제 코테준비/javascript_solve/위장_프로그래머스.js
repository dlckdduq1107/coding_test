function solution(clothes) {
    let answer = 1;
    const count = new Map();
    
    clothes.forEach((v)=>{
        console.log(v[1])
        count.set(v[1], (count.has(v[1])? count.get(v[1])+1 : 2))
    });
    for(const [key,value] of count){
        answer *= value;
    }
    return answer-1;
}