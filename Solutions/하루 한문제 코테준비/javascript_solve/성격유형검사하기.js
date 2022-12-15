function solution(survey, choices) {
  var answer = "";
  const eachPersonal = [
    ["R", "T"],
    ["C", "F"],
    ["J", "M"],
    ["A", "N"],
  ];
  const result = { R: 0, T: 0, C: 0, F: 0, J: 0, M: 0, A: 0, N: 0 };

  survey.forEach((val, idx) => {
    const [first, second] = val.split("");
    // console.log(first, second);
    if (choices[idx] > 4) {
      result[`${second}`] += choices[idx] - 4;
    } else if (choices[idx] < 4) {
      result[`${first}`] += 4 - choices[idx];
    }
  });
//   console.log(result);
  for (let i = 0; i < eachPersonal.length; i++) {
    const [first, second] = eachPersonal[i];
    if (result[`${first}`] < result[`${second}`]) {
      answer += `${second}`;
    } else {
      answer += `${first}`;
    }
  }
  return answer;
}
console.log(solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5]));
