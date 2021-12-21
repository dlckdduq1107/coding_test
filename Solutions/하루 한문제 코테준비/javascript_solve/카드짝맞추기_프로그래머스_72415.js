let answer = Infinity;

const permutation = (arr, selectNum) => {
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
const isMovable = (x,y)=>{
    return (-1<x&&x<4&&-1<y&&y<4)? true : false;
}
const ctrlMove = (x,y,directX,directY,board)=>{
    let [nx,ny] = [x,y];
    while(true){
        const [nnx,nny] = [nx+directX,ny+directY];
        if(!isMovable(nnx,nny)) return [nx,ny];
        if(board[nnx][nny]) return [nnx,nny];
        [nx,ny] = [nnx,nny];
    }
}
const bfs = (sx,sy,ex,ey,board)=>{
    if(sx===ex && sy===ey) return [sx,sy,1];
    const dx = [0,0,1,-1];
    const dy = [1,-1,0,0];

    const q = [];

    const distance = Array.from(new Array(4),()=>new Array(4).fill(0));
    const visited = Array.from(new Array(4),()=>new Array(4).fill(false));

    q.push([sx,sy]);
    visited[sx][sy] = true;

    while(q.length){
        const [x,y] = q.shift();

        for(let i=0; i<4; i++){
            let [nx,ny] = [x+dx[i], y+dy[i]];
            if(isMovable(nx,ny)){
                if(!visited[nx][ny]){
                    visited[nx][ny] = true;
                    distance[nx][ny] = distance[x][y] +1;
                    if(nx===ex&&ny===ey){
                        return [nx,ny,distance[nx][ny]+1];
                    }
                    q.push([nx,ny]);

                }
            }

            [nx,ny] = ctrlMove(x,y,dx[i],dy[i],board);
            if(!visited[nx][ny]){
                visited[nx][ny] = true;
                distance[nx][ny] = distance[x][y]+1;

                if(nx===ex&&ny===ey){
                    return [nx,ny,distance[nx][ny]+1];
                }
                q.push([nx,ny]);
            }
        }

    }
    return [sx,sy,Infinity];
}
const remove = (cardNum,board,cardLocation)=>{
    cardLocation.get(cardNum).forEach(v=>{
        board[v[0]][v[1]] = 0;
    });
}
const restore = (cardNum, board, cardLocation)=>{
    cardLocation.get(cardNum).forEach(v=>{
        board[v[0]][v[1]] = cardNum;
    });
}

const backTracking = (sx,sy,iterIdx,outerPermutationNum,count,board,cardLocation,permutation)=>{
    if(iterIdx===[...cardLocation.keys()].length){
        answer = Math.min(answer,count);
        return;
    }

    const cardNum = permutation[outerPermutationNum][iterIdx];

    const [fx,fy] = [cardLocation.get(cardNum)[0][0], cardLocation.get(cardNum)[0][1]];
    const [lx,ly] = [cardLocation.get(cardNum)[1][0], cardLocation.get(cardNum)[1][1]];

    let [nx1,ny1,distance1] = bfs(sx,sy,fx,fy,board);
    let [nx2,ny2,distance2] = bfs(nx1,ny1,lx,ly,board);

    remove(cardNum,board,cardLocation);
    backTracking(nx2,ny2,iterIdx+1,outerPermutationNum,count+distance1+distance2,board,cardLocation,permutation);
    restore(cardNum,board,cardLocation);

    [nx1,ny1,distance1] = bfs(sx,sy,lx,ly,board);
    [nx2,ny2,distance2] = bfs(nx1,ny1,fx,fy,board);

    remove(cardNum,board,cardLocation);
    backTracking(nx2,ny2,iterIdx+1,outerPermutationNum,count+distance1+distance2,board,cardLocation,permutation);
    restore(cardNum,board,cardLocation);
}
function solution(board, r, c) {
    const cardLocation = new Map();
    for(let i=0; i<4; i++){
        for(let j=0; j<4; j++){
            const cardNum = board[i][j];
            if(cardNum !== 0){
                if(cardLocation.has(cardNum)){
                    cardLocation.set(cardNum,[...cardLocation.get(cardNum),[i,j]]);
                }else{
                    cardLocation.set(cardNum,[[i,j]]);
                }
            }
        }
    }
    // console.log([...cardLocation.keys())
    const resultPermutation = permutation([...cardLocation.keys()],cardLocation.size);
    for(let i=0; i<resultPermutation.length; i++){
        backTracking(r,c,0,i,0,board,cardLocation,resultPermutation);
    }
    // console.log(cardLocation);
    return answer;
}
console.log(solution([[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]],1,0));
