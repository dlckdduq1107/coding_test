const input = stdin = (process.platform === 'linux')? require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n")
:`2
10
1 1220 1340
2 1155 1220
2 1220 1340
3 1220 1240
1 1200 1320
2 1250 1310
2 1330 1550
3 1030 1130
3 1130 1300
3 1240 1330
3
1 0500 2200
1 0000 0700
1 2000 2359`.split("\n");

let [n,...rest] = input;
let current=0;//인풋에 대한 현재 인덱스
for(let i=0; i<n; i++){//n만큼 반복
    let games = {};//날짜별 게임 객체
    let ca = parseInt(rest[current++]);//경기수에 대한 입력 추출
    for(let j=0; j<ca; j++){//경기수 만큼
        let [d,s,e] = rest[current].split(" ");//날짜,시작,끝 추출
        (d in games)?games[d].push([s,e]):games[d] = [[s,e]];//날짜별 경기 객체에 추가
        current +=1;//다음 케이스를 처리하기 위한 현재인덱스 +
    }

    let max_count = 0;//볼수 최대 경기수
    for(let day in games){//객체 반복
        games[day].sort((a,b)=>(a[1]-b[1]));//두번째 요소를 기준으로 정렬
        let cTime = 0;//현재 시간
        games[day].forEach(val => {
            if(cTime <= val[0]){//현재시간이 경기시작시간보다 작으면
                max_count +=1;//볼수 있으므로 +1
                cTime = val[1];//경기 끝 시간을 현재시간으로
            }
        });
    }
    console.log(`Scenario #${i+1}:\n${max_count}\n`);
}
