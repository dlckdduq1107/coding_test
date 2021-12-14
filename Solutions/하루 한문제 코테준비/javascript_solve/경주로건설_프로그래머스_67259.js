const bfs = (sx,sy,n,cpyBoard,cost)=>{
    const [dx,dy] = [[0,0,1,-1],[1,-1,0,0]];
    const q = [];
    q.push([sx,sy,0,0]);
    let newValue;
    while(q.length !== 0){
        const [x,y,direction,value] = q.shift();
        for(let i=0; i<4; i++){
            const [nx,ny] = [x+dx[i],y+dy[i]];
            // console.log(nx,ny,cost)
            if(0<=nx && nx<n && 0<=ny&& ny<n){
                if(cpyBoard[nx][ny]===0){
                    if(x===0 && y===0) newValue = value+100;
                    else{
                        if(direction===i) newValue = value+100;
                        else newValue = value+600;
                    }
                    if(cost[nx][ny]>=newValue){
                        cost[nx][ny] = newValue;
                        q.push([nx,ny,i,newValue]);
                    }
                }
                    
            }

        }
                
    }
    return cost[n-1][n-1];
}
function solution(board) {
    var cost;
    var answer = 0;
    var n = board.length;
    var cpyBoard = [...board];
    cost = Array.from(Array(board.length), ()=>Array(board.length).fill(1e9));
    cost[0][0] = 0;
    const result = bfs(0,0,n,cpyBoard,cost);

    return result;
}
console.log(solution([[0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 1], [0, 0, 1, 0, 0, 0, 1, 0], [0, 1, 0, 0, 0, 1, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0]]));