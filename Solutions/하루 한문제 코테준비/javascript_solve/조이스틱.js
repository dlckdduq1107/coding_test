function solution(name) {
  var answer = 0;
  let minNum = name.length - 1;
  for (let i = 0; i < name.length; i++) {
    const a = name.charCodeAt(i) - 65;
    // console.log(25 - a, a);
    answer += Math.min(26 - a, a);
    
    let index = i + 1;
    while (index < name.length && name[index] == "A") index++;

    minNum = Math.min(minNum, i * 2 + name.length - index);
    minNum = Math.min(minNum, (name.length - index) * 2 + i);
  }

  return answer + minNum;
}
console.log(solution("JEROEN"));
console.log(solution("JAN"));
