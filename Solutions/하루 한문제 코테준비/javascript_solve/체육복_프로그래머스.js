function solution(n, lost, reserve) {
    var answer = 0;
    lost.sort()
    reserve.sort()
    let l = lost.filter((v)=>{
        return !reserve.includes(v)
    })
    let r = reserve.filter((v)=>{
       return !lost.includes(v);
    });
    const a = l.filter((v)=>{
        let extra = r.find((rr)=>{
            return Math.abs(v-rr) <=1;
        });
        if(!extra) return true;
        r = r.filter((q)=>q!==extra)
    })
    console.log(a)
    answer = n-a.length
    return answer;
}