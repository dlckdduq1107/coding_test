function solution(s) {
    var answer = [];
    const p = /{[0-9,]+}/g;

    let part = s.match(p);
    let resultPart = [];
    part.forEach(v => {
        // console.log(v)
        resultPart.push(v.slice(1,v.length-1).split(','))
    });
    resultPart.sort((a,b)=>{
        return a.length-b.length;
    })
    let result = new Map();
    resultPart.forEach(v=>{
        v.forEach(each=>{
            result.set(parseInt(each,10),1);
        });
    });
    // console.log(Array.from(result.keys()))

    return Array.from(result.keys());
}
console.log(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))