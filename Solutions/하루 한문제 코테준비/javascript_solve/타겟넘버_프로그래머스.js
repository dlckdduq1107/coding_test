let result = 0;
const dfs = (start,count,value,numbers,target)=>{
    if(count===numbers.length){
        if(value===target){
            result +=1;
        }
    }else{
        dfs(start+1,count+1,value+numbers[start],numbers,target);
        dfs(start+1,count+1,value-numbers[start],numbers,target);
    }
}
function solution(numbers, target) {
    var answer = 0;
    
    dfs(0,0,0,numbers,target)
    
    return result;
}