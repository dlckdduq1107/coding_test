const select_wall = (start,count)=>{//벽3개 선택하는 함수
    if(count === 3){//벽 3개 선택했을때
        let temp_graph = JSON.parse(JSON.stringify(graph));//그래프 딥카피(이후에 또 수정되어야 하기 때문)
        for(let i=start; i<n*m; i++){// 그래프의 모든 경우
            let x = parseInt(i/m);//행
            let y = i%m;//열
            if(graph[x][y] === 2){//바이러스일때
                spread_virus(temp_graph,x,y);//바이러스 퍼뜨리기
            }
        }
        let count_safe=0;//안전지역 개수 카운트
        temp_graph.forEach(array => {//그래프를 돌면서 안전지역 카운트
            let t = array.filter((val)=>(val === 0));//0인 것만 배열로 리턴
            count_safe += t.length;//배열 개수 더해주기
        });
        max_safe = Math.max(max_safe,count_safe);//안전지역 최대 업데이트
    }
    else{//벽이 3개 미만일때
        for(let i=start; i<n*m; i++){//모든 경우 돌면서
            let x = parseInt(i/m);//행
            let y = i%m;//열
            if(graph[x][y] === 0){//빈 공간일때 
                graph[x][y] = 1;//벽세우고
                select_wall(start,count+1);//다음 벽 세우기로 
                graph[x][y] = 0;//원래상태로 돌려 놓기
            }
        }
    }
}

const spread_virus = (temp_graph,x,y)=>{//바이러스 퍼뜨리기
    for(let i=0; i<4; i++){//4방향으로
        let nx = x+dx[i];
        let ny = y+dy[i];
        if(nx>=0 && nx < n && ny>=0 && ny<m && temp_graph[nx][ny] === 0){//범위내에 있고, 빈공간 일때
            temp_graph[nx][ny] = 2;//바이러스 퍼뜨리기
            spread_virus(temp_graph,nx,ny);//다음 위치로 이동해서 퍼뜨리기
        }
    }
}

//리눅스이면 백준이므로 인풋 아니면 테스트
const input = stdin = (process.platform === 'linux')? require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n")
:`7 7
2 0 0 0 1 1 0
0 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 0 0
0 0 0 0 0 1 1
0 1 0 0 0 0 0
0 1 0 0 0 0 0`.split("\n");
const [nm,...rest] = input;
const [n,m] = nm.split(" ").map((val)=>Number(val));


let graph = rest.map((val)=>val.split(" ").map((a)=>Number(a)))
let dx = [0,0,1,-1];
let dy = [1,-1,0,0];
let max_safe = 0;

select_wall(0,0);
console.log(max_safe);

