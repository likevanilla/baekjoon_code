function solution(array, commands) {
  var answer = [];
  for (let n = 0; n < commands.length; n++) {
    new_arr = array.slice(commands[n][0] - 1, commands[n][1]);
    new_arr.sort((a, b) => a - b);
    result = new_arr[commands[n][2] - 1];
    answer.push(result);
  }

  return answer;
}
