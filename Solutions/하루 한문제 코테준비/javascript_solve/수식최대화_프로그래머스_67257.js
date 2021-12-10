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
  
function solution(expression) {
    var answer = 0;
    let oper = new Set();
    let temp = '';
    let splitEx = [];

    expression.split('').forEach((val)=>{
        if(val==='-' || val==='+'||val==='*'){
            splitEx.push(temp);
            splitEx.push(val);
            oper.add(val);
            temp = '';
            // continue;
        }else{
            temp += val;
        }
        
    });
    splitEx.push(temp);

    let result = 0;
    permutation(Array.from(oper),oper.size).forEach(each=>{
        let tempSplit = [...splitEx];
        // console.log(tempSplit);
        each.forEach(operation=>{
            splitEx.forEach((ex,idx)=>{
                if(ex===operation){
                    let [preIdx,postIdx] = [idx-1,idx+1];
                    while(tempSplit[preIdx]===''){
                        preIdx -= 1;
                    }
                    while(tempSplit[postIdx]===''){
                        postIdx += 1;
                    }
                    tempSplit[idx] = eval(tempSplit[preIdx]+ex+tempSplit[postIdx]).toString();
                    tempSplit[preIdx] = '';
                    tempSplit[postIdx] = '';
                    // console.log(tempSplit)
                }
            });
        });
        result = Math.max(result,Math.abs(parseInt(tempSplit.join(''),10)));
    });
    
    // console.log(splitEx);
    // console.log(result);
    return result;
}
console.log(solution("100-200*300-500+20"));