const fs = require("fs");
const filePath = process.platform === "linux" ? "dev/stdin" : "example.txt";
const input = fs.readFileSync(filePath).toString().trim().split(" ");
var a = parseInt(input[0]);
var b = parseInt(input[1]);

console.log(a + b);
