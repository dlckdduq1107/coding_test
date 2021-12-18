function solution(stones, k) {
    let answer = 0;
    let [start,end] = [1,2000000000];
    while(start<=end){
        const mid = Math.floor((start+end)/2);
        let blank = 0;
        for(let i=0; i<stones.length; i++){
            const each = stones[i];
            if(each-mid<=0){
                blank += 1;
            }else{
                blank = 0;
            }
            if(blank>=k){
                break
            }
        }
        if(blank<k){
            start = mid+1
        }else{
            answer = mid;
            end = mid-1;
        }

    }

    return answer;
}
console.log(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1],3));