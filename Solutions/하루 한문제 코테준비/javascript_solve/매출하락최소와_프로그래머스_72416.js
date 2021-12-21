const calDp = (tree,sales,dp,idx)=>{
    dp.set(idx,[0,0]);
    const childtren = tree.get(idx);
    childtren.forEach(child => {
        if(!dp.get(child)){
            if(tree.get(child)){
                calDp(tree,sales,dp,child);
            }else{
                dp.set(child,[0,sales[child-1]]);
            }
        }
    });

    let group = false;
    
    const noChoice = childtren.reduce((acc,child)=>{
        if(dp.get(child)[0]<dp.get(child)[1]){
            return acc+dp.get(child)[0];
        }else{
            group = true;
            return acc+dp.get(child)[1];
        }
    },0);
    dp.set(idx,[noChoice,noChoice+sales[idx-1]]);

    if(!group){
        let minNum = Infinity;
        childtren.forEach(child=>{
            const differ = dp.get(child)[1]-dp.get(child)[0];
            minNum = Math.min(differ,minNum);
        });
        dp.set(idx,[dp.get(idx)[0]+minNum,dp.get(idx)[1]]);
    }
}
function solution(sales, links) {
    var answer = 0;
    const dp = new Map();
    const tree = new Map();

    links.forEach(el => {
        const [leader, member] = el;
        if(tree.has(leader)){
            tree.set(leader,[...tree.get(leader),member]);
        }else{
            tree.set(leader,[member]);
        }
    });

    calDp(tree,sales,dp,1);
    // console.log(dp);
    // console.log(dp.get(11233))
    answer = dp.get(1)
    return Math.min(...answer);
}
console.log(solution([14, 17, 15, 18, 19, 14, 13, 16, 28, 17],[[10, 8], [1, 9], [9, 7], [5, 4], [1, 5], [5, 10], [10, 6], [1, 3], [10, 2]]));