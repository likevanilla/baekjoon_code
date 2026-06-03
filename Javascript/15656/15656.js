const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "example.txt";
const input = fs
  .readFileSync(filePath)
  .toString()
  .trim()
  .split(/\s+/)
  .map(Number);

const N = input[0];
const M = input[1];
const A = input.slice(2).sort((a, b) => a - b);

const selected = [];
const answer = [];

function DFS(depth) {
  if (depth === M) {
    answer.push(selected.join(" "));
    return;
  }

  for (let i = 0; i < N; i++) {
    selected.push(A[i]);
    DFS(depth + 1);
    selected.pop();
  }
}

DFS(0);

console.log(answer.join("\n"));