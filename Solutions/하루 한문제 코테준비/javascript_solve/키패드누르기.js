function solution(numbers, hand) {
  var answer = "";
  const keypad = {
    1: [0, 0],
    2: [0, 1],
    3: [0, 2],
    4: [1, 0],
    5: [1, 1],
    6: [1, 2],
    7: [2, 0],
    8: [2, 1],
    9: [2, 2],
    "*": [3, 0],
    0: [3, 1],
    "#": [3, 2],
  };
  let left = keypad["*"];
  let right = keypad["#"];
  numbers.forEach((val) => {
    if ([1, 4, 7].includes(val)) {
      answer += "L";
      left = keypad[val];
    } else if ([3, 6, 9].includes(val)) {
      answer += "R";
      right = keypad[val];
    } else {
      let leftDistance =
        Math.abs(keypad[val][0] - left[0]) + Math.abs(keypad[val][1] - left[1]);
      let rightDistance =
        Math.abs(keypad[val][0] - right[0]) +
        Math.abs(keypad[val][1] - right[1]);

      if (leftDistance < rightDistance) {
        answer += "L";
        left = keypad[val];
      } else if (leftDistance > rightDistance) {
        answer += "R";
        right = keypad[val];
      } else {
        if (hand === "left") {
          answer += "L";
          left = keypad[val];
        } else {
          answer += "R";
          right = keypad[val];
        }
      }
    }
  });
  return answer;
}
console.log(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"));
