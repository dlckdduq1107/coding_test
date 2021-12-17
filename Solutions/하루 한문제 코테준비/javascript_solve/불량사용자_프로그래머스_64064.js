function permutation(arr, selectNum) {
    let result = [];
    if (selectNum === 1) return arr.map((v) => [v]);
  
    arr.forEach((v, idx, arr) => {
      const fixer = v;
      const restArr = arr.filter((_, index) => index !== idx);
      const permuationArr = permutation(restArr, selectNum - 1);
      const combineFixer = permuationArr.map((v) => [fixer, ...v]);
      result.push(...combineFixer);
    });
    return result;
}
function check(origin,patterns){
    let flag = true;
    patterns.forEach((i,idx)=>{
        const p = new RegExp(i);
        const m = p.exec(origin[idx]);
        // console.log("rex",i,origin[idx],m)
        if(!m){
            // console.log("nulllllll")
            flag = false;
        }else{
            if(m[0] !== origin[idx]){
                flag = false;
            }
        }
        
        
    });
    return flag;
}
function solution(user_id, banned_id) {
    var answer = 0;
    const patterns = [];
    for(let i=0; i<banned_id.length; i++){
        let temp = '';
        const pattern = banned_id[i];
        for(let j=0; j<pattern.length; j++){
            const each = pattern[j];
            if(each==='*'){
                temp += '[0-9a-z]';
            }else{
                temp += each;
            }
        }
        patterns.push(temp);
    }
    const userList = permutation(user_id,patterns.length);
    const result = new Set();
    userList.forEach((val,idx)=>{
        const set = new Set(val)
        // console.log(val)
        if(check(Array.from(val),patterns)){
            const temp = val.sort().join('');
            if(!result.has(temp)){
                result.add(temp);
            }
        }
    });
    // console.log(result)
    return result.size;
}
console.log(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],["*rodo", "*rodo", "******"]));