## 예시를 example.txt 파일로 저장

## index.js에서 소스 코드 작성
여기서 주의할 점은 예시파일의 경로 변경이다.
/dev/stdin 를 입력해 준 부분을 지우고 txt 파일로 저장된 예시의 경로로 변경해 준다.

## js 파일 실행
1. node JS파일
2. control + option + N

## 한 줄에 공백으로 값이 들어올 때
1 2 로 들어올 때

```js
const input = fs.readFileSync(filePath).toString().trim().split(' ');
var a = parseInt(input[0]);
var b = parseInt(input[1]);
```
input 변수에 공백으로 split한 문자들이 array 형태로 들어온다. parseInt를 통해서 하나하나 분리한다.

## 한 줄에 하나씩 값이 들어올 때
1
2
처럼 개행을 기준으로 값이 하나씩 들어올때
```js
const input = fs.readFileSync(filePath).toString().trim().split("\n");
```
'\n' 개행문자로 split한다.

## 첫 번째 줄에는 길이(n), 두 번째 줄에 공백으로 구분된 값이 주어질 때

```js
/*
3
121 1231 12421
*/
const [n, input] = fs.readFileSync("./input.txt").toString().trim().split("\n");
const inputArr = input.trim().split(" ")

console.log(n);	// 3 
console.log(input);	// 121 1231 12421
console.log(inputArr);	// [ '121', '1231', '12421' ]
```

## 첫 번째 줄에는 길이(n), 두 번째 ~ n개의 줄까지 각각의 값이 주어질 때
```js
/*
3
121
1231
12421
*/
const [n, ...input] = fs.readFileSync("./input.txt").toString().trim().split("\n");

console.log(n);	// 3
console.log(input);	// [ '121', '1231', '12421' ]
```

## /r이 함께 출력되는 경우
```js
const fs = require('fs');
const input = fs.readFileSync('./input.txt', 'utf-8').trim().split('\n').map(line => line.replace('\r', ''));
```

## 공백과 줄바꿈을 한 번에 처리하는 방법
```js
/*
5 2
4 1 2 3 5
*/
const input = fs.readFileSync(filePath).toString().trim().split(/\s+/);

const A = input[0]
const B = input[1]
const C = input.slice(2)

console.log(A) // 5
console.log(B) // 2
console.log(C) // [4, 1, 2, 3 5]
```
