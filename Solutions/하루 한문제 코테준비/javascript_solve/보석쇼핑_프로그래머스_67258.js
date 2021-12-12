function solution(gems) {
    var answer = [];
    let len = new Set(gems).size;
    const dic = new Map();
    dic.set(gems[0],1);
    let [start,end] = [0,0];
    let result = [0,gems.length-1];
    // console.log(dic,result);
    while(start<gems.length && end<gems.length){
        // console.log(dic.length);
        if(dic.size===len){
            if(end-start < result[1]-result[0]) result = [start,end];
            if(dic.get(gems[start])===1){
                dic.delete(gems[start]);
            }
            else dic.set(gems[start],dic.get(gems[start])-1);
            start += 1;
        }else{
            end += 1;
            if(end === gems.length) break;
            if(dic.has(gems[end])) dic.set(gems[end],dic.get(gems[end])+1);
            else dic.set(gems[end],1);
        }
    }
    return [result[0]+1,result[1]+1];
}

console.log(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]));