const fs = require("fs");
const filePath = process.platform === "linux" ? "dev/stdin" : "example.txt";

const [N, NInput, M, MInput] = fs
  .readFileSync(filePath)
  .toString()
  .trim()
  .split("\n");
const NInputArr = NInput.trim().split(" ");
const MInputArr = MInput.trim().split(" ");

const set = new Set(NInputArr);

for (let i = 0; i < M; i++) {
  if (set.has(MInputArr[i])) {
    console.log(1);
  } else {
    console.log(0);
  }
}
