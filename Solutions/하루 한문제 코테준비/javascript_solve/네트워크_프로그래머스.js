const dfs = (start,visited,graph)=>{
    visited[start] = true;
    const nextList = graph[start];
    
    nextList.forEach((v)=>{
        if(!visited[v]){
            dfs(v,visited,graph);
        }
    });
}
function solution(n, computers) {
    var answer = 0;
    const graph =Array.from(new Array(n+1), ()=>new Array().fill([]))
        console.log(graph)

    computers.forEach((v,idx)=>{
        v.forEach((e,i)=>{
            if(idx!==i && e===1){
                graph[idx+1].push(i+1)
            }
        })
    });
    const visited = new Array(n+1).fill(false);
    console.log(visited)
    for(let i=1; i<n+1; i++){
        if(!visited[i]){
            dfs(i,visited,graph);
            answer += 1;
        }
        
    }
    
    console.log(graph)
    return answer;
}